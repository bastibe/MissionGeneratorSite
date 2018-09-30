------------------------------------------------------------------------
title: First Patch
date: 2018-09-30

I just uploaded a quick bug fix for the most important issues in the
release. This bug fix release contains:

- Corrected payload generation (should no longer try to cram ten 20kg
  people into a five-seat aircraft)
- Take-offs from non-default add-on airports no longer messes up the
  Mission Generator.
- Adds some logging, which should make debugging easier in case you find
  more problems.

There is still a known issue with add-on airports that change the runway
layout of default airports. In this case, you might get an incorrect
landing centerline deviation. I am working to fix that, but it is a
major undertaking which will take a while.

If you find more bugs, please post them to the [Mission Generator forum
topic](https://forums.x-plane.org/index.php?/forums/forum/430-mission-generator/).

------------------------------------------------------------------------
title: Released!
date: 2018-09-29

The Mission Generator for X-Plane has been released on the X-Plane.org
store! You can [buy it now for $15](https://store.x-plane.org/Mission-Generator_p_877.html)!

Additionally, we now have a [forum
topic](https://forums.x-plane.org/index.php?/forums/forum/430-mission-generator/)
for release announcements, discussions, and bug reports, which is
exciting!

Thank you very much for your support during the development of this
plugin. In particular, I would like to thank the beta testers, whose
comments improved many aspects of the plugin. And I would like to
thank all the nice commenters on the forums. You have no idea how
motivating a few positive remarks can be!

------------------------------------------------------------------------
title: The code
date: 2018-09-26

The last few days I spent cleaning up the Mission Generator's code, and
documenting it thoroughly. One could argue that no-one will look at the
code of an X-Plane plugin, anyway, so why document it?

But I plan that the initial release of the Mission Generator will only
the first step in a long development. Which means that I will work with
this code for a long time. Spending some effort now to help future me,
who will have forgotten half the intricacies of the Mission Generator,
is time well spent.

But beyond that, I hope that other people will look at the code, and try
to improve things. While the Mission Generator is a commercial piece of
software, I give every user express permission to publish improved
versions of a few key files. This might, for example, include more
varied bonus missions, or more mission templates, or re-balanced
versions of the level ups.

I also hope that the Mission Generator will encourage people to develop
their own plugins. As it turns out, writing plugins for X-Plane is not
hard (if you know programming). There are a lot of intricate and
interesting algorithms in the Mission Generator, and all of them are now
well-documented for intrepid readers.

And of course, old habits die hard. I always try to maintain as good a
code quality as I can in [my programming projects](https://github.com/bastibe).

------------------------------------------------------------------------
title: Getting the Mission Generator ready for release
date: 2018-09-22

As far as I can tell, all major bugs in the Mission Generator have now
been fixed. Now, all that remains is to get this website up and
running, and getting the plugin listed on the X-Plane.org Store.

This is very exciting, since I have never done a commercial project
before, and don't know what to expect!
