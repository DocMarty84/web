+++
title = "Release of v2.2.0"
date = "2019-08-16T03:00:00+02:00"
archives = "2019"
+++

Several discussions on social media led to the development of a couple of features integrated in
the new v2.2.0. But before describing them, we are proud to announce the birth of the
[official documentation](https://doc.koozic.net/)! Some parts still need to be written, but the
major parts are now documented.

# Custom Smart Playlists

Smart and dynamic playlists playlists were introduced in [v1.1.0](/2018/12/20/release-of-v1-1-0/)
with the possibility to generate automatically playlists based on several modes (e.g. random,
favorites, best rated...). The new release allows to pick tracks following custom criteria. The
latter are set in the playlist creation view. Here are 2 examples to illustrate the feature.

*Example 1*: tracks with the genre set to either 'blues', 'country' or 'americana'.

[![01](/img/post/release-of-v2-2-0/01-thumb.png#center)](/img/post/release-of-v2-2-0/01.png)

*Example 2*: tracks with genre set to either 'americana', 'blues', 'jazz', 'country', ..., and
'pop'. But in case of 'pop', the artist cannot contain some pattern such as 'gara', 'dion' or
'obispo' (translate: it plays pop songs, but not Céline Dion).

[![02](/img/post/release-of-v2-2-0/02-thumb.png#center)](/img/post/release-of-v2-2-0/02.png)

# Custom Tags

The regular ID3 tags might not be enough in the library organization. One might want to tag tracks
with specific values, e.g. 'party', 'romantic' and so on. A new field was added on tracks, albums
and artists to do so. On the following example, we added the tags 'energetic' and 'indie' to an
album:

[![03](/img/post/release-of-v2-2-0/03-thumb.png#center)](/img/post/release-of-v2-2-0/03.png)

The colored tags are also displayed in the Kanban view:

[![04](/img/post/release-of-v2-2-0/04-thumb.png#center)](/img/post/release-of-v2-2-0/04.png)

It is also possible to search and filter on these tags.

# Disable transcoding and Subsonic API format

Two settings were added to better cover specific use cases.

The first one is the use of KooZic on hardware with limited resources, e.g. a Raspberry Pi. Some
users have installed KooZic through Docker on a Raspberry Pi, and so far it works perfectly (a
classic installation should work as well). One of the main drawback of such a device is the low CPU
power, making transcoding way too slow to be usable. In such cases, one wants to completely
deactivate transcoding and serve files directly. Note that this option overrides all other
transcoding options, including the one described just below: when activated, no more transcoding is
possible!

The second setting impacts the Subsonic API format. For compatibility reasons, the default format
for Subsonic applications was MP3, unless requested differently by the app itself. However, modern
smartphones are able to play more efficient formats, such as OGG and Opus. An option was added to
select the format sent to Subsonic applications. The most common use case is the limited mobile data
quota. Indeed, Opus has a much better quality than MP3 at low bitrates, so it's possible to request
a lower bitrate without losing quality (e.g. Opus @ 96 kbps instead of MP3 @ 160 kbps). Note that
the format requested by the app itself still has the priority over this setting: if Opus is set but
the app requests MP3, MP3 is used.

[![05](/img/post/release-of-v2-2-0/05-thumb.png#center)](/img/post/release-of-v2-2-0/05.png)

Both options are only displayed in [debug mode](https://doc.koozic.net/settings/debug.html) since
they are useful only in very specific cases.

# Spanish translations

A kind contributor helped to translate the complete application in Spanish. Many thanks to him! We
also changed the translation tool to [Transifex](https://www.transifex.com/koozic/koozic/).
Contributions are highly appreciated, and if your language is not part of the proposed language, do
not hesitate to open a [Github issue](https://github.com/docmarty84/koozic/issues).

# Other Features

Following the
[deprecation by LastFM](https://getsatisfaction.com/lastfm/topics/api-announcement-dac8oefw5vrxq) of
the artist image fetching, Spotify is now used to fetch artist images. The drawback is that if an
artist is not on Spotify, the image won't be available.

As usual, multiple minor performance improvements, especially on memory usage during folder
scanning.

# Upgrade of an existing installation

The v2.2.0 is compatible with the previous v2.1.0 version. To upgrade:

```
wget https://raw.githubusercontent.com/DocMarty84/koozic_install/v2/koozic_install.py -O koozic_install.py
sudo python3 koozic_install.py upgrade
```

### Docker

1.  Stop KooZic: `docker-compose stop`
2.  Download v2.2.0 on
    [the release page](https://github.com/DocMarty84/koozic/releases/download/v2.2.0/koozic-v2.2.0-docker.tar.gz)
3.  Copy the `Dockerfile` and `entrypoint.sh` from v2.2.0 to the folder where v2.1.0 was extracted.
4.  Build: `docker-compose build` > a new version of KooZic is downloaded
5.  Run: `docker-compose up -d`

Do not hesitate to submit a [Github issue](https://github.com/docmarty84/koozic/issues) if
necessary!
