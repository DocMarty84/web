+++
title = "Protéger ses données personnelles"
date = "2009-05-22T03:00:00+02:00"
tags = ["anonymat"]
archives = "2009"
type = "article"
+++

Avant de se lancer dans la sécurisation de ses communications Internet, nous allons voir comment
protéger au mieux les données présentes sur votre ordinateur, votre disque dur externe ou votre clé
USB. La première partie de cet article sera consacrée aux bonnes habitudes à prendre, et la seconde
au chiffrement de vos données.

## Le B-A BA de la sécurité

Tout comme il est ridicule d'avoir un coffre-fort blindé quintuple épaisseur à triple serrure et
reconnaissance rectale exposé dans son jardin, il est nécessaire de sécuriser un tant soit peu son
PC ainsi que son réseau avant de vouloir chiffrer ses données. Quelques conseils simples, pourtant
méconnus voire ignorés, permettent déjà d'atteindre un niveau de sécurité non négligeable.

### Utiliser un navigateur Internet sécurisé

S'il est bien un domaine ou Microsoft ne brille pas, c'est bien la sécurité. En particulier Internet
Explorer, son navigateur intégré, s'est souvent révélé être une véritable passoire à virus, chevaux
de Troie, spywares et autre cochonneries. Bien que Microsoft maintienne mordicus, à chaque nouvelle
version, que son navigateur est le "plus sûr du monde car on a retenu la leçon de la version
précédente", force est de constater que les scénarios se suivent et se ressemblent. On pourra sortir
toutes études qu'on veut comparant le nombre de failles de sécurités, l'important n'est pas le
nombre de failles mais la vitesse de correction de celles-ci. Dans ce domaine, un logiciel
open-source est bien souvent nettement supérieur à un logiciel propriétaire. Utiliser, par exemple,
[Mozilla Firefox](http://www.mozilla-europe.org/fr/firefox/) est donc une première étape dans la
sécurisation de son PC. De plus, celui-ci permet l'utilisation de
[nombreux plugins](https://addons.mozilla.org/fr/firefox/) qui décuplent ses capacités. Citons, par
exemple :

*   [Adblock Plus](https://addons.mozilla.org/fr/firefox/addon/1865), pour en finir avec la
    publicité agressive
*   [CustomizeGoogle](https://addons.mozilla.org/fr/firefox/addon/743), pour améliorer l'utilisation
    de Google (notamment rendre anonyme le cookie de Google, pour éviter que le géant ne trace un
    profil sur vous grâce à vos recherches)
*   [Flashblock](https://addons.mozilla.org/fr/firefox/addon/433), pour bloquer le démarrage
    automatique des animations Flash qui alourdissent la navigation

Et j'en passe...

### Utiliser un client mail sécurisé

Si l'utilisation des webmails (interface web permettant d'avoir accès à ses mails, comme GMail ou
Hotmail) est de plus en plus important, de nombreuses personnes utilisent encore un client mail
comme Outlook. Ceux-ci permettent en effet de gérer plusieurs comptes facilement, sans devoir
visiter chaque webmail séparément. Là encore, l'utilisation d'un client mail comme
[Mozilla Thunderbird](http://www.mozilla-europe.org/fr/products/thunderbird/) est un gage de
sécurité et de modularité supplémentaire grâce aux
[nombreux plugins](https://addons.mozilla.org/fr/thunderbird) disponibles.

### Utiliser un antivirus. A jour...

Si, pour une raison ou une autre, vous êtes toujours sous Windows et que vous n'avez pas
[sauté le pas](http://15minutesoffame.be/nico/blog/category/informatique/passer_a_ubuntu-informatique/),
vous avez surement installé un antivirus. Mais est-il à jour ? En effet, de nouveaux virus
apparaissent chaque jour, et il est nécessaire que la base de données soit à jour. Un antivirus ne
vous empêche pas de faire attention sur ce que vous cliquez (pièces jointes dans les mails, sites
peu fréquentables, etc.). De manière générale, il faut appliquer la règle suivante : si c'est trop
beau, c'est qu'il y a une couille.

### Des mots de passes de taille correcte

Chaque inscription à un site requiert l'utilisation d'un mot de passe. Utilisez des mots de passe
d'au minimum 6 caractères, en utilisant des majuscules, des chiffres et des caractères spéciaux (par
exemple &@#§^”,;:?.=+%£-ÙÇÉÈÏÎÛÜAÂÄ...). Éviter les mots de passe du genre "pierre1976" ou
"Chris06", bien trop simples à deviner. N'utilisez pas le même mot de passe pour votre compte MSN et
votre compte Paypal, l'idéal étant d'utiliser un mot de passe différent pour chaque site. Impossible
de tous les retenir ? En effet, mais rien ne vous empêche de les stocker dans un fichier...
chiffré ! Nous y reviendrons par la suite.

### Sécuriser son WiFi

Pour des raisons de facilité de configuration, le WiFi des routeurs ou les box sont activés sans clé
de connexion, au mieux avec une clé WEP. Ceci est clairement insuffisant, et un voisin mal
intentionné pourra sans problème infiltrer votre réseau. Au mieux il se contentera de surfer et de
télécharger sur votre compte, au pire il ira fouiller le contenu de vos PC s'ils ne sont pas
protégés. Utilisez donc une clé WAP aléatoire de taille maximale (63 caractères). Si vous êtes en
manque d'inspiration, des
[générateurs de clés](http://www.skyminds.net/outils/generateur-de-cles-wpa-securisees/) sont
disponibles sur la toile.

### Supprimer efficacement un fichier

Lorsqu'on supprime un fichier, les données ne sont pas réellement supprimées du disque dur. En
réalité, l'espace occupé par ces données est indiqué comme libre, mais les données sont toujours
présentes. Sous Linux, la commande shred permet de détruire efficacement un fichier :

```
shred -n 35 -z -u fichier
```

Ceci aura pour effet de :

*   remplacer 35 fois les données du fichier par des déchets (`-n 35`)
*   remplacer ces données par des zéros pour masquer le déchiquettage (`-z`)
*   tronquer et supprimer le fichier (`-u`)

Cette méthode est déjà plus efficace ;-)

## TrueCrypt, le couteau suisse du chiffrement

Il existe principalement 3 possibilités de chiffrement : chiffer un fichier particulier, utiliser un
conteneur chiffré et chiffrer une partition complète. TrueCrypt est capable d'effectuer ces deux
dernières tâches. TrueCrypt est un programme libre, et est disponible
[ici](http://www.truecrypt.org/downloads). Il est disponible sous Windows, Mac OS X et Linux
(paquets disponibles pour OpenSuSE et Ubuntu). L'intérêt de TrueCrypt est qu'il est
multi-plateforme : il est possible de créer un conteneur sous Linux et l'utiliser ensuite sous
Windows ou Mac OS X, par exemple.

### Créer un conteneur chiffré

Le but est de créer un fichier conteneur, une sorte de coffre-fort qui va contenir les fichiers à
protéger. Dans TrueCrypt, cliquer sur Volumes → Create New Volume, puis sélectionner "Create a file
container". Deux choix s'offrent à vous :

1.  Standard TrueCrypt volume : comme son nom l'indique, un simple conteneur chiffré dans lequel on
    stockera les fichiers à protéger.
2.  Hidden TrueCrypt volume : plus subtil, le conteneur caché. Le principe est de créer un gros
    conteneur constitué de deux parties. La première partie (Outer volume) contiendra des faux
    fichiers à protéger, et la seconde les vrais fichiers sensibles. Lorsqu'on accède à la première
    partie grâce à un premier mot de passe, l'espace occupé par les fichiers sensibles est spécifié
    comme étant libre. Si on accède à ce fichier via un autre mot de passe, la partie contenant les
    vrais fichiers sensibles (Hidden volume) apparaitra. Cette méthode est la plus sure, car il est
    absolument impossible de prouver la présence des fichiers sensibles. Ce type de protection n'est
    nécessaire que si vos fichiers sont susceptibles de vous porter préjudice.

[![01](/img/post/anonymity-personal-data/01-thumb.png#center)](/img/post/anonymity-personal-data/01.png)
[![02](/img/post/anonymity-personal-data/02-thumb.png#center)](/img/post/anonymity-personal-data/02.png)

L'étape suivante est de sélectionner l'emplacement et le nom du fichier, si possible il devra passer
inaperçu sur le disque. L'étape suivante consiste à choisir deux paramètres : l'algorithme de
chiffrement et l'algorithme de hachage. L'algorithme de chiffrement (voir
l'[article précédent](http://15minutesoffame.be/nico/blog/2009/05/quelques-elements-de-cryptographie/))
est la fonction mathématique qui sera utilisée pour chiffrer les données. Il est possible d'utiliser
consécutivement 2 ou 3 algorithmes, ce qui augmente la sécurité mais diminue la vitesse d'accès. La
[fonction de hachage](http://fr.wikipedia.org/wiki/Fonction_de_hachage) sera utilisé lors de la
génération d'un nombre aléatoire et de la création de la clé de chiffrement de l'entête (la partie
du fichier qui contient des données propres à TrueCrypt). _A priori_, peu importe la fonction
choisie. La taille du fichier se fait à l'étape suivante. Si vous choisissez un conteneur caché,
prenez soin de spécifier une taille supérieure à la taille de vos fichiers confidentiels, étant
donné que vous devrez y placer des "leurres".

[![03](/img/post/anonymity-personal-data/03-thumb.png#center)](/img/post/anonymity-personal-data/03.png)
[![04](/img/post/anonymity-personal-data/04-thumb.png#center)](/img/post/anonymity-personal-data/04.png)
[![05](/img/post/anonymity-personal-data/05-thumb.png#center)](/img/post/anonymity-personal-data/05.png)


Il vous sera ensuite demandé d'utiliser une phrase de passe, ou _passphrase_. C'est l'équivalent
d'un mot de passe, sauf qu'on vous demande... une phrase ;-) Il est conseillé de choisir une phrase
assez longue avec majuscules, chiffres et caractères spéciaux. Vous avez également la possibilité
d'utiliser des keyfiles. Un keyfile est un fichier quelconque qui sera utilisé en complément de
votre passphrase. Il vous sera donc nécessaire de ne pas perdre, modifier ou supprimer ces fichiers,
car dans le cas contraire vous ne pourrez plus accéder à votre volume chiffré. Notez que si vous
avez choisi un conteneur caché, cette étape est liée à la partie contenant les leurres. Choisissez
donc une passphrase qui sera différente de la passphrase qui servira à cacher vos vraies données
confidentielles.

[![06](/img/post/anonymity-personal-data/06-thumb.png#center)](/img/post/anonymity-personal-data/06.png)
[![07](/img/post/anonymity-personal-data/07-thumb.png#center)](/img/post/anonymity-personal-data/07.png)

Si vous avez choisi un conteneur standard, l'étape suivante est celle du choix du
[formatage](http://fr.wikipedia.org/wiki/Formatage). Si vous ne savez que choisir, prenez FAT.
Ensuite, la clé de chiffrement de l'entête sera générée. Bougez votre souris dans la fenêtre, cela
augmentera le caractère aléatoire de cette clé. Cliquez finalement sur _Format_, et votre conteneur
sandard est créé ! Dans le cas d'un conteneur caché, la prochaine étape consiste à remplir
partiellement le conteneur avec des leurres en cliquant sur _Open Outer Volume_. Quand c'est fait,
appuyez sur _Next_, et vous devrez configurer la partie cachée de la même façon que la partie
contenant des leurres.

[![08](/img/post/anonymity-personal-data/08-thumb.png#center)](/img/post/anonymity-personal-data/08.png)
[![09](/img/post/anonymity-personal-data/09-thumb.png#center)](/img/post/anonymity-personal-data/09.png)
[![10](/img/post/anonymity-personal-data/10-thumb.png#center)](/img/post/anonymity-personal-data/10.png)

C'est fini !

### Monter un conteneur chiffré

Pour monter un conteneur chiffré, rien de plus simple. Il suffit de choisir le fichier puis de
cliquer sur Volumes → Mount Volume, puis d'indiquer votre passphrase ainsi que les éventuels
keyfiles. Votre conteneur apparaitra alors de manière similaire à une clé USB ou un disque dur
externe. Sous Linux, les volumes sont montés par défaut dans /media/truecrypt1. Dans le cas d'un
volume caché, vous avez trois possibilités :

1.  Spécifier la passphrase et les keyfiles de votre partie leurre. La partie faussement
    confidentielle sera montée, et les données confidentielles apparaîtront comme espace vide.
    N'ajoutez aucun fichier à votre conteneur ainsi monté, car vos données confidentielles seraient
    altérées voire détruites.
2.  Spécifier la passphrase et les keyfiles de votre partie cachée. La partie leurre n'apparait pas,
    vous pouvez donc ajouter, modifier ou supprimer des fichiers sans soucis.
3.  Si vous cliquez sur _Options_, vous remarquerez la case _Protect hidden volume when mounting
    outer volume_. Si vous spécifiez la passphrase et les keyfiles de votre partie leurre et que
    vous cochez la case en spécifiant la passphrase et les keyfiles de votre partie cachée, votre
    volume leurre sera monté tout en protégeant vos données cachées. Vous pourrez ajouter, modifier
    ou supprimer des fichiers sans risque de la corrompre.

### Créer une partition chiffrée

Le principe est stictement identique, sauf que vous choisissez "Create a volume within a
partition/device" au début du processus de création. Vous pouvez alors choisir de chiffrer une
partition du disque dur, une clé USB, une carte mémoire, un disque externe... Pour monter le volume,
vous choisirez "Select Device". Quelques précautions à prendre tout de même&nbsp;:

*   Ne chiffrez pas des partitions système, car elles seraient formatées. Il faut créer la partition
    avant d'installer le système, ce que TrueCrypt ne permet pas. Par contre, vous pouvez tout à
    fait chiffrer une partition vide (en ayant préalablement redimensionné les partitions, ou en
    ayant prévu cette éventualité lors de l'installation de votre système).
*   Une clé USB a pour vocation de passer d'un PC à l'autre. TrueCrypt sera donc obligatoire pour la
    lire.

## Cryptsetup, pour les adeptes de la ligne de commande

Si, pour une raison ou pour une autre, vous ne pouvez ou ne voulez pas utiliser TrueCrypt,
Cryptsetup vous permet de faire la même chose en ligne de commande. Cryptsetup se trouve dans les
dépôts de la majorité des distributions. Un très bon tutoriel est disponible sur
[TheGlu's Blog](http://blog.theglu.org/index.php/2007/05/19/cryptsetup-le-couteau-suisse-du-chiffrement-de-partitions/).

Je dois dire que vu la simplicité de TrueCrypt, je n'utilise jamais Cryptsetup.

## Crypter des partitions système

La majorité des distributions Linux vous proposent dès l'installation de chiffrer la partition
`/home`, censée contenir vos documents personnels ainsi que les préférences des différents
programmes. Personnellement, je trouve ça assez inutile car je ne mets aucun document sensible dans
mon `/home`. De plus, je préfère scinder tout ce qui a trait au système des documents. A vous de
voir selon vos habitudes... En pratique, la partition sera déchiffrée au moment où le mot de passe
correspond au login sera donné.

Il est également possible d'avoir un système complètement chiffré, avec une passphrase demandée au
démarrage. Ceci n'est absolument pas recommandé, surtout sur un portable : dans certains pays où la
protection des données personnelles est mal vue, les douaniers pourraient être suspicieux. N'oubliez
pas que si vous avez des choses à cacher, le mieux est de ne pas le crier sur tous les toits ;-)

**À suivre, partie 3 : [sécuriser ses échanges](http://15minutesoffame.be/nico/blog2/?article11/securiser-ses-echanges).**
