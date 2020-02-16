.. _converters:

Converters
==========

A converter is a task which converts tracks to a defined format. Many softwares provide such a
functionality (convert FLAC to MP3, MP3 to OGG...), and the KooZic converter is provided for
convenience only. It is not intended to be a real alternative to dedicated softwares. However, since
KooZic uses FFMpeg for music transcoding, a converter was a straightforward tool to include.

Creating a list of tracks to convert is very similar to the way :ref:`playlists` work. Once the
list is created, launch the conversion process and retreive the files in the directory set.


Views
-----

A :term:`Tree`, a :term:`Form` and a :term:`Search` view.


Actions
-------

2 action buttons are available:

* :term:`Run`
* :term:`Purge`

In edit mode, several fields appear. By adding an album, an artist or a playlist, all the
corresponding tracks are added to the converter.

It is also possible to interact with the lines:

* :term:`Reorder`


Fields
------


.. glossary::

   Name
      Name of the converter

   Comment
      Additional description

   Transcoder
      :ref:`transcoders` used for conversion.

   Bitrate/Quality
      In case of a Constant Bitrate Rate (CBR), bitrate of the converted files. In case of a
      Variable Bitrate Rate (VBR), quality of the converted file. The default value depends on the
      transcoder chosen.

   Progress
      Progression of the conversion.

   Destination Folder
      Folder (on the server where KooZic runs) where the converted files are created.

   Max Threads
      Maximum number of threads used during the conversion, i.e. number of tracks converted in
      parallel.

   Normalize
       Normalize tracks loudness thanks to the
       `EBU R128 <https://tech.ebu.ch/docs/r/r128.pd>`_ normalization.

   Add Album Tracks
      When selected, the associated album tracks are added to the converter.

   Add Artist Tracks
      When selected, the associated artist tracks are added to the converter.

   Add Artist Tracks
      When selected, the associated playlist tracks are added to the converter.

   Tracks
      The list of tracks currently in the converter.
