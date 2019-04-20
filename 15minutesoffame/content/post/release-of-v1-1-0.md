+++
title = "KooZic : sortie de la v1.1.0"
date = "2018-12-20T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2018"
type = "article"
+++

Alors que KooZic a fêté discrètement ses 2 ans, le développement continue son petit bonhomme de
chemin, avec comme à l'habitude une release emballée rapidement mais un article qui traîne à
s'écrire. Bref, développer des fonctionnalités c'est marrant, mais rédiger un bel article les
expliquant ça l'est moins.

# Listes de lecture intelligentes et dynamiques

Le concept de liste de lecture intelligente est dans les tuyaux depuis un bon moment déjà. Rien de
révolutionnaire par rapport à d'autres softs : KooZic va créer automatiquement une liste de lecture
sur base d'un des modes supportés :

*   Aléatoire
*   Déjà joué
*   Jamais joué
*   Le plus joué
*   Dernièrement écouté
*   Récent
*   Favoris
*   Le mieux noté
*   Le moins bien noté

[![01](/img/post/release-of-v1-1-0/01-thumb.png#center)](/img/post/release-of-v1-1-0/01.png)

Par défaut, la liste est statique, c'est-à-dire qu'un nombre défini de titres est ajouté. Il est
également possible de définir la liste comme étant dynamique. Dans ce cas, une piste est
automatiquement ajoutée au fur et à mesure qu'on avance dans la liste de lecture.

# Partage de la bibliothèque musicale

Jusqu'à la v1.0.0, chaque utilisateur avait sa propre collection musicale. D'un point de vue
technique, cela rend les choses plus simples à gérer : chacun ses fichiers, ses titres, ses albums
et ses artistes. De plus pas de mélange, et on ne retrouve pas dans sa collection de jazz les albums
de sa petite sœur. Cependant, si plusieurs utilisateurs doivent accéder à la même collection
musicale, cela veut dire ajouter la même collection pour chacun d'eux. Si de nombreux utilisateurs
doivent accéder à la même collection, cela peut poser problème car la base de données est remplie
de redondances.

[![02](/img/post/release-of-v1-1-0/02-thumb.png#center)](/img/post/release-of-v1-1-0/02.png)

Avec la v1.1.0, une option est introduite pour partager la collection musicale entre utilisateurs.
Attention, c'est tout ou rien : soit chacun a sa propre collection, soit on partage tout. Les
données relatives au nombre d'écoutes, les favoris, etc. restent tout de même spécifiques à chaque
utilisateur. Notez qu'il n'est pas dans la roadmap de pouvoir gérer plus finement les accès. Cela
deviendrait vite une usine à gaz pour une utilité assez limitée.

# Autres Nouveautés

Les options de la liste de lecture ont légèrement été réorganisées pour plus de clarté. Par
ailleurs, les pochettes d'album intégrées sont à présent utilisées si aucun fichier "cover", "front"
ou "folder" n'est présent. Dans la vue par dossier, il est désormais possible d'ajouter les pistes
récursivement.

Une option a aussi été ajoutée pour ignorer les tags ID3 sur un répertoire. Cela rendra l'analyse
beaucoup plus rapides pour ceux qui ne les utilisent pas. Par contre, cela signifie que seule la vue
par répertoire contiendra des informations. Les vues pistes, albums, artistes et genres resteront
vides.

Finalement, l'ordre des transcoders est maintenant pris en compte lors du streaming. Auparavant,
Opus était le format par défaut, suivi par Ogg et MP3. Dorénavant, le format par défaut sera celui
du transcoder ayant la plus haute priorité. Dans le doute, ne touchez à rien ;-)

# Mise-à-jour d'une installation existante

La v1.1.0 est compatible avec les versions précédentes. Pour mettre à jour (attention, l'adresse a
changé) :

```
curl https://raw.githubusercontent.com/DocMarty84/koozic_install/v1/koozic_install.py > k_install.py
chmod +x k_install.py
sudo ./k_install.py upgrade
```

N'hésitez pas à soumettre un problème sur [Github](https://github.com/docmarty84/koozic/issues) si
nécessaire !
