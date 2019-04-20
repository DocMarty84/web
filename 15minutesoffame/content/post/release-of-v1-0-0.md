+++
title = "KooZic : sortie de la v1.0.0"
date = "2018-08-10T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2018"
type = "article"
+++

Une version 1.0.0 signifie-t-elle un remaniement important de KooZic par rapport à la
[v0.8.0](/index.php?article35/koozic-sortie-de-la-v0-8-0-derniere-release) ?
Autant être clair : non, pas du tout. Cela marque surtout une série de changements internes qui
rendent les 2 versions incompatibles, et qui justifient du coup un saut de version. Mais cela
n'empêchent pas une série d'améliorations et de nouvelles fonctionnalités d'avoir été intégrées à
la nouvelle mouture.

# Odoo v11.0 et Python 3

Alors que les versions 0.x utilisaient [Odoo](https://www.odoo.com/) v10 et
[Python 2](https://pythonclock.org/), la branche 1.x utilisera Odoo v11 et Python 3. C'est surtout
dans un souci de modernisation et de support que ce choix s'inscrit. En effet, une version d'Odoo
est supportée 3 ans, et le support de Python 2 sera abandonné le 1 janvier 2020. On n'y est pas
encore, mais autant rester à jour !

# Liens de téléchargement

Il est toujours pratique de partager une piste ou un album. La v1.0.0 introduit la possibilité de
générer des liens de téléchargement facilement. En un clic, un lien peut-être généré sur une piste,
un album, un artiste, un genre musical ou une liste de lecture. Il peut alors être partagé : au
premier accès à ce lien, une archive ZIP sera générées avec les fichiers correspondants. Il est
possible de créer plusieurs liens par objet, et il est notamment possible de définir une durée de
vie pour chaque lien.

[![01](/img/post/release-of-v1-0-0/01-thumb.png#center)](/img/post/release-of-v1-0-0/01.png)

# HTML5 ou Web Audio

KooZic utilise les capacités du navigateur pour lire les fichiers audio, sans nécessiter de plugins
externes (heureusement, on est en 2018, Flash est mort depuis longtemps). Ça, c'est bien. Sauf qu'on
est à la merci du bon vouloir du navigateur quand il s'agit de récupérer le flux audio, et ça c'est
moins marrant.

Dans l'approche simple et naïve que KooZic utilise, les pleins pouvoirs sont donnés au navigateur
concernant le chargement de la piste audio. En HTML5, les navigateurs modernes optent pour un mode
"intelligent" : ils ne mettent en cache que ce qui est nécessaire pour éviter le gaspillage de bande
passante. Ça parait être la bonne approche... sauf si vous écoutez une compilation qui dure une
heure (style mega mix). En effet, cela implique que la connexion entre le navigateur et le serveur
va rester ouverte pratiquement tout le temps de la lecture. Si le serveur ou votre connexion
Internet fait un pet de travers durant cette période, la connexion va couper, et la piste va
s'arrêter.

Pour pallier à ce problème, une liste de lecture peut à présent utiliser l'API
[Web Audio](https://developer.mozilla.org/docs/Web/API/Web_Audio_API). Celle-ci permet d'appliquer
des effets à une piste audio, mais dans le cas qui nous préoccupe de charger l'entièreté de la piste
avant de la jouer. Cela implique un temps de chargement plus long, mais une lecture bien plus
stable.

[![02](/img/post/release-of-v1-0-0/02-thumb.png#center)](/img/post/release-of-v1-0-0/02.png)

# Amélioration des performances

Ou plutôt désactivation de certaines fonctionnalités qui peuvent être gourmandes lorsque les
performances de la machine sont limitées :-) Jusqu'à présent, les paramètres de configuration
étaient restés très limités. C'est un choix assumé, le but étant de conserver une interface simple
avec une configuration de base adaptée à chaque installation. Ça, c'est ce que je croyais... Il m'a
été rapporté des cas assez extrêmes d'installations sur lesquels la configuration de base était
inutilisable. Cela a impliqué une série de modifications qui évitent la surconsommation de RAM. De
plus, 3 options ont vu le jour :

*   Désactivation des actions d'arrière-plan
*   Vue par défaut sans miniatures
*   Infos LastFM récupérées à la demande

[![03](/img/post/release-of-v1-0-0/03-thumb.png#center)](/img/post/release-of-v1-0-0/03.png)

Tout cela permet de rendre l'installation bien plus légère pour les petites configurations (enfin,
surtout pour les très grosses médiathèques...).

# Autres Nouveautés

L'API Subsonic est disponible en XML (par défaut) et JSON. J'ai appris à mes dépens qu'il n'y avait
pas de conversion standardisée ente ces deux formats, ce qui fait que le support JSON de KooZic
était assez mauvais. Dès lors, les applications qui utilisaient JSON à la place de XML (par
exemple : Ultrasonic) fonctionnaient plutôt mal. Cela devrait en principe être réglé.

# Mise-à-jour d'une installation existante

Malheureusement, la v1.0.0 est incompatible avec les versions précédentes. La nouvelle installation
va dès lors ignorer la configuration précédente. Avec les scripts d'installation, ça se fait facilement :

```
curl https://raw.githubusercontent.com/DocMarty84/koozic/11.0/extra/installer/koozic_install.py > k_install.py
chmod +x k_install.py
sudo ./k_install.py install
```

Si vous aviez installé KooZic sans passer par le script d'installation, il vous faudra désinstaller
manuellement. N'hésitez pas à soumettre un problème sur
[Github](https://github.com/docmarty84/koozic/issues) !
