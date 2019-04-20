+++
title = "Streaming auto-hébergé : présentation de KooZic"
date = "2016-10-08T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2016"
type = "article"
+++

Dans l'article
[précédent](/nico/blog2/index.php?article24/streaming-auto-heberge-koozic-un-nouveau-venu), nous
avons fait un rapide tour d'horizon des solutions de streaming musical auto-hébergé. Il y était
mentionné l'arrivée d'un nouveau venu dans le domaine, [KooZic](http://koozic.net/). Présentons la
bête...

# Fonctionnalités & Interface

KooZic est conçu pour tirer au mieux parti des [tags ID3](https://fr.wikipedia.org/wiki/ID3) de
votre collection musicale. Au démarrage, il propose une sélection d'albums et de pistes extraits des
derniers ajouts, ainsi qu'une liste aléatoire.

[![01](/img/post/koozic-introduction/01-thumb.png#center)](/img/post/koozic-introduction/01.png)

La création de listes de lecture se fait facilement. On peut ajouter un album ou une piste à la
liste courant en cliquant sur le bouton "+" ou "Add to Current Playlist" qu'on retrouve un peu
partout dans l'interface.

[![01](/img/post/koozic-introduction/01-thumb.png#center)](/img/post/koozic-introduction/01.png)

Un outil dédié permet également de construire rapidement ses listes de lecture. En sélectionnant un
album ou un artiste, toutes les pistes associées sont ajoutées à la liste.

<center><video width="500" controls>
  <source src="/img/post/koozic-introduction/koozic_playlist_creation.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video></center>

La bibliothèque est classée par titre, album et artiste. La vue la plus intéressante est
probablement la vue par album, ainsi que ses possibilités de recherche. Filtrer ou grouper ses
albums se fait naturellement via la barre de recherche.

<center><video width="500" controls>
  <source src="/img/post/koozic-introduction/koozic_search.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video></center>

Il est possible de configurer plusieurs répertoires contenant vos musiques. Ils seront
automatiquement scannés à intervalles réguliers. L'analyse d'un répertoire se fait au rythme de 2000
titres par minute. Les formats acceptés sont le MP3, le FLAC, l'OGG et l'AAC. Le titre est encodé à
la volée grâce à FFmpeg pour être lu dans le navigateur.

Dernière chose mais non des moindres, le lecteur lui-même. Il se présente sous forme d'un panneau
situé en bas de la fenêtre, et qu'on peut faire apparaître ou disparaître grâce au bouton "note de
musique" situé en haut à droite. Les options sont classiques : play, pause, next, previous, shuffle,
repeat... C'est un lecteur HTML5, donc pas besoin de Flash pour fonctionner.

[![01](/img/post/koozic-introduction/01-thumb.png#center)](/img/post/koozic-introduction/01.png)

# Installation

À l'heure actuelle, aucun package n'existe, que ça soit en .deb ou .rpm. On récupère simplement la
dernière version disponible sur le [site officiel](http://koozic.net/download/).

Sous Ubuntu 16.04, l'installation des dépendances se fait sans souci :

```
sudo apt install adduser node-less postgresql-client python python-dateutil python-decorator\
    python-docutils python-feedparser python-imaging python-jinja2 python-ldap python-libxslt1\
    python-lxml python-mako python-mock python-openid python-passlib python-psutil python-psycopg2\
    python-pybabel python-pychart python-pydot python-pyparsing python-pypdf python-reportlab\
    python-requests python-suds python-tz python-vatnumber python-vobject python-werkzeug\
    python-xlsxwriter python-xlwt python-yaml postgresql python-mutagen ffmpeg
```

On crée l'utilisateur dans la base de données :

```
sudo su - postgres -c "createuser -s votre_utilisateur"
```

On se rend dans le répertoire où on a récupéré KooZic, et on initialise la configuration :

```
./odoo-bin -i oomusic -d koozic --without-demo=all --stop-after-init
```

Quand l'initialisation est terminée, il reste à lancer le serveur :

```
./odoo-bin
```

On y accède via [http://localhost:8069](http://localhost:8069). Le login / mot de passe est "admin".
Il faut bien évidemment changer ce mot de passe par mesure de sécurité...

# Sous le capot

Sous le capot, tout est basé sur des technologies open-source et libres.

KooZic se base [Odoo](https://www.odoo.com) (v10), un progiciel de gestion intégré (un ERP). Il est
en fait constitué d'un module (OOMusic) qui est greffé à une version allégée d'Odoo. Seul le
framework Python et web a été conservé, tous les modules métiers (vente, achat, etc.) ont été
enlevés.

Le base de données utilisée est [PostgreSQL](https://www.postgresql.org/). Elle peut gérer sans
problèmes une collection musicale de taille importante.

Finalement, [howler.js](https://howlerjs.com/) est le framework Javascript qui permet de
s'interfacer facilement avec les capacités de lecture de son des navigateurs en HTML5.

# L'avenir...

KooZic est une application qui peut se suffire à elle-même. Cependant, un premier volet
d'amélioration sera d'intégrer les infos d'un service extérieur pour récupérer, par exemple, les
informations d'un artiste ou ses titres les plus populaires. Cela devrait rendre l'interface un peu
plus riche. Un second volet sera le support de l'API de Subsonic, pour profiter des différentes
applications (notamment mobiles) existantes. Mais bon, on en n'est pas encore là...
