.. _playlists:

Playlists
=========

KooZic has extended playlist creation capabilities. It is possible to create playlist manually by
adding tracks, albums or artists, but dynamic playlists are also available.


Views
-----

A :term:`Tree`, a :term:`Form` and a :term:`Search` view.


Actions
-------

3 action buttons are available:

* :term:`Purge`
* :term:`Download`
* :term:`Create Link`
* :term:`Add To Playlist` (only if dynamic playlist)

In edit mode, several fields appear. By adding an album or an artist, all the corresponding tracks
are added to the playlist. A dynamic playlist is automatically populated when switching tracks.
Therefore, in this case, it is usually not necessary to add more than a few tracks before starting
playing it.

Finally, it is also possible to interact with the playlist lines:

* :term:`Reorder`
* :term:`Play`


Fields
------


.. glossary::

   Name
      Name of the playlist

   Comment
      Additional description

   Audio Mode
      * Standard: regular transcoding of the files.
      * No Transcoding: do not transcode audio files. It decreases the server load, at the cost of a
        higher network usage.
      * Normalize: normalize playlist loudness thanks to the
        `EBU R128 <https://tech.ebu.ch/docs/r/r128.pd>`_ normalization. Transcoding will be
        significantly slower when activated, implying larger gaps between songs.

   Audio API
      API used for audio playback.

      * HTML5 Audio: no need to download the full file before starting the playback.
      * Web Audio API: need to download the full file before starting the playback. More reliable
        than HTML5, but longer gaps between tracks.

   Dynamic
      If activated, tracks will be automatically added based on the Smart Playlist.

   Maximum Tracks
      If set (value different from zero), the oldest track of a dynamic playlist is removed when a
      new track is added. This allows creating 'infinite' playlists.

   Current
      Current playlist being played.

   Add Album Tracks
      When selected, the associated album tracks are added to the playlist.

   Add Artist Tracks
      When selected, the associated artist tracks are added to the playlist.

   Smart Playlist
      How tracks are chosen to be automatically added to the playlist. Possible values are:
      Random Tracks, Already Played, Never Played, Most Played, Last Listened, Recent, Favorites,
      Best Rated, Worst Rated and Custom.

   Custom Domain
      When the smart playlist option is set to 'Custom', a domain editor is available. The tracks
      of the dynamic playlist will be chosen based on the conditions defined in this domain.

      *Example 1*: tracks with the genre set to either 'blues', 'country' or 'americana'

      .. image:: /images/custom_domain_1.png

      *Example 2*: tracks with genre set to either 'americana', 'blues', 'jazz', 'country', ..., and
      'pop'. But in case of 'pop', the artist cannot contain some pattern such as 'gara', 'dion' or
      'obispo' (translate: it plays pop songs, but not Céline Dion)

      .. image:: /images/custom_domain_2.png

   Custom Order
      When the smart playlist option is set to 'Custom', it is possible to set one or more sorting
      fields. When the order is not set, the tracks matching the domain are selected randomly in
      order to be added to the playlist. When the order is set, the tracks matching the domain are
      first sorted following the order, then the first track is added to the playlist.

      The combination of sorting fields is possible, as well as the descending order thanks to the
      ``desc`` keyword.

      It is possible to sort by any field available on the tracks, but the most relevant are:

      +------------------+------------------+
      |Field Name        |Field Label       |
      +==================+==================+
      |create_date       |Create Date       |
      +------------------+------------------+
      |duration          |Duration          |
      +------------------+------------------+
      |last_play         |Last Played       |
      +------------------+------------------+
      |last_skip         |Last Skipped      |
      +------------------+------------------+
      |play_count        |Play Count        |
      +------------------+------------------+
      |play_skip_ratio   |Play/Skip Ratio   |
      +------------------+------------------+
      |rating            |Rating            |
      +------------------+------------------+
      |skip_count        |Skip Count        |
      +------------------+------------------+
      |star              |Favorite          |
      +------------------+------------------+
      |track_number      |Track #           |
      +------------------+------------------+

      *Example 1*: sort by duration, meaning that we select the shortest tracks first: ``duration``

      *Example 2*: sort by descending Play/Skip Ratio, meaning that we select the most played tracks
      first: ``play_skip_ratio desc``

      *Example 3*: sort by descending rating and ascending play count, meaning that we select the
      highest rated tracks first, but in case of identical rating we select the least played tracks:
      ``rating desc, play_count``

   Tracks
      The list of tracks currently in the playlist

   Download Links
      The :ref:`download_links` of the playlist.
