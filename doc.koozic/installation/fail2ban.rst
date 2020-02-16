.. _fail2ban:

Fail2ban integration
====================

Fail2ban is useful to prevent brute-force attacks. Its purpose is to ban an IP address which
attempted too login incorrectly too many times. It is often used for SSH connections, but it can
also be used in KooZic.

This tutorial assumes that you already set KooZic running behind :ref:`nginx`, as a `systemd`
service (which should be the case if you installed it thanks to the :ref:`auto_script`).


Enable proxy mode
-----------------

The first step is to make sure that the ``proxy_mode`` option is turned on in KooZic, which is not
the case by default. To do so, edit the file ``~/.odoorc`` and add the line:
::

   proxy_mode = True

Note that ``~/`` refers to the home directory of the user running KooZic (``root`` by default).

Then, restart the service:
::

    service koozic@<USER> restart


Add the jail
------------

Configurations files are provided on
`Github <https://github.com/DocMarty84/koozic/tree/v3/extra/fail2ban>`_. To add configuration:

* Copy the filter ``filter.local`` to ``/etc/fail2ban/filter.d/koozic-login.local``
* Copy the jail ``jail.local`` to ``/etc/fail2ban/jail.d/koozic-login.local``.

Restart the fail2ban service.
