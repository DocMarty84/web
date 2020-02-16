Actions
=======

This page describes the basic actions that can be found in the Music interface.

.. glossary::

   Add And Play
      Add at the end of the :ref:`current_playlist` and start playing the first track. Hidden if
      already in the playlist.

   Add Recursively To Current Playlist
      Add all tracks found recursively in the folder to the :ref:`current_playlist`.

   Add To Current Playlist
      Add at the end of the :ref:`current_playlist`. Hidden if already in the playlist.

   Add To Playlist
      Add tracks at the end of the playlist being edited.

   Create Link
      Generate a :ref:`download_links` which allows an external person to download the content of
      the object (track, album, playlist...).

   Download
      Builds a zip file with the content of the object (track, album, artist, playlist) and starts
      downloading.

   Force Full Scan
      Force a complete analysis of the folder, meaning that all folders and files are scanned and
      updated. It should only be used if inconsistencies are found between the file tags and the
      library information.

   Play
      Play the track right away without adding it in the :ref:`current_playlist`. This is useful to
      quickly listen to a track without messing with the playlist.

   Purge
      Remove all lines from the playlist.

   Reorder
      When the handle is displayed at the left of a list, it means that the elements can be
      manually reordered.

   Run
      Start the conversion process. More precisely, flag the converter to be ready for conversion.
      The conversion automatically starts in the background within 2 minutes.

   Scan
      Analyzes the folder in order to add new tracks in the library or update the information on
      existing trakcs. It also removes the deleted tracks from the library. It only analyzes folders
      and tracks for which the modification time has changed since last scan. It means that if the
      ID3 tags of a file are updated, its modification time should also be updated.

      The database is updated every 1000 new files or every 2 minutes.

   Unlock
      A folder being analyzed is 'locked', meaning that it is protected against multiple scans at
      the same time. If the scanning process crashes at some point (hopefully it shouldn't happen),
      the folder may stay 'locked' without actual analysis running. This allows to 'unlock' the
      folder and make it available for scanning.

   Update Events
      Retrieve all the events of the artists thanks to BandsInTown.
