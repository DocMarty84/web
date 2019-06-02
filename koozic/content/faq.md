+++
title = "FAQ"
+++

### How can I contribute?

Any bug or request can be filed on [GitHub](https://github.com/DocMarty84/koozic). We also need
translators for the [OOMusic project](https://poeditor.com/join/project/RMl91o65Bs) (the Odoo module
behind KooZic)!

### One of my folder appears in red color, what does that mean?

It means that the folder is being scanned, and is currently locked. Depending on the size of your
collection, it might take a few seconds to... a lot of time. Usually, KooZic is able to scan 2000
songs per minute during the first scan, then it should not take more than a few seconds for each
scan. Moreover, once a day, a cache of the album images is built for performance reasons. This might
take a few minutes as well. If the folder is locked for an unusually long delay:

-   shutdown KooZic and launch it with the option `--log-level=debug`: this will give you more
    detailed logs
-   Click on the 'Unlock' button to force the unlocking of the folder.

### Changes in my collection are not reflected in KooZic, why?

There might be several reasons:

-   the scheduled scan hasn't run yet -> you can run it manually by clicking 'Scan' in the folder
    view
-   the scheduled scan crashes -> see 'One of my folder appears in a red...' question
-   Folder or file modification date is not updated -> make sure it is

Regarding the last cause, it is for example the case with EasyTag: by default, changing the tags of
a file won't change the modification date of the folder, thus the folder will be skipped. Go have a
look in the parameters ;-)

### How to enable SSL support (HTTPS)?

There is no built-in SSL support. However, KooZic works perfectly behind any web server software,
such as Apache or Nginx. [Here](https://github.com/DocMarty84/koozic/tree/v2/extra/nginx) is an
example of SSL configuration with Nginx.

### Is there pre-packaged version?

Not for now. However, the installation script supports the major Linux distributions. Moreover, a
Docker version is available for support on Windows and MacOS.
