KooZic's documentation
======================

Welcome to `KooZic <https://koozic.net/>`_'s documentation, the official documentation for the self-
hosted media server based on Odoo!

About
-----

KooZic is an alternative to applications such as Subsonic or Ampache. It gives you the possibility
to access your music and video collection on any device, for free. It offers:

* a clean and well-structured interface
* a real-time conversion of all music and video formats so it can be played in any web browser
* the full support of ID3 tags, and the possibility to add custom tags
* dynamic smart playlists (random, favorites, never played and even custom based on your criteria)
* the Subsonic API compatibility to use with apps such as DSub or Ultrasonic
* online content retrieval such as artist biography or upcoming events
* and much more...

Actually, not really much more. KooZic's philosophy is to keep things clean and useful. It's not
bloated with fancy but often useless features. The configuration is also voluntarily limited (or
'opinionated' as some software developers like to name it).

As always, the best starting point is to test it. Just give a try to our
`test server <http://demo.koozic.net:8069/public>`_ to see if it could fit your needs.

Getting started
---------------

You might want to start with the :ref:`quickstart` installation tutorial to get your media server up
and running within a few minutes. The configuration of your media folders should be straightforward
since the first steps are guided in the interface.

In case you would need a more specific setup, the :ref:`detailed_instructions` will guide you
through the various steps of the manual process.

If things are still unclear, feel free to browse the documentation!

.. toctree::
   :maxdepth: 2
   :caption: Installation

   installation/quickstart
   installation/detailed_instructions
   installation/https
   installation/fail2ban
   installation/advanced_configuration

.. toctree::
   :maxdepth: 2
   :caption: Music

   music/suggestions
   music/playlists/index
   music/library/index
   music/events
   music/configuration/index
   music/views
   music/actions

.. toctree::
   :maxdepth: 2
   :caption: Global Configuration

   settings/user_preferences
   settings/users
   settings/debug
   settings/crons
