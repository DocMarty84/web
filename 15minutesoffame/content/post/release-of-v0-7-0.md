+++
title = "KooZic : sortie de la v0.7.0"
date = "2017-09-01T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2017"
type = "article"
+++

KooZic souffle bientôt sa première bougie, et j'arrive petit à petit à un résultat satisfaisant d'un
point de vue des fonctionnalités, de la stabilité et des performances. Avec la v0.7.0, quelques
nouvelles vues font leur apparition.

# Miniatures d'artistes

Il est possible de récupérer les infos d'un artiste via LastFM depuis la
[v0.2.0](/nico/blog2/index.php?article26/koozic-sortie-de-la-v0-2-0). On récupère la biographie, les
meilleures pistes, les artistes similaires... Mais jusqu'à présent, pas l'image. C'est maintenant le
cas, avec en sus un mur de miniatures.

[![01](/img/post/release-of-v0-7-0/01-thumb.png#center)](/img/post/release-of-v0-7-0/01.png)

Ça rend la navigation bien plus agréable ;-) De plus, l'image de l'artiste est utilisée dans le
panneau de lecture si l'image de l'album n'est pas trouvé.

# Mode prévisualisation

Jusqu'à aujourd'hui, lancer la lecture d'une piste se faisait toujours depuis une liste de lecture.
C'était voulu pour une question de simplicité de code, mais pas toujours pratique. Ce n'est
désormais plus le cas : il est possible de lancer la lecture d'une piste depuis n'importe quel
endroit (vue de l'artiste, de l'album...). A la fin de la lecture, la liste de lecture en cours est
simplement reprise.

# Statistiques

Odoo fournit par défaut des outils qui permettent de créer des graphiques ainsi que des tableaux
croisés dynamiques. Cela a permis de créer de jolis rapports statistiques sur la composition de la
collection musicale.

[![02](/img/post/release-of-v0-7-0/02-thumb.png#center)](/img/post/release-of-v0-7-0/02.png)

Cela fonctionne avec les albums, mais aussi les pistes.

[![03](/img/post/release-of-v0-7-0/03-thumb.png#center)](/img/post/release-of-v0-7-0/03.png)

Cette dernière vue (dite "pivot") permet d'avoir une vue claire sur la répartition des genres
musicaux. Et par ailleurs, on peut facilement détecter les genres musicaux "doublons" ("Pop/Rock" et
"Pop-Rock", par exemple).

# Autres Nouveautés

Beaucoup de travail a été apporté à la réécriture de certaines parties de code, pour les rendre plus
lisibles, mais aussi améliorer sensiblement les performances. En fait, cela représente la plus
grosse masse de travail de cette version, mais au final, ce n'est pas le plus marquant visuellement
;-)

# Mise-à-jour d'une installation existante

La nouvelle version est disponible sur le [site du projet](https://koozic.net). Pas de crainte à
avoir, les sources précédentes peuvent être supprimées. On extrait la nouvelle version, et on lance
la mise-à-jour à partir du répertoire:

```
./odoo-bin -u oomusic,oovideo -d koozic --stop-after-init
```

On peut relancer ensuite avec la commande habituelle.
