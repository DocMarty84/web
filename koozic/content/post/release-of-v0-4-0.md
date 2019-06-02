+++
title = "Release of v0.4.0"
date = "2017-03-11T03:00:00+02:00"
archives = "2017"
+++

The new version of KooZic (v0.4.0) is officially out! Six months after the release of the very first
version, a big step forward has been achieved with a new folder browsing view. This should satisfy
people who don't have a library correctly tagged.

KooZic was created with ID3 tags in mind. It is still the strength of the software since it gives
you access to tracks, albums, artists or genres effortlessly, whether other softwares provide
limited capabilities. However, if spending hours to tag your music collection is not your cup of
tea, KooZic is not really usable. A folder browsing mode was introduced back in v0.2.0, but it was
not handy.

# Folder browsing

The new browsing mode follows the same foundations that the software: a clear and easy access to the
essential functionalities, whatever the size of the library.

[![01](/img/post/release-of-v0-4-0/01-thumb.png#center)](/img/post/release-of-v0-4-0/01.png)

The first element of the list is the current folder. The second ('..') allows to come back to the
parent folder. Then, the list of sub-folders and the list of tracks. It is possible to add to the
current playlist all tracks of a folder by clicking on '+'. A track is added with a simple click.

[![02](/img/post/release-of-v0-4-0/02-thumb.png#center)](/img/post/release-of-v0-4-0/02.png)
[![03](/img/post/release-of-v0-4-0/03-thumb.png#center)](/img/post/release-of-v0-4-0/03.png)

# Current playlist

The interaction with the current playlist has been improved. A click on a track launches the
playback, and using the button 'Play', which has disappeared. The track highlighted is updated
automatically at every track change, not only when the whole page is refreshed. That is clearly a
minor enhancement, but that globally improves the user friendliness.

# Upgrade of an existing installation

To upgrade an existing installation, first download the new version from the
[download page](/download/) and turn off your running server. Extract the sources and run in the
newly extracted folder (watch out: it is **\-u web**):

```
./odoo-bin -u web -d koozic --stop-after-init
```

When the upgrade process is over, start again your server and enjoy!
