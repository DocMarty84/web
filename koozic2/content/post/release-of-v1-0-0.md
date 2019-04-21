+++
title = "Release of v1.0.0"
date = "2018-08-10T03:00:00+02:00"
archives = "2018"
+++

Does a version 1.0.0 mean a major refactoring of KooZic in comparison to
[v0.8.0](/2018/04/06/release-of-v0-8-0/)? Actually not at all. This instead refers to major internal
changes making both versions incompatible, which justifies a version jump. However, that doesn't
prevent some improvements and new features to be included in this version.

# Odoo v11.0 and Python 3

While versions 0.x were using [Odoo](https://www.odoo.com/) v10 and
[Python 2](https://pythonclock.org/), the branch 1.x uses Odoo v11 and Python 3. This is to make
sure KooZic's core is always up-to-date with latest technologies. Indeed, an Odoo version is
supported 3 years, while the Python 2 support will stop on January 1st 2020. We are not there yet,
but better keep a modern software!

# Download Links

It can always be handy to easily share a track or an album. The v1.0.0 introduces the possibility
to generate download links with one click. A link can be generated for a track, an album, an artist,
a musical genre or even a playlist. It can be shared easily: when the link is first accessed, a ZIP
archive is created with the corresponding files. It is possible to create several download links for
an object, and it is also possible to define a lifetime for each link.

[![01](/img/post/release-of-v1-0-0/01-thumb.png#center)](/img/post/release-of-v1-0-0/01.png)

# HTML5 or Web Audio

KooZic uses the web browser's abilities to read audio files, without the need of external plugins
(and hopefully, Flash died a long time ago). This is pretty good. However, this means that we rely
on the browser's good will when it comes to stream the audio file... and this is not funny.

In the naive approach used, the web browser completely handles the audio loading. With HTML5, the
modern browsers use a 'smart' mode: they only retrieve what is really necessary to avoid wasting
bandwidth. That seems to be a good approach... unless you are listening to some one-hour track (such
as a mega-mix). Indeed, this means that the connexion must remain opened during the playback time.
If the server or you Internet connection fails, the connexion will stop, and so the playback.

To circumvent this problem, a playlist can now use the
[Web Audio](https://developer.mozilla.org/docs/Web/API/Web_Audio_API) API. It gives the possibility
to apply sound effects to a track, but in our case KooZic will use it to completely preload the
track before loading. This implies a longer gap between tracks, but a much stable playback.

[![02](/img/post/release-of-v1-0-0/02-thumb.png#center)](/img/post/release-of-v1-0-0/02.png)

# Performance Improvements

Or more accurately, deactivation of resource-hungry processes :-) Until now, the settings were
limited. This was a design choice, the goal being to keep a simple interface and a basic
configuration adapted to all installations. Or that's what I was thinking... It was reported to me
extreme installations for which the default configuration was simply unusable. This led to the
introduction of several internal modifications to prevent the use of all resources. Moreover, 3
settings have been added:

*   Désactivation of scheduled actions
*   Default view without thumbnails
*   LastFM information fetched on-demand

[![03](/img/post/release-of-v1-0-0/03-thumb.png#center)](/img/post/release-of-v1-0-0/03.png)

This drastically reduces the workload in case of an installation with reduced resources (or a huge
music library).

# Other Features

The Subsonic API is available in XML (default) and JSON. I learned the hard way that there was no
standard conversion between the two formats, meaning that the JSON API support from KooZic was
pretty bad. Therefore, some softwares using this API instead of the XML API (e.g. Ultrasonic) were
not using properly. That should now be fixed.

# Upgrade of an existing installation

Unfortunately, the v1.0.0 is not compatible at all with previous versions. A new installation will
therefore ignore the previous configuration. However, the installation script makes it easy:

```
curl https://raw.githubusercontent.com/DocMarty84/koozic/11.0/extra/installer/koozic_install.py > k_install.py
chmod +x k_install.py
sudo ./k_install.py install
```

If you installed KooZic without the installation script, you will have to uninstall manually. Do not
hesitate to open an issue on [Github](https://github.com/docmarty84/koozic/issues) in case of
trouble!
