+++
title = "KooZic : sortie de la v0.4.0"
date = "2017-03-17T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2017"
type = "article"
+++

Bientôt 6 mois après la première version publique de KooZic, une nouvelle mouture vient de voir la
jour: la v0.4.0. Un grand pas en avant avec l'arrivée d'une navigation par dossier revue et
corrigée. Cela devrait (enfin !) satisfaire ceux chez qui la collection musicale n'est que
partiellement ou incorrectement taggée.

KooZic a été conçu pour donner la possibilité d'accéder facilement à une collection musicale
correctement taggée. C'était et cela reste toujours le point fort du logiciel, car cela permet de
naviguer et rechercher très facilement par album, artiste ou genre musical, ce que d'autres font
avec un support limité. Seulement voilà, si passer des heures à tagger votre collection n'est pas
votre tasse de thé, le logiciel a un intérêt assez limité. Un mode de navigation par dossier a bien
été introduit dans la v0.2.0, mais il n'était pas franchement ergonomique.

# Navigation par dossier

Le nouveau mode de navigation suit l'idée général du logiciel, à savoir un accès clair et performant
aux fonctions essentielles, quelque soit la taille de la collection musicale. Une capture d'écran
vaut mieux qu'un long discours :

[![01](/img/post/release-of-v0-4-0/01-thumb.png#center)](/img/post/release-of-v0-4-0/01.png)

Le premier élément de la liste est le répertoire courant. Le second ("..") permet de revenir au
répertoire parent. Ensuite, on trouve la liste des sous-répertoires, puis des pistes musicales. Il
est possible d'ajouter à la liste de lecture courante toutes les pistes d'un répertoire en cliquant
sur le "+". Une piste s'ajoute quant à elle avec un simple click.

[![02](/img/post/release-of-v0-4-0/02-thumb.png#center)](/img/post/release-of-v0-4-0/02.png)
[![03](/img/post/release-of-v0-4-0/03-thumb.png#center)](/img/post/release-of-v0-4-0/03.png)

# Liste de lecture courante

L’interaction de la liste de lecture courante a été améliorée : un click sur la ligne permet de
lancer la lecture d'un titre, il n'est plus nécessaire d'utiliser le bouton "Play". La piste mise en
évidence est bien mise à jour à chaque changement de piste, et pas seulement au rafraîchissement de
la page. C'est loin d'être fondamental, mais cela améliore l'expérience générale.

# Mise-à-jour d'une installation existante

La nouvelle version est disponible sur le [site du projet](https://koozic.net). Pas de crainte à
avoir, les sources précédentes peuvent être supprimées. On extrait la nouvelle version, et on lance
la mise-à-jour à partir du répertoire:

```
./odoo-bin -u web -d koozic --stop-after-init
```

Attention, c'est bien "-u web", donc légèrement différent des mises-à-jour précédentes. On peut
relancer ensuite avec la commande habituelle.
