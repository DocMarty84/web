+++
title = "Release of v0.3.0"
date = "2017-01-12T03:00:00+02:00"
tags = []
categories = ["release"]
type = "blog"
banner = "img/news/release-of-v0-3-0/banner.jpg"
+++

The new version of KooZic (v0.3.0) is officially out!

# Support of the Subsonic API

The main feature of v0.3.0 is the support of the Subsonic API. Practically, it means that any
third-party application compatible with a Subsonic server is compatible with KooZic out of the box!
The efforts have been focused on the support of mobile applications, on both Android and iOS
devices. The goal was to support as many features as possible, and so far we could achieve an
excellent support for the main purpose of KooZic: music streaming ;-) Oh, and by the way: no license
fees with KooZic!

#### Full support

*   Audio streaming
*   Browse library with and without ID3 tags
*   Predefined lists, such as latest albums or tracks, most played...
*   List of albums by genre
*   Fetch and delete playlists
*   Fetch artists and albums informations from LastFM

#### Partial support

*   Playlist modifications (due to a technical limitation)

#### Not supported

*   Podcasts
*   Shares
*   Chat
*   User management (on purpose, for security reason)
*   Video streaming

In the future, video streaming might be supported. Regarding the other unsupported features, their
usefulness is rather limited in 2017...

### Compatibility of mobile applications

Here is a list of mobile applications, and their compatibility with KooZic.

#### Android

Three applications were tested amongst the most popular ones. Their compatibility with KooZic is
excellent, whatever your choice is.

*   [DSub](https://f-droid.org/repository/browse/?fdid=github.daneren2005.dsub): probably the best
    choice, actively developed. You should definitively have a look at its numerous features!
*   [UltraSonic](https://play.google.com/store/apps/details?id=org.moire.ultrasonic): a very good
    choice, although less fancy features than DSub. Anyway, perfectly suitable for a daily use.
*   [Subsonic Music Streamer](https://play.google.com/store/apps/details?id=net.sourceforge.subsonic.androidapp):
    the official client. More a proof-of-concept than an application that you would use on a daily
    basis.

#### iOS

On iOS, three applications were also tested. Once again, the compatibility with KooZic is very good.

*   [play:Sub](https://itunes.apple.com/us/app/play-sub-subsonic-music-streamer/id955329386?mt=8):
    probably the best choice (and the best app), actively developed. Subjectively even better than
    DSub...
*   [AVSub](https://itunes.apple.com/us/app/avsub/id923424694?mt=8): a lot of features, although not
    really in line with the iOS design.
*   [Soundwaves](https://itunes.apple.com/app/soundwaves/id736139596?mt=8): a free app! It focuses
    on music streaming and leaves aside the fancy stuff. Anyway, it does it pretty well.

This feature is available for testing on our demo server. To connect your app, use the following
information:

*   URL: http://demo.koozic.net:8069
*   login: demo
*   password: demo

# Additional features

A new menu gives a quicker access to musical genres organization. For a given genre, you can find
the list of artists and albums related.

[![01](/img/news/release-of-v0-3-0/01-thumb.png#center)](/img/news/release-of-v0-3-0/01.png)
[![02](/img/news/release-of-v0-3-0/02-thumb.png#center)](/img/news/release-of-v0-3-0/02.png)

Aside from the Subsonic support, most of the development focused on performance improvements and
maintainability. Image caching has been simplified and rationalized, while LastFM caching mechanism
has been completely rewritten to make it much more flexible. However, nothing noticeable for the end
user, except a few visual tweaks here and there.

# Upgrade of an existing installation

To upgrade an existing installation, first download the new version from the
[download page](/download/) and turn off your running server. Extract the sources and run in the
newly extracted folder:

```
./odoo-bin -u oomusic -d koozic --stop-after-init
```

When the upgrade process is over, start again your server and enjoy!
