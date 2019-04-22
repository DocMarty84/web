+++
title = "Release of v0.5.0"
date = "2017-04-13T03:00:00+02:00"
tags = []
categories = ["release"]
type = "blog"
banner = "img/news/release-of-v0-5-0/banner.jpg"
+++

About a month after the release of v0.4.0, the v0.5.0 is already out! Well, 'already out' is maybe
too much: there are few functional changes, but a major step forward for French translation.

Loading a new translation in KooZic is a piece of cake. However, you might have noticed that the
interface is partially translated. This is due to the fact that Odoo, the software on which relies
KooZic, is completely translated in many languages. However, the music extension is not. As of
today, only the French translation is available. Other translations can be added collaboratively on
the [POEdit project](https://poeditor.com/join/project/RMl91o65Bs). Aside from the translations,
improvements have been introduced in track sorting.

# Load a translation

To load a new translation, you must be connected as Administrator. Go to 'Settings', then 'Load a
Translation'.

[![01](/img/news/release-of-v0-5-0/01-thumb.png#center)](/img/news/release-of-v0-5-0/01.png)

Select a language, then click on 'Load'.

[![02](/img/news/release-of-v0-5-0/02-thumb.png#center)](/img/news/release-of-v0-5-0/02.png)
[![03](/img/news/release-of-v0-5-0/03-thumb.png#center)](/img/news/release-of-v0-5-0/03.png)

The last step is to change the language in the user's preferences.

[![04](/img/news/release-of-v0-5-0/04-thumb.png#center)](/img/news/release-of-v0-5-0/04.png)
[![05](/img/news/release-of-v0-5-0/05-thumb.png#center)](/img/news/release-of-v0-5-0/05.png)

Here we are!

[![06](/img/news/release-of-v0-5-0/06-thumb.png#center)](/img/news/release-of-v0-5-0/06.png)

### Contribute to the translation

As said previously, it is possible to contribute to the translation on the corresponding
[POEdit project](https://poeditor.com/join/project/RMl91o65Bs). At the moment, only French, German,
Italian and Spanish are available. If necessary, I will add other languages.

# Track sorting and album artist

The track sorting has been enhanced to take into account a numbering like '1', '2', '3' instead of
'01', '02', '03'. Moreover, the artist of an album will be defined with the following logic: if the
tag 'Album Artist' is filled in on the tracks, it is preferred. If it is not filled in, the tag
'Artist' is used.

# Upgrade of an existing installation

To upgrade an existing installation, first download the new version from the
[download page](/download/) and turn off your running server. Extract the sources and run in the
newly extracted folder:

```
./odoo-bin -u oomusic -d koozic --stop-after-init
```

It is also suggested to use a version of the Python library Mutagen >= v1.33. Indeed, the previous
versions suffer from a [bug](https://github.com/quodlibet/mutagen/issues/252) which incorrectly maps
the performer to the album artist (the FLAC tracks are not impacted). Unfortunately, the default
version in Ubuntu 16.04 is v1.22, which is affected by the bug. To upgrade:

```
sudo apt install python-pip
sudo pip2 install mutagen --upgrade
```

When the upgrade process is over, start again your server and enjoy! To take advantage of the new
track sorting, it is required to force a full scan on the existing folders. First, switch to the
debug mode. Change the URL from:

```
http://localhost:8069/web#view...
```

To:

```
http://localhost:8069/web?debug#view...
```

In 'Configuration > Folders', click on 'Force Full Scan'. Note that the scan duration will be
slightly longer than the initial scan, since a complete update of the library takes more time than
creating it.
