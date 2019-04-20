+++
title = "KooZic : sortie de la v0.8.0, dernière release..."
date = "2018-04-06T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2018"
type = "article"
+++

... utilisant Python 2.

Les derniers mois ont été assez calmes au niveau de [KooZic](https://koozic.net/),
logiciel de streaming musical. Le développement ne s'est pas arrêté pour autant, que du contraire.
Plusieurs fonctionnalités ont été développées. Entre autres, le support de la normalisation audio,
du non-transcodage et d'un convertisseur.

# Normalisation audio

Lorsqu'une liste de lecture est parcourue, il nous est tous arrivé au moins une fois de passer d'un
titre à un autre et de percevoir une nette différence de volume. Ceci s'explique simplement par le
fait que qu'un fichier audio possède un certain niveau de volume, qui peut être différent de l'un à
l'autre. Évidemment, lors de l'écoute d'un album complet, ceci n'arrive pas, vu que le volume de
l'album est cohérent d'un morceau à l'autre. Mais lorsque les titres proviennent d'origines
différentes, le volume peut fortement varier.

De nombreux lecteurs audio permettent de normaliser le volume des titres grâce à la méthode
[ReplayGain](https://en.wikipedia.org/wiki/ReplayGain). Plus récemment, l'industrie de diffusion a
opté pour une nouvelle méthode de normalisation, la bien nommée
[EBU R128](https://tech.ebu.ch/loudness) (European Broadcasting Union Recommendation R128). Depuis
la version 3.2.1, FFMpeg supporte nativement cette méthode de normalisation. Cool, hein ?

[![01](/img/post/release-of-v0-8-0/01-thumb.png#center)](/img/post/release-of-v0-8-0/01.png)

Avec la v0.8.0 de KooZic, il est donc à présent possible de paramétrer une liste de lecture pour que
la normalisation sus-nommée soit appliquée à tous les titres. Pour que cela fonctionne, il sera
évidemment nécessaire de disposer de FFMpeg >= 3.2.1. Notez qu'un binaire est maintenant distribué
avec le package KooZic. Il suffit de le copier dans "/usr/local/bin", et le tour est joué.

Une information importante à avoir en tête : la normalisation est un processus gourmand en
ressources et augmente de manière non négligeable la durée de conversion. À voir donc si votre
serveur peut tenir cette charge supplémentaire.

# Et si on ne convertissait plus du tout ?

L'option exactement opposée a été introduite dans cette nouvelle mouture. Et si on profitait des
capacités de nos navigateurs modernes pour lire les fichiers audio sans aucun traitement ?

[![02](/img/post/release-of-v0-8-0/02-thumb.png#center)](/img/post/release-of-v0-8-0/02.png)

Il est possible de paramétrer une liste de lecture pour contourner complètement l'utilisation de
FFMpeg, et simplement lire le fichier tel qu'on le possède. Cela permet de décharger fortement le
serveur, au prix d'une augmentation du trafic réseau.

Il est à noter que les résultats diffèrent d'un navigateur à l'autre, selon le format. Selon votre
configuration, cela peut s'avérer une option très utile.

# Un outil de conversion, mais pour quoi faire ?

Parce que j'en avais besoin. Il existe une myriade d'outils pour convertir un fichier audio d'un
format vers un autre. La plupart font ça très bien. Mais, à ma connaissance, aucun ne permet de
facilement importer une liste de lecture et de la convertir, en respectant la hiérarchie des
fichiers. KooZic est capable de le faire.

[![03](/img/post/release-of-v0-8-0/03-thumb.png#center)](/img/post/release-of-v0-8-0/03.png)

À l'image des listes de lecture, on peut facilement créer une liste de fichiers à convertir. Il est
également possible d'importer une liste de lecture existante. On choisit le mode de conversion, la
qualité, le répertoire de sortie (par défaut dans "/tmp/koozic/"), et on démarre. La conversion
démarre de manière asynchrone après moins de 2 minutes. Rien de très sexy, il faut rafraîchir la
page pour voir l'avancement. Mais ça fonctionne, et c'est efficace.

# Autres Nouveautés

Dans les nouveautés perceptibles, on notera le pré-chargement de la piste suivante lors de la
lecture. 30 secondes avant la fin d'une piste, KooZic va charger la piste suivante. Cela permet de
diminuer de manière conséquente le gap entre 2 pistes, et se rapprocher d'une configuration
"gapless".

Comme annoncé plus haut, cette version est la dernière version utilisant Python 2 (Odoo v10). La
prochaine version utilisera Python 3 (Odoo v11).

# Mise-à-jour d'une installation existante

La nouvelle version est disponible sur le [site du projet](https://koozic.net). Pas de crainte à
avoir, les sources précédentes peuvent être supprimées. On extrait la nouvelle version, et on lance
la mise-à-jour à partir du répertoire:

```
./odoo-bin -u oomusic,oovideo -d koozic --stop-after-init
```

On peut relancer ensuite avec la commande habituelle.
