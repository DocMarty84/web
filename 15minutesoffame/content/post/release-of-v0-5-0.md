+++
title = "KooZic : sortie de la v0.5.0"
date = "2017-04-14T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2017"
type = "article"
+++

Un mois s'est écoulé depuis la sortie de la v0.4.0 de KooZic, la v0.5.0 est déjà prête. Enfin,
"déjà" est un bien grand mot : peu de changements fonctionnels, mais une grande avancée dans la
francisation du logiciel.

Changer la langue dans KooZic est un jeu d'enfant. Cependant, ceux qui ont essayé ont remarqué que
le logiciel n'était que partiellement traduit. Cela est dû au fait que Odoo, le logiciel sur lequel
est basé KooZic, est entièrement traduit. Cependant, l'extension musicale n'était jusqu'à
aujourd'hui pas traduite, ce qui est aujourd'hui chose faite. Outre les traductions, quelques
modifications ont été apportées au tri des pistes.

# Traduction française

Pour activer la traduction française, il est nécessaire d'être connecté en Administrateur. On se
rend dans "Settings", et on choisit "Load a Translation".

[![01](/img/post/release-of-v0-5-0/01-thumb.png#center)](/img/post/release-of-v0-5-0/01.png)

On choisit le français, puis "Load".

[![02](/img/post/release-of-v0-5-0/02-thumb.png#center)](/img/post/release-of-v0-5-0/02.png)
[![03](/img/post/release-of-v0-5-0/03-thumb.png#center)](/img/post/release-of-v0-5-0/03.png)

Il reste à changer les préférences de l'utilisateur.

[![04](/img/post/release-of-v0-5-0/04-thumb.png#center)](/img/post/release-of-v0-5-0/04.png)
[![05](/img/post/release-of-v0-5-0/05-thumb.png#center)](/img/post/release-of-v0-5-0/05.png)

Nous voilà avec une belle interface en français !

[![06](/img/post/release-of-v0-5-0/06-thumb.png#center)](/img/post/release-of-v0-5-0/06.png)

## Contribuer à la traduction

Il est tout à fait possible de contribuer à la traduction de KooZic. Cela peut se faire de façon
participative sur le projet [OOMusic de POEditor](https://poeditor.com/join/project/RMl91o65Bs).
Pour le moment, il est possible de traduire vers l'allemand, l'italien et l'espagnol. Si cela est
nécessaire, je rendrai d'autres langues disponible.

# Tri des pistes et albums

Le tri des pistes est amélioré pour prendre en compte une numérotation du style "1", "2", "3" au
lieu de "01", "02", "03". De plus, à partir de la v0.5.0, l'artiste d'un album sera déterminé comme
suit : si le tag "Album Artist" de l'album est présent sur les pistes, il est préféré. Si il n'est
pas rempli, le tag "Artist" est utilisé.

# Mise-à-jour d'une installation existante

La nouvelle version est disponible sur le [site du projet](https://koozic.net). Pas de crainte à
avoir, les sources précédentes peuvent être supprimées. On extrait la nouvelle version, et on lance
la mise-à-jour à partir du répertoire:

```
./odoo-bin -u oomusic -d koozic --stop-after-init
```

On peut relancer ensuite avec la commande habituelle.

Il est également suggéré d'utiliser une version de la librairie Python Mutagen au moins égale à la
v1.33. En effet, les versions précédentes souffrent d'un
[bug](https://github.com/quodlibet/mutagen/issues/252) qui associe de manière erronée le tag
"Performer" à l'artiste de l'album (le format FLAC n'est pas impacté par ce bug). Malheureusement,
par défaut Ubuntu 16.04 embarque la v1.22 de Mutagen, qui est affectée par ce bug. Pour mettre à
jour, on va passer par pip :

```
sudo apt install python-pip
sudo pip2 install mutagen --upgrade
```

Pour profiter pleinement du nouveau tri des pistes, il sera nécessaire de forcer un scan complet des
répertoires. Pour cela, passer tout d'abord en mode debug : changer l'URL de

http://localhost:8069/web

vers :

http://localhost:8069/web?debug

Dans "Configuration > Folders", il reste à cliquer sur "Force Full Scan". Notez que ce scan prendra
plus de temps que le scan initial, car mettre à jour complètement la bibliothèque prend plus de
temps que de la créer.
