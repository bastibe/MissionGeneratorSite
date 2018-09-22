from markdown import markdown
import datetime

posts = []
with open('news.md') as newsfile:
    post = dict(content=[])
    front_matter = False
    for line in newsfile:
        if line.startswith('-----'):
            if post['content']:
                post['content'] = ''.join(post['content'])
                posts.append(post)
                post = dict(content=[])
            front_matter = True
        elif front_matter and line.startswith('title:'):
            post['title'] = line.split(':', 1)[1].strip()
        elif front_matter and line.startswith('date:'):
            post['date'] = datetime.datetime.strptime(line.split(':', 1)[1].strip(), '%Y-%m-%d')
        else:
            front_matter = False
            post['content'].append(line)
    if post['content']:
        post['content'] = ''.join(post['content'])
        posts.append(post)

posts = sorted(posts, key=lambda p: p['date'], reverse=True)


with open('news.xml', 'wt') as rss:
    rss.write(f'''<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
<channel>
<title>Mission Generator News</title>
<description>News for the Mission Generator plugin for X-Plane</description>
<link>https://missiongenerator.eu/news0.html</link>
<lastBuildDate>{datetime.datetime.now():%a, %d %b %Y %H:%M:%S %Z}</lastBuildDate>
''')

    for post in posts:
        rss.write(f'''
  <item>
    <title>{post['title']}</title>
    <pubDate>{post['date'].strftime('%a, %d %b %Y %H:%M:%S %Z')}</pubDate>
    <description><![CDATA[
{markdown(post['content'], tab_length=2)}
    ]]>
    </description>
  </item>
''')

    rss.write('''
</channel>
</rss>
''')


pages = []
while posts:
    if len(posts) > 5:
        pages.append(posts[:5])
        posts = posts[5:]
    else:
        pages.append(posts)
        posts = []

for idx, posts in enumerate(pages):
    with open(f'news{idx}.html', 'wt') as html:
        html.write('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="alternate"
      type="application/rss+xml"
      href="https://missiongenerator.eu/news.xml"
      title="Mission Generator News"/>
  <title>Mission Generator News</title>
  <meta name="author" content="Bastian Bechtold">
  <meta name="referrer" content="no-referrer">
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <link href="style.css" rel="stylesheet" type="text/css">
</head>

<body>
  <header>
    <a href="privacy.html">Privacy</a>
    <a href="about.html">About Me</a>
    <a href="news0.html">News</a>
    <a href="index.html">Home</a>
    <img src="icon.png"/>
    <h1>Mission Generator</h1>
    <h2>A plugin for X-Plane</h2>
  </header>

  <hr>
''')

        for post in posts:
            html.write(f'''
  <section class='post'>
    <h1 class='title'>{post['title']}</h1>
    <h2 class='date'>{post['date'].strftime('%Y-%m-%d')}</h2>
''')

            for line in markdown(post['content'], tab_length=2).splitlines():
                html.write('    ' + line + '\n')
            html.write('  </section>\n')

        html.write('''
  <section class="navigation">
''')
        if idx > 0:
            html.write(f'    <a class="prev" href="news{idx-1}.html">Previous Page</a>\n')
        if idx+1 < len(pages):
            html.write(f'    <a class="next" href="news{idx+1}.html">Next Page</a>\n')
        html.write('  </section>\n')

        html.write('''
</body>
</html>
''')

# magick icon.png -resize 64x64 favicon.ico
