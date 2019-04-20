+++
title = "KooZic : sortie de la v0.6.0"
date = "2017-05-24T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2017"
type = "article"
+++

Après une v0.5.0 assez limitée en changements, KooZic sort en v0.6.0 avec une nouveauté qui déchire
le slip et qui fait déjà trembler Youtube : le support des vidéos !

Bon, peut-être pas encore faire trembler Youtube, mais quand même ;-P A l'instar de Subsonic, KooZic
supporte à présent le streaming vidéo, c'est-à-dire que les vidéos stockées sur le serveur peuvent
être converties à la volée et diffusée où que vous soyez.

# Streaming vidéo

Contrairement à Subsonic, les vidéos sont traitées de façon indépendante de la collection musicale.
Cela se présente sous la forme d'un module Odoo ([OOVideo](https://github.com/DocMarty84/oovideo)),
avec à l'heure actuelle la possibilité de naviguer par dossier. Cela ressemble à la navigation par
dossier de la partie musicale.

[![01](/img/post/release-of-v0-6-0/01-thumb.png#center)](/img/post/release-of-v0-6-0/01.png)

Au niveau du lecteur, on utilise [Clappr](http://clappr.io/), avec une extension pour gérer les
sous-titres ([Clappr-Subtitle](https://github.com/JMVTechnology/Clappr-Subtitle)). Ce lecteur
utilise le support HTML5 du navigateur, donc pas de Flash. L'interface (moche) permet de choisir la
résolution, le bitrate, la piste audio et les sous-titres chargés (support SRT uniquement).

[![02](/img/post/release-of-v0-6-0/02-thumb.png#center)](/img/post/release-of-v0-6-0/02.png)

Pour le moment, chaque changement implique de recharger la vidéo. C'est pas super sexy ni pratique,
mais ça fait le job et ça permet d'adapter la qualité au débit de la connexion ainsi qu'aux
capacités du serveur. Comme pour la partie musicale, c'est FFMpeg qui se charge de l'encodage en
temps réel. L'option "Raw" permet de charger une vidéo sans l'encoder. Cela ne fonctionne évidemment
que pour les formats supportés tels quels par le navigateur.

À terme, ces options pourraient être intégrées comme des extensions de Clappr (l'utilisation du
conditionnel est très important ici).

# Autres nouveautés

En marge du support vidéo, la v0.6.0 supporte la toute dernière version de
[l'API de Subsonic](http://www.subsonic.org/pages/api.jsp). C'est la v1.15.0 de l'API, correspondant
à Subsonic 6.1. Comme à chaque fois, Odoo est mis à jour, ce qui inclut des corrections mineures et
des correction de failles de sécurité.

# Mise-à-jour d'une installation existante

La nouvelle version est disponible sur le [site du projet](https://koozic.net). Pas de crainte à
avoir, les sources précédentes peuvent être supprimées. On extrait la nouvelle version, et on lance
la mise-à-jour à partir du répertoire:

```
./odoo-bin -u oomusic -d koozic --stop-after-init
```

On peut relancer ensuite avec la commande habituelle.

Pour le support vidéo, il faut tout d'abord installer **mediainfo**. Sous Ubuntu :

```
sudo apt install mediainfo
```

Ensuite, dans l'interface et en tant qu'administrateur, passer tout d'abord en mode debug : changer
l'URL de

http://localhost:8069/web

vers :

http://localhost:8069/web?debug

Dans "Apps", cliquez sur "Update Apps List" et validez. Recliquez sur le sous-menu "Apps" : vous y
trouvez OOVideo.
