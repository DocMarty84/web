.. _crons:

Scheduled Actions
=================

This menu is accessible in :ref:`debug_mode` under Settings > Technical > Scheduled Actions.

The purpose of the scheduled actions is to perform tasks in the background. Such tasks consist of
updating images or retrieving data from external sources. This is to ensure a smooth user experience
while the data is up-to-date.

The default parameters should be appropriate for all configurations, so make sure you know what you
are doing before changing anything.

Actions
-------

.. glossary::

   oomusic.build.artists.image.cache
      Retrieves the image of artists from Spotify. A batch of 500 artists is chosen randomly and
      updated.

      Execute Every: 1 month

   oomusic.build.bandsintown.cache
      Update the BandsInTown information of the followed artists. A batch of 200 artists is chosen
      randomly for update.

      Execute Every: 1 day

   oomusic.build.image.cache
      Update the image of folders and albums. A batch of 500 folders is chosen randomly and updated.

      Execute Every: 1 day

   oomusic.build.lastfm.cache
      Update the LastFM artist information, e.g. the artist biography. A batch of 200 artists is
      chosen randomly for update.
      The cached requests are considered valid for 16 weeks. Therefore, even if the action runs
      every day, the data is updated once every 16 weeks.

      Execute Every: 1 day

   oomusic.build.spotify.cache
      Update the Spotify artist information, e.g. the artist image URL. A batch of 200 artists is
      chosen randomly for update.
      The cached requests are considered valid for 26 weeks. Therefore, even if the action runs
      every day, the data is updated once every 26 weeks.

      Execute Every: 1 day

   oomusic.convert
      Check if there is any track to convert from the :ref:`converters`.

      Execute Every: 2 minutes

   oomusic.scan.folder
      Scan the :ref:`folders` for any new file.

      Execute Every: 3 hours

   oomusic.unlock.folder
      In case the folder scanning was interrupted before the end (e.g. if KooZic was stopped), some
      folders might be flagged as being scanned while they aren't anymore. This cleans up such
      situation.

      Execute Every: 10 minutes
