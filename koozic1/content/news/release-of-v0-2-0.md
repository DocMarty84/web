+++
title = "Release of v0.2.0"
date = "2016-11-05T03:00:00+02:00"
tags = []
categories = ["release"]
type = "blog"
banner = "img/news/release-of-v0-2-0/banner.jpg"
+++

Today, we are excited to announce the release of v0.2.0!

# Features

The major new feature is the support of LastFM artist information: biography, top tracks and similar
artists. All top tracks and artists which are found in your library are displayed in the "Top
Tracks" and "Similar Artists" tabs of an artist.

[![01](/img/news/release-of-v0-2-0/01-thumb.png#center)](/img/news/release-of-v0-2-0/01.png)
[![02](/img/news/release-of-v0-2-0/02-thumb.png#center)](/img/news/release-of-v0-2-0/02.png)

It is not easy to use the software in case the ID3 tags of the music library are not set correctly.
A new view as been added in order to browse the collection by folder.

[![03](/img/news/release-of-v0-2-0/03-thumb.png#center)](/img/news/release-of-v0-2-0/03.png)

Other minor improvements have been added:

*   rating of artists, albums or tracks
*   set artist as favorite
*   force full scan of a folder

# Upgrade of an existing installation

To upgrade an existing installation, first download the new version from the
[download page](/download/) and turn off your running server. Extract the sources and run in the
newly extracted folder:

```
./odoo-bin -u oomusic -d koozic --stop-after-init
```

When the upgrade process is over, start again your server and enjoy!
