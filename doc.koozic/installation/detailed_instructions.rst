.. _detailed_instructions:

Detailed instructions
=====================

The installer mentioned in the :ref:`quickstart` instructions only supports a limited number of
distributions. In case your distributions is not supported, please refer to the following generic
instructions to install on your system.


Step 0: create a specific user
------------------------------

It is usually advised, for security reason, to always launch a service accessible from the outside
world with a user different from ``root``. Therefore, you should create for example the ``koozic``
user, with the appropriate access rights to your music files.


Step 1: install prerequisites
-----------------------------

First step of installation is to get all the package and pip dependencies. As a references, here are
the packages for:

- DEB-based distributions: `apt packages <https://github.com/DocMarty84/koozic_install/blob/fdc1649538d75675cfebe4cf4f6ab6fb88eea62c/koozic_install.py#L268-L309>`_, `pip packages <https://github.com/DocMarty84/koozic_install/blob/fdc1649538d75675cfebe4cf4f6ab6fb88eea62c/koozic_install.py#L312-L315>`_
- RPM-based distributions: `dnf packages <https://github.com/DocMarty84/koozic_install/blob/fdc1649538d75675cfebe4cf4f6ab6fb88eea62c/koozic_install.py#L327-L381>`_, `extra pip packages <https://github.com/DocMarty84/koozic_install/blob/fdc1649538d75675cfebe4cf4f6ab6fb88eea62c/koozic_install.py#L384-L387>`_

Depending on what is available for your distribution, some dependencies might need to be installed
with ``pip`` instead of your package manager. The complete list is given in the
`requirements <https://github.com/DocMarty84/koozic/blob/v3/requirements.txt>`_.

You will also need a recent version of FFmpeg (>= 3.4).

**Important note**: ``Pillow==5.4.1`` requires ``zlib1g-dev`` and ``libjpeg-dev``.


Step 2: set-up PostgreSQL
-------------------------

Second step is to set-up PostgreSQL. Assuming you will run KooZic with the user named `koozic`, you
need to create the corresponding PostgreSQL user:

::

   su - postgres -c "createuser -s koozic"


Step 3: Download
----------------

Third step is to download the `latest version of KooZic <https://github.com/DocMarty84/koozic/releases/latest>`_
(get the file ``koozic-*.tar.gz``), uncompress the archive.

Step 4: launch KooZic
---------------------

Fourth step is to execute this as the ``koozic`` user:

::

   ./odoo-bin --workers=4 -d koozic-v3 --limit-time-cpu=1800 --limit-time-real=3600 --without-demo=all --no-database-list


on Fedora, you need to add ``--db-template=template0`` to the command line. This might be necessary
for other distributions as well.

After 10-20 seconds (the very first execution takes some time since it needs to create all database-
related stuff), you should be able to connect to http://localhost:8069 with the email / password
``admin``.
