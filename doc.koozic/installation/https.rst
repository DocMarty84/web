.. _https:


HTTPS
=====

Once KooZic is up and running, it is always a good idea to set up an HTTPS endpoint to prevent
passwords to be sent in clear on the network. KooZic doesn't directly provide an embedded option for
this, but it supports the most common reverse-proxy servers. The rationale behind this is that
implementing the security required for HTTPS should not be taken lightly. Therefore, we prefer
relying on battle-tested softwares when it comes to such matters.


Certificate with Let's Encrypt
------------------------------

Here is the procedure to generate a Let's Encrypt SSL certificate


Certificate generation
^^^^^^^^^^^^^^^^^^^^^^

Get the code:
::

   git clone https://github.com/certbot/certbot

Generate the certificates:
::

   cd certbot
   ./certbot-auto certonly -d <your_domain> --rsa-key-size 4096

The certificates sould be created in ``/etc/letsencrypt/live/<your_domain>``.


Auto renewal of certificate
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a ``cron`` job (once a day) for the ``root`` user with the following command:
::

   </path/to/certbot-auto> renew --no-self-upgrade ; service {apache,nginx} restart


.. _nginx:

NGINX
-----

The preferred web server is NGINX. It should be available in the package manager of all major
distributions. For example on Ubuntu:
::

   sudo apt install nginx

For an additional security level, generate the
`Diffie-Hellman parameter <https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange>`_
(this takes time...):
::

   openssl dhparam -out dh4096.pem 4096
   sudo mv dh4096.pem /etc/nginx/

A configuration file is provided in order to activate the SSL encryption on
`Github <https://github.com/DocMarty84/koozic/tree/v3/extra/nginx>`_.

Copy the file ``nginx_ssl_config`` to ``/etc/nginx/sites-available/default``. Change:

* ``<your_domain>`` to your own domain name.
* ``ssl_certificate`` and ``ssl_certificate_key`` to the Let's Encrypt configuration (make sure to
  use ``fullchain.pem`` and not ``cert.pem``):

::

   ssl_certificate     /etc/letsencrypt/live/<your_domain>/fullchain.pem;
   ssl_certificate_key /etc/letsencrypt/live/<your_domain>/privkey.pem;

Restart the service:
::

   service nginx restart

KooZic should now be available at ``https://<your_domain>``.

The next step is to perform the :ref:`fail2ban` in order to prevent brute-force attacks.
