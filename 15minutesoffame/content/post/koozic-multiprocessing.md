+++
title = "KooZic : activer le multiprocessing"
date = "2017-02-10T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2017"
type = "article"
+++

[KooZic](https://koozic.net/) est un logiciel de streaming musical à installer sur votre propre
serveur. Dans sa configuration standard, il utilise un seul processeur, ce qui est généralement
suffisant pour une utilisation avec un seul utilisateur. Mais il est possible de profiter de
l'architecture multicœur des machines actuelles assez simplement...

Activer le multiprocessing peut se justifier pour plusieurs raisons :

*   de nombreux utilisateurs seront connectés en même temps
*   améliorer globalement les performances, en particulier la récupération des images
*   parce que c'est facile

# Dépendances

Il est nécessaire d'installer psycogreen et gevent. Sous Ubuntu, ça se fait simplement :

```
sudo apt install python-psycogreen python-gevent
```

Jusque là, rien de très sorcier.

# Mode multi-worker

Activer le multiprocessing se fait en passant en paramètre un nombre non nul de "workers".
L'estimation habituelle est la suivante : `#workers = #CPU * 2` (pour un processeur multi-thread).
Pour un serveur avec 4 CPU / 8 threads, cela donnera un maximum de 8 workers dédiés aux connexions
client, alors qu'un worker sera automatiquement utilisé pour les tâches planifiées.

Pour ce qui est de l'utilisation de la mémoire vive, 1 worker utilise environ 150 Mo de RAM.

En pratique, on lance Koozic avec la commande suivante :

```
./odoo-bin --workers=8
```

Rien de bien sorcier jusque là, sauf que dans le cas de KooZic, ça va poser des problèmes si vous
avez une grosse collection musicale. En effet, en mode multi-worker, KooZic stoppe un processus s'il
dure plus de 60s (temps CPU) ou 120s (temps réel). Et ça, c'est pas assez pour les tâches de fond
que KooZic doit exécuter (scan de la médiathèque, cache des images et des infos LastFM). On va donc
augmenter largement ces paramètres :

```
./odoo-bin --workers=8 --limit-time-cpu=1800 --limit-time-real=3600
```

Ça devrait faire l'affaire, même pour les grosses librairies musicales.

# Limite d'utilisateurs

C'est bien beau tout ça, mais ça fait combien d'utilisateurs au total ? Sur le
[site de référence de Odoo](https://www.odoo.com/documentation/10.0/setup/deploy.htm) (sur lequel se
base KooZic), on évalue 1 worker = 6 utilisateurs concurrents. Dans le cas de KooZic, on pourrait
facilement multiplier par 4 ou 5, car on ne fait majoritairement que de la consultation
d'information et des recherches légères.

Mais (car il y a un mais) KooZic lance un processus de conversion (appel à FFMpeg) pour chaque
lecture de piste. Cela occupe 100 % d'un thread pendant environ 5 secondes, pour une piste de 4
minutes. Cela fait qu'un thread peut couvrir dans le meilleur des cas les besoins en conversion
d'une petite cinquantaine d'utilisateurs (240s / 5s = 48). Notons que l'utilisation de la RAM par
FFMpeg est très faible.

Avec tout ceci, on peut estimer 1 worker = 15 utilisateurs concurrents. Cela devrait garantir une
utilisation fluide, sans surcharger en permanence le serveur à 100 %.
