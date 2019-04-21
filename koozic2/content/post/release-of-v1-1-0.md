+++
title = "Release of v1.1.0"
date = "2018-12-20T03:00:00+02:00"
archives = "2018"
+++

Koozic recently blew its second candle, while the development is still ongoing. As usual, the new
version is ready quite quickly, but the corresponding news takes some time to be written. Develop
new functionalities is a fun job, but writing a decent release blog is less.

# Smart and dynamic playlists

The smart playlist concept has been in the development pipe for a while now. Nothing revolutionary
in comparison to other softs, though: KooZic creates automatically a playlist based on one of the
following supported modes:

*   Random
*   Already Played
*   Never Played
*   Most Played
*   Last Listened
*   Recent
*   Favorites
*   Best Rated
*   Worst Rated

[![01](/img/post/release-of-v1-1-0/01-thumb.png#center)](/img/post/release-of-v1-1-0/01.png)

By default, a playlist is static, meaning that a defined number of tracks is added. It is also
possible to define the playlist as dynamic. In this case, a track is automatically added while
listening to the playlist.

# Sharing the music library

Up to v1.0.0, each user had his/her own music library. From a technical point of view, that makes
things way easier: each user has his own files, tracks, albums and artists. Moreover no mixing
between collections, one won't find in his jazz collection the tracks of his younger sister.
However, if several users access the same library, it means that the same folder must be added for
each of them. If a lot of users need this access, this can cause an (performance) issue since the
database is filled with redundant data.

[![02](/img/post/release-of-v1-1-0/02-thumb.png#center)](/img/post/release-of-v1-1-0/02.png)

A new option is introduced in v1.1.0 in order to share the music collection among users. Watch out,
it's a all or nothing policy: either each user has his own collection, or all collections are
shared. The data related to the playback counting, favorites, etc. remain specific for each user.
Please note that there is no plan to make the access rights more fined-grained. This would quickly
become overkill for a limited use.

# Other Features

The playlist options have been slightly reorganized for clarity. Moreover, the integrated album
cover arts are now extracted if no 'cover', 'front' or 'folder' is available. In the folder view, it
is now possible to add tracks recursively.

Another option has been added to ignore ID3 tags on a folder. This makes the folder analysis way
faster for users who don't use them. However, this also means that only the folder view will contain
data. The tracks, albums, artists and genres views will remain empty.

Finally, the order of the transcoders is now taken into account during streaming. Up to v1.0.0, Opus
was the default format, followed by Ogg and MP3. From now on, the default format will be the one
with the highest priority. In case of doubt, do not touch anything ;-)

# Upgrade of an existing installation

The v1.1.0 is compatible with the previous v1.0.0 version. To upgrade (the URL has changed):

```
curl https://raw.githubusercontent.com/DocMarty84/koozic_install/v1/koozic_install.py > k_install.py
chmod +x k_install.py
sudo ./k_install.py upgrade
```

Do not hesitate to submit a [Github issue](https://github.com/docmarty84/koozic/issues) if
necessary!
