+++
title = "KooZic : sortie de la v0.2.0"
date = "2016-11-05T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2016"
type = "article"
+++

Il y a près d'un mois sortait
[la v0.1 de KooZic](/nico/blog2/index.php?article25/streaming-auto-heberge-presentation-de-koozic).
Le développement a avancé, et aujourd'hui sort la v0.2.0. Jetons un œil sur les nouveautés.

# Nouveautés

L'ajout majeur de cette version 0.2.0 est le support des informations publiées sur
[LastFM](http://www.last.fm/). À l'heure actuelle, le support est limité aux artistes. Pour chaque
artiste, KooZic va rechercher sa biographie, ses titres les plus connus mais également les artistes
similaires. Ceux qui sont retrouvés dans la collection musicale sont affichés dans les onglets "Top
Tracks" et "Similar Artists".

[![01](/img/post/release-of-v0-2-0/01-thumb.png#center)](/img/post/release-of-v0-2-0/01.png)
[![02](/img/post/release-of-v0-2-0/02-thumb.png#center)](/img/post/release-of-v0-2-0/02.png)

Pour rendre plus agréable l'utilisation de KooZic lorsque les tags ID3 ne sont pas définis
correctement, un nouveau mode de navigation par répertoire a été intégré. Il permet de naviguer par
répertoire, et de visualiser le nombre de titres présents dans chacun d'eux. Cela se rapproche du
fonctionnement de beaucoup de logiciels de ce type, mais ça on en a déjà parlé ;-)

[![03](/img/post/release-of-v0-2-0/03-thumb.png#center)](/img/post/release-of-v0-2-0/03.png)

Dans les améliorations mineures, on trouve la possibilité de noter les artistes, albums ou titres
(de 0 à 5), ainsi que l'extension du tag "favori" aux artistes. On peut également forcer le scan
complet d'un répertoire. Par la même occasion, on note quelques bugs mineurs et améliorations des
performances.

# Mise-à-jour d'une installation existante

La nouvelle version est disponible sur le [site du projet](https://koozic.net). Pas de crainte à
avoir, les sources précédentes peuvent être supprimées. On extrait la nouvelle version, et on lance
la mise-à-jour à partir du répertoire:

```
./odoo-bin -u oomusic -d koozic --stop-after-init
```

On peut relancer ensuite avec la commande habituelle.

Un billet suivra prochainement pour décrire la logique suivie pour la numérotation des versions et
la méthode de mise-à-jour.

# À venir

L'étape suivante consiste à supporter l'API de Subsonic. Grâce à ça, les applications mobiles
l'utilisant seront aussi capables de se connecter au serveur KooZic. Spoiler : en fait, c'est déjà
presque fini et ça fonctionne, mais pas testé suffisamment en profondeur pour l'instant ;-)
