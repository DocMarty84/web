+++
title = "KooZic : script d'installation automatique"
date = "2018-04-05T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2018"
type = "article"
+++

DEB, RPM, PKG, Debian, Ubuntu, Fedora, CentOS, OpenSUSE, Archlinux, Gentoo... Autant de systèmes de
paquets et de distributions qui font de GNU/Linux un écosystème riche et varié. Mais aussi un enfer
à supporter. Le système de packaging change d'un système à l'autre, et les dépendances varient d'une
version à l'autre. Essayez de générer un DEB d'une application un peu complexe compatible pour
Ubuntu 14.04, 16.04 (bientôt 18.04), Debian 8 et 9, et vous allez vite comprendre la galère. J'ai
essayé, j'en ai eu marre et j'ai laissé tombé. Mais je n'ai pas pour autant baissé les bras...

Un beau package bien emballé est la voie royale pour s'immiscer dans la logithèque de l'utilisateur
moyen. Mais pour un projet mené avec une équipe limitée (moi), c'est beaucoup trop chronophage.
Ayant définitivement abandonné l'idée de me lancer dans le packaging multi-plateforme du logiciel de
streaming musical [KooZic](https://koozic.net/), j'ai opté pour quelque chose de plus simple : un
script d'installation.

# Utilisation

Les systèmes suivant sont supportés :

*   Ubuntu 16.04 (et dérivés, par exemple Linux Mint 18.x)
*   Debian 9
*   Debian 8
*   Fedora 27
*   CentOS 7.4

Si votre système est différent, tant pis, ça sert à rien de continuer à lire. Si il est dans la
liste, l'installation tient en 3 commandes :

```
curl https://raw.githubusercontent.com/DocMarty84/koozic/10.0/extra/installer/koozic_install.py > k_install.py
chmod +x k_install.py
sudo ./k_install.py install
```

Y'a plus qu'à aller sur [http://localhost:8069](http://localhost:8069)...

Au niveau des options, on a la possibilité de spécifier :

*   `-u` : l'utilisateur qui sera utilisé (par défaut : root)
*   `-d` : le répertoire d'installation (par défault : /opt)

Supprimer KooZic ?

```
sudo ./k_install.py uninstall
```

Voilà.

# Mais ça fait quoi exactement ?

Lancer un script quelconque en root n'est franchement pas ce qu'il y a de plus sûr. Qui sait ce qui
peut se cacher derrière ce qui est exécuté ? Celui qui prend la peine de lire le script, bien sûr.
Pour ceux que ça ne motive pas plus que ça, il reste à me faire confiance.

Juré craché, le script va :

1.  installer les dépendances via le système de paquets
2.  installer les dépendances Python manquantes avec pip
3.  mettre en place un serveur PostgreSQL
4.  télécharger la dernière version
5.  installer FFMpeg dans /usr/local/bin
6.  initialiser KooZic
7.  installer et démarrer un script systemd qui permettra de lancer KooZic au démarrage du système

En cas de désinstallation, les étapes 1 à 3 ne seront pas annulées, pour éviter de casser quoi que
ce soit. Le reste disparaîtra à tout jamais. Ou jusqu'à la prochaine installation.

# Migration d'une installation existante

Si vous êtes de ceux qui utilisent KooZic, merci d'avoir passé le cap de l'installation manuelle ;-)
Pour rendre votre installation compatible avec l'installation automatique, il faut stopper KooZic et
désactiver le démon systemd si vous en avez créé un. Ensuite, rien de bien exceptionnel :

```
sudo ./k_install.py install -u USER
```

Remplacez USER par l'utilisateur qui était utilisé précédemment. Normalement, ça devrait
fonctionner. Si pas... ben... Criez à l'aide.
