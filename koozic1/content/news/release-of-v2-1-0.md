+++
title = "Release of v2.1.0"
date = "2019-04-05T03:00:00+02:00"
tags = []
categories = ["release"]
type = "blog"
banner = "img/news/release-of-v2-1-0/banner.jpg"
+++

After a major UI refactoring in v2.0.0, KooZic is getting social and can now display upcoming
events. Moreover, it is the first version to integrate LDAP authentication.

# Upcoming events

The major feature of this release is the addition of a social part to KooZic through the artists'
events. It is now possible to update the artist's events from its form view, in the 'Events' tab.
Moreover, each user can follow his preferred artists thanks to the 'Follow' switch, on the top
right.

[![01](/img/news/release-of-v2-1-0/01-thumb.png#center)](/img/news/release-of-v2-1-0/01.png)

The events linked to a followed artist are aggregated in the top menu 'Events'. By default they are
grouped by month, which allows a quick overview.

[![02](/img/news/release-of-v2-1-0/02-thumb.png#center)](/img/news/release-of-v2-1-0/02.png)

Finally, it is also possible to define a maximum distance to display an event in the list. Each user
can modify his settings (from the top right menu) and choose his location as well as the maximum
distance allowed.

[![03](/img/news/release-of-v2-1-0/03-thumb.png#center)](/img/news/release-of-v2-1-0/03.png)

# UI Enhancement

One of the major UI issue of KooZic is the number of clicks required to play a track. It first has
to be added to a playlist, then play. It might be annoying, but up to now I hadn't found a good
technical solution. It is now the case, therefore 'Add And Play' buttons have been added in many
places.

[![04](/img/news/release-of-v2-1-0/04-thumb.png#center)](/img/news/release-of-v2-1-0/04.png)

Such a button adds the tracks to the current playlist and starts playing.

# LDAP authentication integration

It is not possible to integrate the KooZic users with a LDAP registry. To do so, it is necessary to
install the appropriate module thanks to the 'Apps' menu: 'Authentication via LDAP'

[![05](/img/news/release-of-v2-1-0/05-thumb.png#center)](/img/news/release-of-v2-1-0/05.png)

Then, you need to configure the server in the 'Settings', 'Users & Companies > LDAP Servers' menu. A
configuration example is shown with a test server.

[![06](/img/news/release-of-v2-1-0/06-thumb.png#center)](/img/news/release-of-v2-1-0/06.png)

# Other Features

The video player [Clappr](http://clappr.io/) has been updated, with a new subtitles management
(support of SRT and WEBVTT files).

# Upgrade of an existing installation

The v2.1.0 is compatible with the previous v2.0.0 version. To upgrade:

```
curl https://raw.githubusercontent.com/DocMarty84/koozic_install/v2/koozic_install.py > k_install.py
chmod +x k_install.py
sudo ./k_install.py upgrade
```

Notes:

*   A new Python library is required:
```
sudo pip3 install webvtt-py==0.4.2
```

*   To install the new LDAP module, you first need to reload the plugin list manually. Go to
[http://localhost:8069/web?debug](http://localhost:8069/web?debug), then 'Apps' and 'Update Apps List'

Do not hesitate to submit a [Github issue](https://github.com/docmarty84/koozic/issues) if
necessary!
