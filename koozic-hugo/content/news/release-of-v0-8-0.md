+++
title = "Release of v0.8.0, last release..."
date = "2018-04-06T03:00:00+02:00"
tags = []
categories = ["release"]
type = "blog"
banner = "img/news/release-of-v0-8-0/banner.jpg"
+++

... using Python 2! The last few months have been rather quiet regarding KooZic. The development
didn't stop, though. Several features have been added. Among others, the support of audio
normalization, non-transcoding, and a converter.

# Audio normalization

When playing one track after another, it is sometimes possible to perceive a non-negligible volume
difference. This can simply be explained knowing that each audio track has a defined volume level,
which can be different from one file to another. Obviously, when listening to a complete album, this
doesn't happen since the volume level is coherent from one track to the other. On the other hand,
when the tracks come from various sources, the volume level can vary significantly.

Many audio players feature the volume normalization thanks to the
[ReplayGain](https://en.wikipedia.org/wiki/ReplayGain) method. More recently, the broadcast industry
has agreed on another normalization method, aka [EBU R128](https://tech.ebu.ch/loudness) (European
Broadcasting Union Recommendation R128). FFMpeg supports natively this method from 3.2.1. Nice,
isn't it?

[![01](/img/news/release-of-v0-8-0/01-thumb.png#center)](/img/news/release-of-v0-8-0/01.png)

From v0.8.0, it is possible to parametrize a playlist so that the normalization method is applied to
all tracks. This functionality requires FFMpeg >= 3.2.1. Please note that a cross-distribution
binary executable is now provided with KooZic. You can simply copy it to '/usr/local/bin', and you
should be good to go.

It is important to stress out that normalization is a resource-consuming process, and thus increases
substantially the conversion time. It's up to you to check if your server is capable of handling
such an extra load.

# And what about converting like, not at all?

The exact opposite option has also been introduced in this release. We can take advantage of our
modern browsers' audio playing capabilities to skip any pre-processing.

[![02](/img/news/release-of-v0-8-0/02-thumb.png#center)](/img/news/release-of-v0-8-0/02.png)

It is now possible to parametrize a playlist in order to completely avoid the use of FFMpeg, to
simply read the file as it is stored on the server. This allows a major reduction of the server
load, at the cost of an increase in the network traffic.

It is worth pointing out that the results may vary depending on your browser (even from one version
to another). However, that still can be a very useful option depending on your set-up.

# An audio converter tool, but for which purpose?

Long story short: because I needed one. An endless number of tools exist in order to convert an
audio file from one format to another. Most of them are doing a great job. But, to my knowledge,
none of them allows to easily import a playlist and convert it, while respecting the file/folder
organization. KooZic can do it.

[![03](/img/news/release-of-v0-8-0/03-thumb.png#center)](/img/news/release-of-v0-8-0/03.png)

Similarly to playlists, one can easily create a list of file to convert. It is also possible to
import an existing playlist. One chooses the conversion mode, the quality (bitrate), the output
folder ('/tmp/koozic/' by default), and press 'Run'. The conversion starts asynchronously after less
than 2 minutes. Nothing really sexy, one needs to realod the page to see the progression. But that
does the job, and it is efficient.

# Other Features

Amongst the the more noticeable features, the pre-loading of the upcoming track is one of the most
important. 30 seconds before the end of a track, KooZic preloads the next track. This allows to
reduce significantly the gap between tracks, and to get a 'almost gapless' feature.

As announced at the beginning of this article, this is the last version using Python 2 (Odoo v10).
The upcoming versions will use Python 3 (Odoo v11).

# Upgrade of an existing installation

To upgrade an existing installation, first download the new version from the
[download page](/download/) and turn off your running server. Extract the sources and run in the
newly extracted folder:

```
./odoo-bin -u oomusic,oovideo -d koozic --stop-after-init
```
