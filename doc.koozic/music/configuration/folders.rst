.. _folders:

Folders
=======

This is where users define the folders containing the music files.


Views
-----

A :term:`Tree`, a :term:`Form` and a :term:`Search` view.


Actions
-------

3 action buttons are available:

* :term:`Scan`
* :term:`Force Full Scan`: only accessible in :ref:`debug_mode`
* :term:`Unlock`


Fields
------

.. glossary::

   Folder Path
      Directory to analyze, browsed recursively.

   No auto-scan
      Exclude this folder from the automatized scheduled scan. Useful if the folder is not always
      accessible, e.g. linked to an external drive.

   Use ID3 Tags
      Read ID3 tags from the music tracks. Deactivate this option if the tags are not set correctly.

   File Analysis
      File analysis tool. Taglib should be the preferred option, while Mutagen is better for
      compatibility with remote mounting points, such as rclone.

   Last Scanned
      Last scanned date

   Library
      Statistics about the library

   Preview Folder Content
      A subset of the files found in the given folder.
