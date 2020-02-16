Settings
========

A handful of settings are provided regarding folder sharing and performances.

.. glossary::

   Folder Sharing
      When active, the content of the :ref:`folders` are shared among all :ref:`Users`. When
      inactive, each user has his own library. It's a all-or-nothing configuration: either all
      folders are shared, or none of them. There is no possibility to choose which folders are
      shared and which aren't.

      It is advised to active the setting when all :ref:`Users` access the same music library to
      avoid duplicated information in the database.

      User-specific data such as favorites, ratings or followed artists remains user-specific
      whatever the configuration.

      *Default: Inactive (user specific)*

   Scheduled Actions
      Several processes are run in the background, called :ref:`crons`. Their purpose is to update
      the data without any user intervention. 4 actions can be deactivated thanks to this option:

      * Folder scanning: scan the folders for new content (every 3 hours)
      * Artists image cache: resize the artist images to speed up the view loading
      * Albums image cache: resize the album images to speed up the view loading
      * Events cache: fetch the events of the followed artists
      * LastFM cache: prefetch the artist information on LastFM to speed up the artist view loading

      Deactivate this option if you have limited resources.

      *Default: Active*

   Default Views
      The albums and artists are available as a :term:`Kanban` or :term:`Tree` views. The Kanban
      view is a bit nicer but also slower to load (because of the thumbnails). This options allows
      you to choose which is the default view used when accessing albums or artists.

      *Default: Kanban, with thumbnails*

   Artists and Events Info
      If the artists and events information has not been fetched yet or outdated (112 days for
      LastFM, 182 days for Spotify and 14 days for events) it is automatically fetched. When
      deactivated, the user must update the information manually. It can be done 'Update Artist
      Info' and 'Update Events Info' in the 'Action' menu.

      *Default: Fetched automatically*

   Disable Transcoding
      In case of a system with limited resources (e.g. Raspberry Pi), transcoding shows poor
      performances. Therefore, it might be useful to completely deactivate the transcoding feature
      in the whole application.

      When activated, the transcoding is deactivated whatever the configuration of the playlist or
      the third-party Subsonic app. It means that it overrides the :term:`Audio Mode` as well as the
      :term:`Subsonic API Format` options.

      Only in :ref:`debug_mode`.

      *Default: False*

   Subsonic API Format
      A regular Subsonic server converts the tracks to the MP3 format only. However, most modern
      mobile applications can handle other formats such as Ogg or Opus. The setting gives the
      possibility to choose the format used when connecting through the Subsonic API.

      Note that it is strongly recommended to keep the default value. Changing it might lead to
      unexpected behaviors of your mobile application.

      Only in :ref:`debug_mode`.

      *Default: mp3*
