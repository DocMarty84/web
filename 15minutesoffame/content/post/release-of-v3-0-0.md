+++
title = "KooZic : sortie de la v3.0.0"
date = "2020-02-21T03:00:00+02:00"
tags = ["odoo", "streaming", "planet"]
archives = "2020"
type = "article"
+++

[KooZic](https://koozic.net/), le serveur de musique basé sur Odoo sort aujourd'hui en v3.0.0.

Ces derniers mois ont été dédiés à la mise-à-jour de KooZic en v3. D'un point de vue fonctionnalités, KooZic est considéré comme un logiciel mature. Dès lors, l'essentiel du travail a lieu sous le capot. Le code source est gardé aussi propre que possible, et parfois retravaillé dans un souci d'amélioration des performances et de la stabilité. De plus, il est conservé compatible avec les dernières versions de Python et PostgreSQL.

N'hésitez pas à essayer [le serveur de démonstration](https://demo.koozic.net/public) ou suivre les [instructions d'installation](https://koozic.net/installation/).

# Contrôle à distance

L'objectif de KooZic est d'accéder à votre médiathèque à distance. Cependant, le contrôle de la lecture est censé se faire directement depuis l'interface du navigateur web.

Dans mon cas, j'utilise KooZic pour jouer la maison dans mon salon, depuis un media center. En effet, les liste de lectures intelligentes et personnalisées me permettent de filtrer efficacement le genre de musique qui doit être joué dans la pièce. J'ai créé une liste de lecture dynamique suivant certains critères et je la laisse jouer pendant des centaines d'heures. Cependant, j'ai tout de même besoin de facilement mettre en pause, passer à la piste suivante ou encore diminuer ou augmenter le volume.

La nouvelle version dispose d'un contrôle à distance simplifié. Il est possible de générer un lien unique que autorise le contrôle du lecteur depuis n'importe quel appareil.

[![01](/img/post/release-of-v3-0-0/01-thumb.png#center)](/img/post/release-of-v3-0-0/01.png)

Quand on accède à cette adresse depuis un smartphone, une télécommande permet d'effectuer les actions habituelles de lecture.

[![02](/img/post/release-of-v3-0-0/02-thumb.png#center)](/img/post/release-of-v3-0-0/02.png)

Toute action est capturée et notifiée dans l'interface web.

[![03](/img/post/release-of-v3-0-0/03-thumb.png#center)](/img/post/release-of-v3-0-0/03.png)

Si la commande à distance est configurée comme étant "Publique", quiconque disposant du lien peut contrôler la lecture sans besoin d'avoir un compte. Un invité peut dès lors scanner le QR code et contrôler la lecture.

Il est important de noter que **HTTPS doit être configuré** sur votre installation pour que cela fonctionne. Une procédure est détaillée dans la [documentation](https://doc.koozic.net/installation/https.html).

# Autres nouveautés

La v3 supporte les pochettes intégrées des fichiers M4A ainsi que Vorbis (OGG, OGA, OPUS). Il est également possible d'ajouter la même piste plus d'une fois dans une liste de lecture, et nettoyer les pistes dupliquées dans une liste de lecture.

# Mise-à-jour d'une installation existante

Une nouvelle version majeure marque une incompatibilité avec la version précédente. Il est dès lors conseillé de désinstaller la v2 avant d'installer la v3.

```
wget https://raw.githubusercontent.com/DocMarty84/koozic_install/v3/koozic_install.py -O koozic_install.py
```

Pour désinstaller :

```
sudo python3 koozic_install.py uninstall
```

Pour installer :

```
sudo python3 koozic_install.py install
```

Il est ensuite possible de se connecter sur [http://localhost:8069/](http://localhost:8069/) avec
les identifiants "admin" / "admin".

### Docker

1. Arrêtez et supprimer la version précédente  : `docker-compose down`
2. Suivez mes [instructions d'installation pour Docker](https://koozic.net/installation/).

N'hésitez pas à soumettre un [problème Github](https://github.com/docmarty84/koozic/issues) si
nécessaire !
