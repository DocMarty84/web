Advanced configuration
======================

The default configuration provided by the :ref:`auto_script` should be enough for mist use cases.
However, many tweaking options may be used to optimize the deployment of KooZic. You can find the
exhaustive list by running ``/opt/koozic/odoo-bin --help``. Any option should be added to the
``~/.odoorc`` file.

Here is a list of the most common options you might need.


Common
------

.. glossary::

    ``pidfile=PIDFILE``
        file where the server pid will be stored

    ``data_dir=DATA_DIR``
        Directory where to store Odoo data


HTTP Service
------------

.. glossary::

    ``http_interface=HTTP_INTERFACE``
        Listen interface address for HTTP services. Keep empty to listen on all interfaces (0.0.0.0)

    ``http_port=PORT``
        Listen port for the main HTTP service

    ``longpolling_port=PORT``
        Listen port for the longpolling HTTP service

    ``http_enable={True,False}``
        Disable the HTTP and Longpolling services entirely

    ``proxy_mode={True,False}``
        Activate reverse proxy WSGI wrappers (headers rewriting). Only enable this when running
        behind a trusted web proxy!


Web interface
-------------

.. glossary::

    ``db_filter=REGEXP``
        Regular expressions for filtering available databases for Web UI. The expression can use
        ``%d`` (domain) and ``%h`` (host) placeholders.


Logging
-------

.. glossary::

    ``logfile=LOGFILE``
        file where the server log will be stored

    ``log_level=LOG_LEVEL``
        specify the level of the logging. Accepted values:
        ['info', 'debug_rpc', 'warn', 'test', 'critical', 'debug_sql', 'error', 'debug',
        'debug_rpc_answer', 'notset'].


Database
--------

.. glossary::

    ``database=DB_NAME``
        specify the database name

    ``db_user=DB_USER``
        specify the database user name

    ``db_password=DB_PASSWORD``
        specify the database password

    ``pg_path=PG_PATH``
        specify the pg executable path

    ``db_host=DB_HOST``
        specify the database host

    ``db_port=DB_PORT``
        specify the database port

    ``db_sslmode=DB_SSLMODE``
        specify the database ssl connection mode (see PostgreSQL documentation)

    ``db_maxconn=DB_MAXCONN``
        specify the maximum number of physical connections to PostgreSQL


Security
--------

.. glossary::

    ``list_db={True,False}``
        Disable the ability to obtain or view the list of databases. Also disable access to the
        database manager and selector, so be sure to set a proper ``database`` parameter first


Advanced
--------

.. glossary::

    ``max_cron_threads=MAX_CRON_THREADS``
        Maximum number of threads processing concurrently cron jobs (default 2).

    ``unaccent``
        Use the unaccent function provided by the database when available.


Multiprocessing
---------------

.. glossary::

    ``workers=WORKERS``
        Specify the number of workers, 0 disable prefork mode.

    ``limit_memory_soft=LIMIT_MEMORY_SOFT``
        Maximum allowed virtual memory per worker, when reached the worker be reset after the
        current request (default 2048MiB).

    ``limit_memory_hard=LIMIT_MEMORY_HARD``
        Maximum allowed virtual memory per worker, when reached, any memory allocation will fail
        (default 2560MiB).

    ``limit_time_cpu=LIMIT_TIME_CPU``
        Maximum allowed CPU time per request (default 60).

    ``limit_time_real=LIMIT_TIME_REAL``
        Maximum allowed Real time per request (default 120).

    ``limit_time_real_cron=LIMIT_TIME_REAL_CRON``
        Maximum allowed Real time per cron job. (default: ``limit_time_real``). Set to 0 for no
        limit.

    ``limit_request=LIMIT_REQUEST``
        Maximum number of request to be processed per worker (default 8192).
