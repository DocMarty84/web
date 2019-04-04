+++
title = "Release of v0.7.0"
date = "2017-09-01T03:00:00+02:00"
tags = []
categories = ["release"]
type = "blog"
banner = "img/news/release-of-v0-7-0/banner.jpg"
+++

KooZic will soon be blowing its first candle as we are progressively reaching a satisfying result in
terms of functionalities, stability and performances. In the meantime, the v0.7.0 is bringing some
nice new views, amongst bug fixes and performance improvements.

# Artists Thumbnails

KooZic retrieves artist information from LastFM since [v0.2.0](/2016/11/05/release-of-v0-2-0/). We
retrieve the biography, top songs, similar artists... but not the images. It is the case as of
v0.7.0, with an extra artist thumbnails view.

[![01](/img/news/release-of-v0-7-0/01-thumb.png#center)](/img/news/release-of-v0-7-0/01.png)

It makes browsing more pleasant ;-) Moreover, the artist image is used in the music panel if the
album cover cannot be found.

# Preview Mode

Until today, playing a track would always require to go through a playlist. You couldn't simply
'play' a song, you had to add it to a playlist, then play it. It was a design choice made for the
sake of coding simplicity, but that wasn't user friendly. From v0.7.0, it is possible to start
playing a song from anywhere (artist view, album view...). Just press the 'Play' button. At the end
of the song, the player will switch back to the current playlist.

# Statistics

You always wanted to get some statistical insights to your music library? For example, what are the
most common music genres? The v0.7.0 brings that feature! Thanks to the out-of-the-box Odoo tools, a
graph and a pivot view are available.

[![02](/img/news/release-of-v0-7-0/02-thumb.png#center)](/img/news/release-of-v0-7-0/02.png)

The views are available for albums, but also for tracks.

[![03](/img/news/release-of-v0-7-0/03-thumb.png#center)](/img/news/release-of-v0-7-0/03.png)

The latest view ('pivot') is great to spot duplicated content ("Pop/Rock" and "Pop-Rock", for
example), as well as getting detailed information.

# Other Features

A lot of effort has been made in order to rewrite some parts of the code in order to make them more
readable and increase the performances. Actually, this is the major part of the v0.7.0 release,
although this is not the most striking visually ;)

# Upgrade of an existing installation

To upgrade an existing installation, first download the new version from the
[download page](/download/) and turn off your running server. Extract the sources and run in the
newly extracted folder:

```
./odoo-bin -u oomusic,oovideo -d koozic --stop-after-init
```

When the upgrade process is over, start again your server and enjoy!
