+++
title = "Installation"
+++

KooZic uses Python 3.5+, relies on PostgreSQL as a database system and FFmpeg for music
transcoding. It uses as a core system the Odoo software. KooZic is being extensively tested on
Ubuntu 18.04. However, it should work on any Linux distribution without much trouble.

In case of problem, check the
[Odoo installation guide](https://www.odoo.com/documentation/13.0/setup/install.html), as well as
the [FFmpeg](https://ffmpeg.org/download.html) documentation. Windows is not supported, while it
should be possible to make it work on OSX.

A [Docker Compose](https://docs.docker.com/compose/) image is available and provides an up and
running installation without hassle. It should work on any Docker-supported platform (including
Windows).

# Automatic installation

An installation script is provided to automatize installation, un-installation and upgrade.

### TL;DR:

In a terminal, run the following:

```
wget https://raw.githubusercontent.com/DocMarty84/koozic_install/v3/koozic_install.py -O koozic_install.py
sudo python3 koozic_install.py install
```

Access KooZic in your browser at [http://localhost:8069](http://localhost:8069). The default login
and password is `admin`. Change the password right away!

### Okay, now the details...

The installation script takes 2 optional arguments:

-   `-u`: user (default: root)
-   `-d`: install directory (default: /opt)

It is advised to use another user than root. Just make sure the user has access to the media
folders. The script will:

-   Retrieve the latest version
-   Install all the dependencies
-   Setup PostgreSQL
-   Install FFMpeg
-   Setup a systemd service

The following platforms are supported:

-   Ubuntu 18.04 (and derivatives, such as Linux Mint)
-   Debian 10
-   Fedora 31 (do not forget to check your SELinux configuration)
-   OpenSUSE 15.1

### Don't like it?

```
sudo python3 koozic_install.py uninstall
```

Note that PostgreSQL as well as the dependencies won't be removed automatically (because I don't
want to screw your system). You might also want to remove FFMpeg at `/usr/local/bin/ffmpeg`.

# Docker

1.  Install Docker Compose following the
    [official instructions](https://docs.docker.com/compose/install/)
2.  Download the "koozic-\*-docker.tar.gz" file on
    [GitHub](https://github.com/DocMarty84/koozic/releases/latest).
3.  Edit "docker-compose.yml" and replace "/music" by the music folder you want to share.
4.  Build & run:

```
docker-compose build
docker-compose up -d
```

After ~10-20 seconds, KooZic should now be accessible in your browser at
[http://localhost:8069](http://localhost:8069). To add your music in the library, go to Settings >
Folders, and create the media folder `/mnt/host`.

The usual Docker instructions can be used to start and stop the container later on:

```
docker-compose start
docker-compose stop
```
