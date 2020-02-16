+++
title = "Release of v3.0.0"
date = "2020-02-21T03:00:00+02:00"
archives = "2020"
+++

The last few months have been dedicated to update KooZic to v3. From a feature point-of-view, KooZic
is considered as a mature software. Therefore, most of the work is done under the hood. The codebase
is kept as clean as possible, and sometimes refactored to improve performance and stability.
Moreover, it is kept compatible with the latest versions of Python and PostgreSQL.

Do not hesitate to give it a test on [the demo server](https://demo.koozic.net/public) or follow the
[installation instructions](/installation/).

# Remote Control

The purpose of KooZic is to access the music library remotely. However, controlling the playback is
supposed to be done directly from the web interface.

In my use case, I ended up using KooZic to play music at home, from a media center. Indeed, the
customized smart playlists allow me to filter efficiently the type of music I want to play in the
room. I created a dynamic playlist and let it play for hundreds of hours. Still, I need to be able
to easily pause, skip the track or turn the volume up or down from my smartphone.

The new version introduces a simple remote control feature. It is possible to generate a unique URL
that allows controlling the player from any device.

[![01](/img/post/release-of-v3-0-0/01-thumb.png#center)](/img/post/release-of-v3-0-0/01.png)

When accessing this URL from a smartphone, a simple remote control gives access to the basic
playback actions.

[![02](/img/post/release-of-v3-0-0/02-thumb.png#center)](/img/post/release-of-v3-0-0/02.png)

Any remote action is captured and notified in the web interface.

[![03](/img/post/release-of-v3-0-0/03-thumb.png#center)](/img/post/release-of-v3-0-0/03.png)

If the remote control is configured as 'Public', anyone with the link can access the controls
without the need of a login. Any guest can therefore scan the QR code and control the playback.

It is important to note that **HTTPS must be configured** on your installation for this feature. A
detailed procedure is provided in the
[documentation](https://doc.koozic.net/installation/https.html).

# Other Features

v3 supports embedded cover art in M4A and Vorbis files (OGG, OGA, OPUS). It is also possible to add
the same tracks more than once in the same playlist, and purge the duplicates in a playlist.

# Upgrade of an existing installation

A new major version means an incompatibility with the previous version. It is therefore advised to
uninstall the v2 before installing the v3.

```
wget https://raw.githubusercontent.com/DocMarty84/koozic_install/v3/koozic_install.py -O koozic_install.py
```

To uninstall:

```
sudo python3 koozic_install.py uninstall
```

To install:

```
sudo python3 koozic_install.py install
```

It is then possible to connect to [http://localhost:8069/](http://localhost:8069/) with the
credentials 'admin' / 'admin'.

### Docker

1. Stop and remove the previous version: `docker-compose down`
2. Follow the [Docker installation instructions](https://koozic.net/installation/).

Do not hesitate to submit a [Github issue](https://github.com/docmarty84/koozic/issues) if
necessary!
