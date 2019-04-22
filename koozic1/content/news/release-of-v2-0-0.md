+++
title = "Release of v2.0.0"
date = "2019-02-01T03:00:00+02:00"
tags = []
categories = ["release"]
type = "blog"
banner = "img/news/release-of-v2-0-0/banner.jpg"
+++

I took advantage of some free time during the last weeks to move forward on the update of KooZic to
version 2. Some user interface modifications have been brought, along with an increase of
performances and a Docker installation more flexible.

# New user interface

No more left menu, the browsing is now achieved thanks to a menu at the top of the screen. This
allows taking advantage of the whole width of the screen.

[![01](/img/news/release-of-v2-0-0/01-thumb.png#center)](/img/news/release-of-v2-0-0/01.png)

Technically speaking, Bootstrap 4 replaces the version 3. However, the menu organization remains
unchanged, with an identical structure.

[![02](/img/news/release-of-v2-0-0/02-thumb.png#center)](/img/news/release-of-v2-0-0/02.png)
[![03](/img/news/release-of-v2-0-0/03-thumb.png#center)](/img/news/release-of-v2-0-0/03.png)

Note that this represents the major part of the visible modifications. Most of the work has been
done under the hood.

# Docker

A [mysterious contributor](https://github.com/DocMarty84/koozic/pull/15) kindly proposed a
fundamental change in the way the Docker containers are handled. In v1, it was impossible to update
without resetting the container, meaning losing the configuration. Thanks to the use of
[Docker Compose](https://docs.docker.com/compose/), the database containing the configuration is now
separated from the KooZic executable. Therefore, it is possible to update the container containing
the executable while keeping the configuration.

# Other Features

Several small details have been improved to make the user interface more reactive. Moreover, the
duration analysis of the initial analysis of the library has been reduced. Note that it only apply
to a local library. Indeed, in the case of a remote library the bottleneck is usually located at the
data transfer level.

[![04](/img/news/release-of-v2-0-0/04-thumb.png#center)](/img/news/release-of-v2-0-0/04.png)

Last point, it is now possible to choose which library will be used for the tag analysis: Taglib or
Mutagen. Mutagen can be useful for specific remote mounting points, for example thanks to
[rclone](https://rclone.org/). In all other cases, Taglib should be preferred. This can be
configured at the folder level.

# Upgrade of an existing installation

A new major version means an incompatibility with the previous version. It is therefore advised to
uninstall the v1 before installing the v2.

```
wget https://raw.githubusercontent.com/DocMarty84/koozic_install/v2/koozic_install.py -O koozic_install.py
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

## Docker

A Docker installation assumes that [Docker Compose](https://docs.docker.com/compose/install/) was
installed previously. When it is done, retrieve the necessary archive:

```
wget https://github.com/DocMarty84/koozic/releases/download/v2.0.0/koozic-v2.0.0-docker.tar.gz
tar xf koozic-v2.0.0-docker.tar.gz
cd docker
```

In the file 'docker-compose.yml', replace '/music' by the directory containing your library. Then we
start everything:

```
docker-compose build
docker-compose up -d
```

After ~10 seconds, it is then possible to connect to
[http://localhost:8069/](http://localhost:8069/) with the credentials 'admin' / 'admin'. The last
step is to go to Configuration > Folders > Create and add '/mnt/host' in 'Folder Path', then click
on 'Scan'.

Do not hesitate to submit a [Github issue](https://github.com/docmarty84/koozic/issues) if
necessary!
