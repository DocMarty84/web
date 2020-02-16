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

   Tracks
      The list of tracks currently in the playlist

   Download Links
      The :ref:`download_links` of the playlist.
