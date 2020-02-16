.. _albums:

Albums
======

It lists all your albums.


Views
-----

A :term:`Kanban`, a :term:`Tree`, a :term:`Form`, a :term:`Search`, a :term:`Graph` and a
:term:`Pivot` view.


Actions
-------

In the kanban and tree views, 2 actions:

* :term:`Add To Playlist`
* :term:`Add And Play`

In the form view, 4 action buttons:

* :term:`Add To Playlist`
* :term:`Add And Play`
* :term:`Download`
* :term:`Create Link`

An album can be set as favorite and be given a rating. The latters can be used when filtering or
creating dynamic :ref:`playlists`. Custom tags can be defined, and individual tracks have 2 actions:

* :term:`Add To Playlist`
* :term:`Play`


Fields
------

.. glossary::

   Name
      Title of the album. Based on the ID3 tag of the first track.

   Favorite
      Set the album as favorite by starring it.

   Image
      Retrieved by looking for files named 'folder', 'cover' or 'front'. If none of these are found,
      extract the embedded cover of the first track if present. Images are refreshed every couple
      of days.

   Year
   Artist
   Genre
      Based on the ID3 tag of the first track.

   Rating
      The rating of the album, from 0 to 5.

   Custom Tags
      These can be used to add information not given in the regular ID3 tags.

   Tracks
      Tracks of the album

   Download Links
      The :ref:`download_links` of the album.
