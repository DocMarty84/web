+++
title = "Release of v0.6.0"
date = "2017-05-24T03:00:00+02:00"
archives = "2017"
+++

After a v0.5.0 which brought only a limited number of changes, the v0.6.0 is released with a
featured already feared by Youtube: video support!

Alright, maybe Youtube is not yet that impressed, but who knows ;-) Similarly to Subsonic, KooZic
now supports video streaming, meaning that videos stored on the server can be converted in real time
and broadcasted wherever you want.

# Video streaming

In KooZic, videos are handled differently than in Subsonic. The video library is completely
separated from the music library. It is available thanks to a new Odoo module
([OOVideo](https://github.com/docmarty84/oovideo)). Navigation is achieved thanks to file browsing,
with a similar look and feel than the file browsing available in the music library.

[![01](/img/post/release-of-v0-6-0/01-thumb.png#center)](/img/post/release-of-v0-6-0/01.png)

[Clapper](http://clappr.io/) has been selected as player, alongside with an extension to support
subtitles ([Clapper-Subtitle](https://github.com/JMVTechnology/Clappr-Subtitle)). The player uses
the HTML5 capabilities of the web browser, so no need of any plug-in to make it work. The ugly
interfaces allows you to choose the bitrate, the resolution, the language track and the subtitle
track (SRT format only).

[![02](/img/post/release-of-v0-6-0/02-thumb.png#center)](/img/post/release-of-v0-6-0/02.png)

At the moment, every change implies to reload the media. That's not really sexy nor very convenient,
but that does the job. Great thing is that it allows you to fine tune the quality to take full
advantage of your bandwidth and server capabilities. Similarly to the music library, FFMpeg takes in
charge the real-time transcoding. The option "Raw" loads the video without any encoding. This
obviously works only for video formats supported by the browser.

In the future, these options **could** be integrated as Clappr extensions.

# Other features

Next to video support, the v0.6.0 implements the lastest version of
[the Subsonic API](http://www.subsonic.org/pages/api.jsp). This is the v0.15.0 of the API,
corresponding to Subsonic v6.1. As always, Odoo is updated, which includes minor corrections and
security flaws patching.

# Upgrade of an existing installation

To upgrade an existing installation, first download the new version from the
[download page](http://koozic.net/download/) and turn off your running server. Extract the sources
and run in the newly extracted folder:

```
./odoo-bin -u oomusic -d koozic --stop-after-init
```

When the upgrade process is over, start again your server and enjoy!

For video support, you will need **mediainfo**. On Ubuntu:

```
sudo apt install mediainfo
```

Then, switch to the debug mode. Change the URL from:

```
http://localhost:8069/web#view...
```

To:

```
http://localhost:8069/web?debug#view...
```

In "Apps", click on "Update Apps List", and validate. Click again on the sub-menu "Apps": you will find OOVideo.
