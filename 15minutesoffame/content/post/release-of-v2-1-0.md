+++
title = "KooZic : sortie de la v2.1.0"
date = "2019-04-05T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2019"
type = "article"
+++

Après un changement majeur d'interface en v2.0.0, KooZic se socialise avec la prise en charge des
événements musicaux. C'est aussi la première version avec l'intégration de LDAP.

# Concerts et événements

La grosse nouveauté de cette version est l'ajout d'une partie sociale à KooZic via la récupération
des concerts des artistes. Il est possible de mettre à jour les événements liés à un artiste à
partir de sa fiche, dans l'onglet "Événements". De plus, chaque utilisateur peut suivre les artistes
de son choix via le bouton "Suivre", en haut à droite.

[![01](/img/post/release-of-v2-1-0/01-thumb.png#center)](/img/post/release-of-v2-1-0/01.png)

Les événements liés aux artistes suivis sont agrégés dans le menu supérieur "Événements". Par
défaut, ils sont groupés par mois, ce qui permet d'avoir une vue d'ensemble assez rapidement.

[![02](/img/post/release-of-v2-1-0/02-thumb.png#center)](/img/post/release-of-v2-1-0/02.png)

Finalement, il est également possible de définir la distance maximale à laquelle un événement se
produit pour qu'il soit affiché dans cette liste. Chaque utilisateur peut modifier ses préférences
(à partir du menu tout en haut à droite), et indiquer son emplacement et la distance maximale
autorisée.

[![03](/img/post/release-of-v2-1-0/03-thumb.png#center)](/img/post/release-of-v2-1-0/03.png)

# Amélioration de l'UI

Un des problèmes d'interface de KooZic est le nombre de clics nécessaire avant de jouer un titre. Il
faut ajouter les piste dans une liste de lecture, puis lancer. C'est parfois pénible, mais jusqu'à
présent je n'avais pas trouvé de bonne solution. C'est maintenant chose faite, des boutons "Ajouter
et jouer" on été introduits un peu partout.

[![04](/img/post/release-of-v2-1-0/04-thumb.png#center)](/img/post/release-of-v2-1-0/04.png)

Un tel bouton a pour effet d'ajouter les pistes de l'album à la liste de lecture courante, et lancer
sa lecture.

# Intégration avec LDAP

Il est possible d'intégrer les utilisateurs KooZic avec un annuaire LDAP. Pour cela, il faut tout
d'abord installer le module approprié via le menu "Applications" : "Authentification via LDAP".

[![05](/img/post/release-of-v2-1-0/05-thumb.png#center)](/img/post/release-of-v2-1-0/05.png)

Ensuite, il faut configurer le serveur dans les Paramètres, menu "Utilisateurs et sociétés >
Serveurs LDAP". Un exemple de configuration est présenté ci-après avec un serveur de test.

[![06](/img/post/release-of-v2-1-0/06-thumb.png#center)](/img/post/release-of-v2-1-0/06.png)

# Autres Nouveautés

Le lecteur vidéo [Clappr](http://clappr.io/) a été mis à jour, avec une nouvelle gestion des
sous-titres (support des SRT et WEBVTT).

# Mise-à-jour d'une installation existante

La v2.1.0 est compatible avec la version précédente. Pour mettre à jour :

```
curl https://raw.githubusercontent.com/DocMarty84/koozic_install/v2/koozic_install.py > k_install.py
chmod +x k_install.py
sudo ./k_install.py upgrade
```

Notes :

*   Une nouvelle librairie est nécessaire : `sudo pip3 install webvtt-py==0.4.2`
*   Pour installer le module LDAP, il faut tout d'abord recharger la liste des modules manuellement.
Aller à [http://localhost:8069/web?debug](http://localhost:8069/web?debug), puis "Applications" et
"Mettre à jour la liste des Applications"

N'hésitez pas à soumettre un problème sur [Github](https://github.com/docmarty84/koozic/issues) si
nécessaire !
