.. _transcoders:

Transcoders
===========

Transcoders are used to convert the tracks to the given format, thanks to FFMpeg.

The order has an importance: the transcoder on top of the list has the highest priority. The first
format compatible with the browser will be selected. Opus is the default choice, and there is little
reason to change the order. Opus is compatible with all modern browsers, and has a very good
quality over size ratio.

However, it is possible to select another transcoder with the top priority, e.g. MP3. In this case,
MP3 will be preferred by the browser.

When accessing KooZic through a `mobile application <https://koozic.net/download/>`_  using the
Subsonic API, the default format is MP3. This can be changed in the settings (see
:term:`Subsonic API Format`).


Views
-----

A :term:`Tree`, a :term:`Form` and a :term:`Search` view.


Actions
-------

* :term:`Reorder`


Fields
------

.. glossary::

   Transcoder Name
      The name, including the output format.

   Command Line
      The FFMpeg command line executed for conversion. Specific characters are replaced:

      - ``%i``: input file
      - ``%s``: start from this seek time
      - ``%b``: birate for output file
      - ``%n``: extra parameter for normaliation

   Bitrate/Quality
      Default bitrate or quality (for VBR).

   Buffer Size (KB)
      Size of the buffer used while streaming. A larger value can reduce the potential file download
      errors when playing, but will increase the waiting delay when switching songs.

      *Default: 200*

   Blacklisted Formats
      Input formats which cannot be converted using the transcoder.

   Output Format
      It must be consistent with the format specified in the Command Line.
