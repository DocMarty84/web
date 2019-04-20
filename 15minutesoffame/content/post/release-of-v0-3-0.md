+++
title = "KooZic : sortie de la v0.3.0"
date = "2017-01-13T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2017"
type = "article"
+++

Dans le [dernier billet](/nico/blog2/index.php?article26/koozic-sortie-de-la-v0-2-0) sur KooZic,
j'annonçais un support de l'API de Subsonic. Voilà qui est fait pour la v0.3.0.

# Support de l'API Subsonic

Cette version 0.3.0 apporte en priorité le support de l'API de Subsonic. En pratique, cela signifie
que toutes les applications compatibles avec un serveur Subsonic, comme les applications mobiles,
sont désormais compatibles avec KooZic. La compatibilité a été poussée au maximum, dans les limites
de ce qui est supporté par KooZic. Par exemple, pas de gestion des podcasts ou des partages, vu que
ce n'est pas implémenté dans KooZic. Mais pas de frais de licence non plus ;-) Le support de l'API
est totalement libre et gratuit.

#### Supporté

*   Streaming audio
*   Parcours de la bibliothèque avec ou sans tags ID3
*   Listes prédéfinies, comme les derniers albums ou titres ajoutés, les plus joués, etc.
*   Liste des albums par genre
*   Récupération et suppression de playlists
*   Infos des artistes et albums

#### Partiellement supporté

*   Modification de playlists (dû à une contrainte technique)

#### Non supporté

*   Podcasts
*   Partages
*   Chat
*   Gestion d'utilisateurs (voulu pour une question de sécurité)
*   Streaming vidéo

Seul le streaming vidéo sera probablement implémenté dans un avenir plus ou moins proche. Le reste
des fonctionnalités me parait un peu inutile en 2017...

## Applications mobiles compatibles

Voilà une liste exhaustive des apps testées et de leur compatibilité avec KooZic.

#### Android

Trois apps ont été testées parmi les plus populaires. Leur compatibilité avec KooZic est excellente,
quelque soit le choix.

*   [DSub](https://f-droid.org/repository/browse/?fdid=github.daneren2005.dsub) : le meilleur choix,
    encore activement développé. De nombreuses fonctionnalités qui en font une référence.
*   [UltraSonic](https://play.google.com/store/apps/details?id=org.moire.ultrasonic) : un très bon
    choix également, un peu moins fourni en fonctionnalités "fancy" que DSub, mais agréable au
    quotidien.
*   [Subsonic Music Streamer](https://play.google.com/store/apps/details?id=net.sourceforge.subsonic.androidapp) :
    le client officiel. Basique, on sent que c'est plus un "proof-of-concept" qu'une application
    encore maintenue.

#### iOS

Mon accès à des appareils Apple étant limité (et les apps étant presque toutes payantes), les tests ont été plus limités.

*   [play:Sub](https://itunes.apple.com/us/app/play-sub-subsonic-music-streamer/id955329386?mt=8) :
    le meilleur choix, encore activement développé. Une vraie référence pour les appareils iOS, et
    subjectivement un cran au-dessus de DSub, tous OS confondus.
*   [AVSub](https://itunes.apple.com/us/app/avsub/id923424694?mt=8) : bof bof... L'interface est
    assez moche, en tous cas pas du tout en ligne avec le design iOS. Globalement, pas mal de petits
    soucis dans l'interface, peut-être dû à des spécificités que je n'aurais pas implémentées.
*   [Soundwaves](https://itunes.apple.com/app/soundwaves/id736139596?mt=8) : une des seules apps
    gratuite. Les fonctionnalités sont limitées mais l'essentiel, à savoir le streaming musical, est
    bel et bien là. Une bonne alternative à play:Sub.

Il est possible de tester ces applications avec le serveur de démonstration. Voici les infos pour
s'y connecter :

*   URL : http://demo.koozic.net:8069
*   login : demo
*   password : demo

# Autres nouveautés

Un nouveau menu permet d'accéder au classement par genre musical plus facilement. Pour un genre
musical, on trouve les artistes et les albums qui y sont associés.

[![01](/img/post/release-of-v0-3-0/01-thumb.png#center)](/img/post/release-of-v0-3-0/01.png)
[![02](/img/post/release-of-v0-3-0/02-thumb.png#center)](/img/post/release-of-v0-3-0/02.png)

Le reste des nouveautés est plutôt invisible pour l'utilisateur. Des améliorations ont été apportées
au niveau des performances, et quelques détails visuels ont été appliquées. Certaines parties ont
été réécrites pour être plus facilement maintenables dans le futur, comme la récupération des
données via LastFM.

# Mise-à-jour d'une installation existante

La nouvelle version est disponible sur le [site du projet](https://koozic.net). Pas de crainte à
avoir, les sources précédentes peuvent être supprimées. On extrait la nouvelle version, et on lance
la mise-à-jour à partir du répertoire:

```
./odoo-bin -u oomusic -d koozic --stop-after-init
```

On peut relancer ensuite avec la commande habituelle.
