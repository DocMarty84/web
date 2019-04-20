+++
title = "KooZic : image Docker prête à l'emploi"
date = "2017-11-24T03:00:00+02:00"
tags = ["odoo", "streaming", "docker"]
archives = "2017"
type = "article"
+++

Une galère assez commune chez tous les développeurs est de pouvoir fournir une méthode
d'installation simple du logiciel qu'on propose. Quant on ne se bat pas pour le rendre compatible
pour chaque plate-forme, on doit encore lutter pour que son bébé soit facilement accessible au
commun des mortels. Sous GNU/Linux en particulier, il faut jongler avec une myriade de
distributions, des systèmes de paquets différents, des dépendances... Bref, ça bouffe déjà un temps
dingue juste pour s'assurer que ça fonctionne un peu partout, mais en plus il faut emballer ça
proprement pour chaque distribution. C'est une tâche titanesque de se tenir à jour quand on fait ça
tout seul. Tellement titanesque que je ne l'ai pas fait, car je voulais une solution plus générique.

# C'est alors que Docker vint...

[Docker](https://www.docker.com/) est un logiciel libre qui automatise le déploiement d'applications
dans des conteneurs logiciels (merci Wikipedia). En d'autres termes, Docker permet d'exécuter une
application telle que KooZic dans un environnement isolé, et dans ce cas prêt à l'emploi.

Dans Docker, on ne va pas simplement exécuter KooZic, on va lancer un système complet dans lequel on
va exécuter ce qui est nécessaire. Dans notre cas, une Ubuntu 16.04 avec tout ce qu'il faut dedans :
les dépendances Python, PostgreSQL, FFmpeg...

# Mise en place

C'est simplissime. Tout d'abord, on [installe Docker](https://www.docker.com/get-docker) pour son
système. La Docker Community Edition (CE) est suffisante dans notre cas, et ça se trouve
[par ici](https://www.docker.com/community-edition).

Ensuite, dans un terminal (GNU/Linux, MacOS ou Windows) :

```
docker run -d -p 8069:8069 -p 8072:8072 -v <host_folder>:/mnt/host:ro --name koozic docmarty84/koozic
```

Il suffit de remplacer `<host_folder>` par le répertoire contenant votre collection musicale. Par
exemple, "/home/toto/Musique". On attend quelques minutes que tout ça se télécharge et se lance,
puis quand c'est fini... Et ben c'est tout ! On accède à KooZic sur
[http://localhost:8069/](http://localhost:8069/), comme d'habitude. Login et mot de passe sont
"admin", rien de nouveau non plus.

Une petite astuce cependant : lors de la configuration du répertoire contenant la musique, il faudra
indiquer "/mnt/host". En effet, notre répertoire contenant la musique est accessible dans Docker via
ce point de montage.

Par la suite, on pourra démarrer et arrêter KooZic avec les commandes suivantes :

```
docker start koozic
docker stop koozic
```

# Conclusion

Rendre KooZic accessible via Docker permet de facilement l'exécuter sur n'importe quelle
plate-forme, y compris Windows et MacOS (ok, je vais être honnête : j'ai pas testé sous Windows).
Par contre, à l'heure actuelle, la mise-à-jour d'une version à l'autre n'est pas encore possible.
