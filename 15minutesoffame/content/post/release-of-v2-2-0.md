+++
title = "KooZic : sortie de la v2.2.0"
date = "2019-08-16T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2019"
type = "article"
+++

Plusieurs discussions sur les médias sociaux ont mené au développement de nouvelles fonctionnalités
intégrées dans la nouvelle v2.2.0. Avant de les passer en revue, c'est avec fierté que nous
annonçons la naissance de... la [documentation officielle](https://doc.koozic.net/) ! Certaines
parties sont encore manquantes, mais les parties principales sont maintenant documentées.

# Listes de lecture intelligentes personnalisées

Les listes de lecture intelligentes et dynamiques ont été introduites en
[v1.1.0](/post/release-of-v1-1-0/) avec la possibilité de générer automatiquement des listes basées
sur plusieurs modes prédéfinis (par exemple: aléatoire, favoris, mieux notés...). Cette nouvelle
version permet de sélectionner les pistes suivant des critères personnalisés. Ces derniers sont
définis à la création de la liste de lecture. Voici deux exemples.

*Exemple 1* : pistes dont le genre est soit "blues", "country" ou "americana".

[![01](/img/post/release-of-v2-2-0/01-thumb.png#center)](/img/post/release-of-v2-2-0/01.png)

*Exemple 2* : pistes dont le genre est soit "americana", "blues", "jazz", "country", ... et "pop".
Mais dans le cas de "pop", l'artiste ne peut pas contenir certaines valeurs comme "gara", "dion" ou
"obispo" (traduction : on joue de la pop, mais pas Céline Dion).

[![02](/img/post/release-of-v2-2-0/02-thumb.png#center)](/img/post/release-of-v2-2-0/02.png)

# Étiquettes personnalisées

Les étiquettes ID3 habituelles ne sont parfois pas suffisantes dans le classement de la médiathèque.
On pourrait vouloir marquer les pistes avec des valeurs spécifiques, par exemple "fête",
"romantique", etc. Un nouveau champ a été ajouté sur les pistes, les albums et les artistes. Dans
l'exemple suivant, nous ajoutons les étiquettes "energetic" et "indie" à un album :

[![03](/img/post/release-of-v2-2-0/03-thumb.png#center)](/img/post/release-of-v2-2-0/03.png)

Les étiquettes colorées sont également affichées en vue Kanban :

[![04](/img/post/release-of-v2-2-0/04-thumb.png#center)](/img/post/release-of-v2-2-0/04.png)

Il est également possible de rechercher et filtrer sur ces étiquettes.

# Désactivation du transcodage et format de l'API Subsonic

Deux paramètres ont fait leur apparition pour couvrir des cas spécifiques.

Le premier est l'utilisation de KooZic sur du matériel aux performances limitées, par exemple un
Raspberry Pi. Plusieurs utilisateurs ont effectué l'installation Docker sur un Raspberry Pi, et cela
fonctionne parfaitement (une installation classique devrait fonctionner également). Un invonvénient
d'une telle machine est sa faible puissance CPU, rendant le transcodage bien trop lent pour être
utilisable. Dans de tels cas, il est nécessaire de désactiver complètement le transcodage et envoyer
les fichiers tels quels. Notez que cette option l'emporte sur toutes les autres options d'encodage,
y compris celle décrite juste après : quand elle est activée, aucun transcodage n'est possible !

La deuxième option impacte le format de l'API Subsonic. Pour des raisons de compatibilité, le format
par défaut pour les applications Subsonic est MP3, à moins qu'un autre format ne soit explicitement
demandé par l'app elle-même. Cependant, les smartphones modernes sont capables de lire des formats
bien plus efficaces, comme OGG et Opus. Une option a été ajoutée pour sélectionner le format envoyé
aux applications Subsonic. L'utilisation la plus courante est pour les forfaits mobiles limités. En
effet, Opus permet d'encoder à faible débit avec une meilleure qualité que le MP3 (par exemple,
Opus @ 96 kbps au lieu de MP3 @ 160 kbps). Notez que le format demandé par l'application elle-même
aura toujours la priorité sur cette option. si Opus est choisi mais que l'app demande du MP3, MP3
sera utilisé.

[![05](/img/post/release-of-v2-2-0/05-thumb.png#center)](/img/post/release-of-v2-2-0/05.png)

Ces deux options sont uniquement affichées en
[mode debug](https://doc.koozic.net/settings/debug.html) car elles ne sont utiles que dans des cas
très particuliers.

# Traduction en espagnol

Un gentil contributeur a été a la traduction complète de l'application en espagnol. Un grand merci à
lui ! Nous avons également changé notre outil de traduction pour passer à
[Transifex](https://www.transifex.com/koozic/koozic/). Les contributions sont appréciées, et si
votre langue ne fait pas partie des langues proposées, n'hésitez pas à ouvrir un
[problème Github](https://github.com/docmarty84/koozic/issues).

# Autres nouveautés

Suite à la
[dépréciation par LastFM](https://getsatisfaction.com/lastfm/topics/api-announcement-dac8oefw5vrxq)
de la récupération des images d'artistes, nous utilisont à présent les images Spotify.
L'inconvénient est que si l'artiste n'est pas présent sur Spotify, aucune image ne sera disponible.

De plus, de multiples améliorations de performances ont été introduites, en particulier
l'utilisation mémoire durant l'analyse des répertoires.

# Mise-à-jour d'une installation existante

La v2.2.0 est compatible avec la version précédente v2.1.0. Pour mettre à jour :

```
wget https://raw.githubusercontent.com/DocMarty84/koozic_install/v2/koozic_install.py -O koozic_install.py
sudo python3 koozic_install.py upgrade
```

### Docker

1.  Arrêter KooZic : `docker-compose stop`
2.  Télécharger la v2.2.0 sur
    [la page de téléchargement](https://github.com/DocMarty84/koozic/releases/download/v2.2.0/koozic-v2.2.0-docker.tar.gz)
3.  Copier le `Dockerfile` et `entrypoint.sh` de la v2.2.0 vers le répertoire où la v2.1.0 a été
    extraite.
4.  Construire : `docker-compose build` > une nouvelle version de KooZic est téléchargée.
5.  Démarrer : `docker-compose up -d`

N'hésitez pas à soumettre un [problème Github](https://github.com/docmarty84/koozic/issues) si
nécessaire !
