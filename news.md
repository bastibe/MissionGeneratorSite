------------------------------------------------------------------------
title: Fifth Patch (v1.1.2)
date: 2018-10-20

It seems that all major issues have actually been resolved as of the
previous version. Thus, I can now finally focus on refining the
experience, and start tackling subtler issues and preferences. This
patch is full of small improvements that don't change the game, but
should make for a smoother experience.

For example, there was an interesting issue with helicopters: When a
helicopter touches down, it immediately finishes the current mission
and unloads the payload. Normally, this is not an problem. But in
*some* cases, with particularly heavy payloads and particularly smooth
touch downs, taking off the payload would make the helicopter light
enough to float up again! So with v1.1.2, helicopter missions will
only finish once touched down *and* the collective is reduced (see
settings.lua for the particular threshold).

Another issue were taxi speeds and cruise speeds. The centerline
deviation is only calculated if the aircraft is moving faster than the
taxi speed, but a perfectly reasonable taxi speed for a passenger jet
will be far beyond the takeoff speed of small ultralights. So now the
taxi speed is determined either by a minimum of 30 km/h, or a quarter
of the stall speed, whichever is higher (Again, adjustable in
settings.lua). Similarly, the cruise speed is now the mean of the
maneuvering speed and top speed (center of the yellow arc), which is
probably conservative for turbine-powered aircraft, and a bit too fast
for piston aircraft, but in any case much better than before.

A third issue was a real head-scratcher: Sometimes, some X-Plane
datarefs would apparently contain invalid data. This seems to happen
randomly, but more often at very low frame rates (which I don't run)
and in conjunction with a lot of other plugins (which I don't use). As
such, I could never reproduce these issues. The root cause is probably
a bug in SASL or X-Plane, and not under my control. And in any case,
most of the time, these little hickups would not matter much, and
merely cause a transient error in the X-Plane log or a short flicker
on the briefing screen. But *sometimes*, in very rare cases, they
would block mission progress, or prevent mission success. I have added
workarounds for these cases, which will hopefully make them
unproblematic.

And finally, there are of course a number of additional bug fixes,
like fixes for the payload name generation, time formatting in the
briefing and debriefing, overly-unreliable missions, and a renamed
menu item.

------------------------------------------------------------------------
title: Fourth Patch (v1.1.1)
date: 2018-10-08

The last patch (v1.1.0) added the ability to rebuild the Mission
Generator's scenery database from the actual sceneries' apt.dat files.
While this fixed many issues, some people had add-on sceneries with
incorrectly formatted apt.dat files, which tripped up the database
crawler.

The resulting incomplete scenery database lead to empty mission lists or
even freezes when opening the mission list (if you had one of those
malformed sceneries). As always, this problem did not happen on my
machine, since none of my sceneries had these problems.

Thus, I now added some scenery validation code which should prevent
malformed apt.dat files from messing up the whole scenery database.

Additionally, the patch fixes a bunch of smaller issues, such as payload
issues, mission distance issues, and more mission templates. And I have
a new theory on why the centerline deviation is sometimes way off: It
might be because the Mission Generator interprets taxiing too fast as
part of the takeoff roll. If you experience the centerline issue, try
taxiing slower than 30 km/h (15 kt).

------------------------------------------------------------------------
title: Third Patch (v1.1.0) (fixes the Centerline Issue)
date: 2018-10-05

As reported before, the Mission Generator used to report incorrect
centerline deviations for certain third-party sceneries, and would
never show some sceneries as mission destinations.

Both of these issues were due to X-Plane not giving plugins
information about runways, which meant that the Mission Generator used
its own runway database that I created offline from X-Plane's apt.dat.

Of course, this database would not show any changed runway layouts or
added runways from third-party sceneries, or X-Plane's own global
airport updates.

As of v1.1.0, the Mission Generator intelligently reads your installed
sceneries, and builds a new runway database every time you install a
new scenery. The process can take a few seconds to finish, but it is
only run if your scenery changes. If you think it might not have
picked up on a new scenery, you can also start the rebuild manually
from the menu bar.

------------------------------------------------------------------------
title: Second Patch (v1.0.2)
date: 2018-10-01

- Fixes debriefing issue (thank you, shaja, for finding and [fixing](https://forums.x-plane.org/index.php?/forums/topic/159020-not-recognizing-completed-missions/&do=findComment&comment=1495812) it!)

------------------------------------------------------------------------
title: That Centerline Issue
date: 2018-10-01

Some people are seeing an issue where the Takeoff centerline deviation
and landing centerline deviation are wildly off. This is caused by
add-on airports, or an updated apt.dat, which moved the runway
locations.

Since X-Plane does not give plugins information about the locations of
runways, the Mission Generator has its own database of runway locations,
derived from X-Plane's default apt.dat. Thus, if an add-on moves the
runway locations, the Mission Generator won't know about it, and will
assume you landed in the wheeds.

To fix this, I will add a new menu option to rebuild the scenery
database in a future update. But this is a bigger undertaking, and will
take a few days.

As a nice side benefit, this will make completely new add-on airports
available as mission targets as well.

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
