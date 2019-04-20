+++
title = "KooZic : sortie de la v2.0.0"
date = "2019-02-01T03:00:00+02:00"
tags = ["odoo", "streaming", "docker"]
archives = "2019"
type = "article"
+++

J'ai mis à profit mon temps libre de ces dernières semaines pour avancer dans la mise à jour de
KooZic en version 2. Au programme, quelques changements dans le style de l'interface, des
performances améliorées et une installation via Docker plus flexible.

# Nouveau style

Exit le menu de gauche, la navigation se fait à présent via un menu situé en haut de l'écran. Cela
permet de profiter de toute la largeur de l'écran.

[![01](/img/post/release-of-v2-0-0/01-thumb.png#center)](/img/post/release-of-v2-0-0/01.png)

Techniquement parlant, c'est Bootstrap 4 qui remplace la version 3. Cependant, l'organisation des
menus reste inchangée, la structure est identique.

[![02](/img/post/release-of-v2-0-0/02-thumb.png#center)](/img/post/release-of-v2-0-0/02.png)
[![03](/img/post/release-of-v2-0-0/03-thumb.png#center)](/img/post/release-of-v2-0-0/03.png)

Notez que cela représente la grosse majorité des modifications visibles. Le plus gros du travail a
été apporté sous le capot.

# Docker

Un [mystérieux contributeur](https://github.com/DocMarty84/koozic/pull/15) a gentiment proposé un
changement fondamental dans la manière dont les containers Docker sont gérés. Auparavant, il était
impossible de mettre à jour sans remettre le container à zéro, c'est-à-dire perdre toutes la
configuration. Grâce à l'utilisation de [Docker Compose](https://docs.docker.com/compose/), la base
de données contenant la configuration est à présent séparée de l'exécutable. Dès lors, il est
possible de mettre à jour le container contenant l'exécutable tout en conservant la configuration.

# Autres Nouveautés

Une série de petits détails ont été améliorés pour rendre l'interface plus réactive. Par ailleurs,
la durée de l'analyse initiale de la médiathèque a été diminuée. Notez que cela ne s'applique pas
sur une médiathèque distante, car dans ce cas le goulot d'étranglement si situe plutôt au niveau du
transfert de données en réseau.

[![04](/img/post/release-of-v2-0-0/04-thumb.png#center)](/img/post/release-of-v2-0-0/04.png)

Dernier point, il est désormais possible de choisir quelle outil d'analyse de tags sera utilisé:
Taglib ou Mutagen. Mutagen peut être utile pour des montages spécifiques, par exemple via
[rclone](https://rclone.org/). Dans tous les autres cas, Taglib est à préférer. Cela se configure
par dossier à analyser.

# Mise-à-jour d'une installation existante

Qui dit nouvelle version majeure dit aussi incompatibilité avec la version précédente. Il est dès
lors conseillé de désinstaller la v1 avant d'installer la v2.

```
wget https://raw.githubusercontent.com/DocMarty84/koozic_install/v2/koozic_install.py -O koozic_install.py
```

Pour désinstaller :

```
sudo python3 koozic_install.py uninstall
```

Installer :

```
sudo python3 koozic_install.py install
```

On peut se connecter sur [http://localhost:8069/](http://localhost:8069/) avec les identifiants
"admin" / "admin".

## Docker

Une installation Docker suppose que [Docker Compose](https://docs.docker.com/compose/install/) ait
été préalablement installé. Quand cela est fait, on récupère le strict nécessaire :

```
wget https://github.com/DocMarty84/koozic/releases/download/v2.0.0/koozic-v2.0.0-docker.tar.gz
tar xf koozic-v2.0.0-docker.tar.gz
cd docker
```

Dans le fichier "docker-compose.yml", on remplace "/music" par le répertoire contenant votre
médiathèque. On démarre le tout :

```
docker-compose build
docker-compose up -d
```

Au bout d'une dizaine de secondes, on peut se connecter sur
[http://localhost:8069/](http://localhost:8069/) avec les identifiants "admin" / "admin". Reste à
aller dans Configuration > Folders > Create et ajouter "/mnt/host" dans "Folder Path"

N'hésitez pas à soumettre un problème sur [Github](https://github.com/docmarty84/koozic/issues) si
nécessaire !
