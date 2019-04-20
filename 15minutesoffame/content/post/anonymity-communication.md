+++
title = "Sécuriser ses échanges"
date = "2009-05-27T03:00:00+02:00"
tags = ["anonymat"]
archives = "2009"
type = "article"
+++

Dans l'[article précédent](http://15minutesoffame.be/nico/blog2/?article10/proteger-ses-donnees-personnelles),
nous avons vu comment il était possible de protéger ses données personnelles grâce à TrueCrypt. Nous
allons à présent voir comment il est possible de protéger des données à échanger grâce à la
[cryptographie asymétrique](http://15minutesoffame.be/nico/blog/2009/05/quelques-elements-de-cryptographie/).
Un récent article de
[®om](http://blog.rom1v.com/2009/05/gnupg-chiffrer-et-signer-sous-ubuntu-pour-les-nuls/) est très
bien mais peut-être trop orienté Ubuntu. Je tenterai donc d'apporter quelques éléments nouveaux.

# Pourquoi chiffrer ses communications ?

Avant d'aller plus loin, posons nous la question : pourquoi donc chiffrer un e-mail, vu que votre
messagerie dispose d'un mot de passe et que vous n'avez rien à cacher ? Tout comme un courrier
classique, un e-mail risque de voyager entre plusieurs intermédiaires (au minimum, les serveurs
mails). L'inconvénient est qu'un e-mail classique peut être facilement lu :

*   Par le serveur mail lui-même. Au minimum, votre serveur mail dispose d'un anti-spam : le contenu
    sera donc analysé pour vérifier que certains mots-clés ne s'y trouvent pas. Google, entre
    autres, étend ce principe pour vous proposer de la publicité ciblée. Chaque mail reçu avec GMail
    est donc analysé pour tracer votre portrait.
*   Les [éventuels mouchards](http://www.numerama.com/magazine/12976-Loppsi-les-mouchards-sous-l-autorite-d-un-juge-en-voie-de-disparition.html)
    du gouvernements français. Hé oui, il semble que la réalité dépasse la fiction...
*   Votre FAI, si la connexion à votre webmail n'est pas chiffrée.
*   Un petit malin qui se serait infiltré sur votre réseau... Même si c'est le moins probable,
    l'espionnage industriel n'est pas un mythe.

Contrairement à une lettre placée dans une enveloppe, le contenu d'un e-mail peut donc être
_relativement_ facilement accessible. Il ne faut pas non plus sombrer dans la paranoïa, car dans la
vie courante de nombreuses traces sont également semées ça et là. Pensez donc aux diverses cartes de
fidélité des grands magasins (Monsieur Auchan sait tout de vous, de vos habitudes alimentaires à
votre marque de PQ triple épaisseur préférée), aux inscriptions diverses, abonnements... Sans
compter que tous ces fichiers clients s'échangent. Inutile donc de vouloir chiffrer le moindre
échange si, en parallèle, vous semez des traces à tout va. Certains sujets mériteraient, par contre,
une attention plus particulière. Monsieur Google ou Microsoft vous inspire-t-il suffisamment
confiance pour que vous lui racontiez vos problèmes sentimentaux, vos problèmes de santé ou la
dernière crasse que votre patron vous a faite ? A vous d'utiliser ces services "gratuits" en
connaissance de cause...

Un point n'a cependant pas été abordé, les erreurs humaines (que celui qui n'a jamais envoyé un
e-mail par erreur me jette la première bière ;-) ). Dans le domaine industriel, cela pourrait être
très problématique : envoyer un rapport confidentiel à un concurrent, fournir des résultats
financiers à de mauvaises personnes, une blague de cul bien grasse à la vieille secrétaire
acariâtre...

Il n'est donc pas nécessaire d'avoir quelque chose à se reprocher pour utiliser le chiffrement. De
toutes façons, vous êtes légalement tenus de fournir votre clé de déchiffrement aux autorités, sinon
vous risquez la peine maximale du délit dont on vous accuse.

# Le principe de base de la cryptographie asymétrique

La cryptographie asymétrique se base sur l'utilisation d'une paire de clé, composée d'une clé
publique et d'une clé privée. La clé publique est utilisée pour chiffrer des données, et la clé
privée pour les déchiffrer ansi que pour les signer (de manière à en assurer la provenance). Ces
deux clés étant mathématiquement liées, à chaque clé publique ne correspond qu'une seule clé privée.
Cependant, déduire la clé privée à partir de la clé publique est excessivement long (plusieurs
centaines voire milliers d'années), ce qui assure une très bonne sécurité.

Prenons un petit exemple : Bob désire envoyer des données secrètes à Alice et Jack, mais il veut pas
qu'Alice ait accès aux informations envoyées à Jack, et inversement. En premier lieu, Bob, Alice et
Jack génèrent chacun une paire de clé. Chacun s'échange ensuite ses clés publiques respectives. Pour
envoyer un message à Alice, voilà ce qui va se passer :

1.  Bob chiffre le message grâce à la clé publique d'Alice
2.  Bob signe le message grâce à sa propre clé privée
3.  Bob envoie le message à Alice
4.  Alice vérifie la signature du message grâce à la clé publique de Bob, et s'assure qu'il en est
bien l'auteur
5.  Alice déchiffre le message grâce à sa clé privée

Supposons que Jack soit une enflure et qu'il parvienne à intercepter le message de Bob. Bien qu'il
soit en possession de la clé publique d'Alice, il ne pourra rien en faire car déduire la clé privée
d'Alice à partir de sa clé publique est très long. Bob et Alice peuvent donc communiquer sans
risques.

Nous utiliserons GnuPG dans le texte qui suit, qui est une implémentation libre et open source
d'OpenPGP. Notez que GnuPG utilise une méthode de chiffrement hybride. En fait, le chiffrement
asymétrique s'applique à une clé symétrique qui est utilisée pour le chiffrement des données.

# Gestion de clés sous Linux

Avant tout chose, il sera nécessaire d'installer Seahorse ainsi que gnupg grâce à votre gestionnaire
de paquets.

## Générer une paire de clés

Lancez tout d'abord Seahorse (il est possible qu'il se trouve sous l'appellation "Applications →
Accessoires → Mots de passe et clés de chiffrement" sous Gnome). Pour générer une paire de clés,
cliquez tout d'abord sur Clé → Créer une nouvelle clé, et choisir "Clé PGP". Entrer ensuite vos
informations personnelles :

[![01](/img/post/anonymity-communication/01-thumb.png#center)](/img/post/anonymity-communication/01.png)

A tout hasard, je décoche "N'expire jamais" et je choisis une clé de 4096 bits (sécurité maximale).
Entrez ensuite votre passphrase, qui n'est rien d'autre qu'un long mot de passe. La paire de clé
générée apparait dans votre liste de clés :

[![02](/img/post/anonymity-communication/02-thumb.png#center)](/img/post/anonymity-communication/02.png)

L'identifiant de la clé permettra d'identifier votre clé lorsque vous la déposerez sur un serveur de
clés (voir plus loin). Dans les propriétés de la clé (Clic droit → Propriétés), vous pourrez changer
la passphrase ainsi que la date d'expiration. Sous l'onglet détails, vous trouverez également
l'empreinte unique de votre clé (chez moi : 5ED6 EE4A 8514 6203 A01E 688F 28CD 661C C961 9A0F).
Cette empreinte vous permettra d'identifier univoquement votre clé. En effet, il est tout à fait
possible de générer une clé avec des informations identiques (même utilisateur, adresse e-mail et
commentaire).

[![03](/img/post/anonymity-communication/03-thumb.png#center)](/img/post/anonymity-communication/03.png)

Nous constatons que la clé que la clé est en fait composée de deux sous-clés. La clé DSA est
utilisée pour signer le message (à l'origine, DSA était destiné uniquement à la signature) et
ElGamal est utilisée pour le chiffrement.

## Échanger sa clé publique

Maintenant que nous avons créé notre paire de clé, il va falloir échanger notre clé publique. Pour
cela, deux solutions : copier-coller ou sauvegarder la clé publique, ou l'envoyer sur un serveur de
clés.

Si on ne désire pas utiliser un serveur de clé, il suffit d'un clic droit sur une clé et de
choisir :

*   Copier, pour la copier dans le presse papier.
*   Exporter la clé publique, pour créer un fichier contenant la clé.

Rien de plus simple que de la transmettre à son correspondant (e-mail, IM...).

L'utilisation d'un serveur de clé peut cependant être utile car une clé peut être sujette à
modification. Il est possible de modifier la date d'expiration, de révoquer (annuler) la clé ou
d'ajouter sa signature à une clé publique. En synchronisant son trousseau de clé avec le serveur,
vos correspondant seront mis au courant des éventuelles modifications. Pour cela, il suffit de
choisir "Synchroniser et publier des clés" lors du clic droit. Vous pouvez faire un tour du côté des
serveurs de clé. Personnellement, je n'ai jamais eu de problème avec le serveur du MIT :
hkp://pgp.mit.edu:11371.

[![04](/img/post/anonymity-communication/04-thumb.png#center)](/img/post/anonymity-communication/04.png)

Votre correspondant pourra chercher la clé grâce à la fonction de recherche, disponible en cliquant
sur Distant → Chercher des clés distantes. La recherche s'effectue sur le nom, l'adresse mail ou le
commentaire. Un simple Clic droit → Importer et la clé apparaitra dans l'onglet "Autres clés obtenues".

## Signer une clé publique

Signer une clé publique reçue n'est pas un acte anodin : ceci est censé assurer que vous êtes sûr de
la provenance de la clé. Reprenons notre exemple avec Bob, Alice et Jack. Supposons qu'Alice et
Jack ne se connaissent pas, et que Bob connaisse tout le monde.

*   Bob et Alice échangent leur clé, chacun s'assure qu'elle est correcte et la signe grâce à sa clé
    privée.
*   Bob et Jack échangent leur clé, chacun s'assure qu'elle est correcte et la signe grâce à sa clé
    privée.
*   Jack désire communiquer avec Alice, mais ne la connait pas. Si il récupère la clé d'Alice sur un
    serveur de clé, il constatera qu'elle a été signée par une personne de confiance, c'est-à-dire
    Bob. Il est donc sûr que cette clé est la bonne.

Pour signer une clé d'un correspondant (apparaissant dans l'onglet "Autres clés obtenues"), il
suffit de faire un Clic droit → Signer la clé et de choisir quelle clé privée sera utilisée pour la
signer (ainsi que le niveau de confiance).

## Application : chiffrer/signer ou déchiffrer un fichier quelconque

Haaa, enfin une petite application ! Chiffrer un fichier n'est pas possible depuis Seahorse, et en
fonction de votre environnement de bureau, cela peut être différent. Pour Gnome, un simple clic
droit sur le fichier vous donne accès aux options voulues (voir l'
[article de ®om](http://blog.rom1v.com/2009/05/gnupg-chiffrer-et-signer-sous-ubuntu-pour-les-nuls/)).
C'est donc extrêmement simple. Si vous voulez une méthode universelle, faites donc un petit tour
plus bas dans la section ocncernant la ligne de commande.

# Gestion de clés sous Windows

GnuPG est [disponible sous Windows](http://www.gpg4win.org/). Après installation, deux interfaces de
gestion des clés sont disponibles : WinPT et GPA. Le principe est identique à Seahorse, donc pas de
captures d'écrans :-D

Pour générer une clé dans le cas de GPA, il faut tout d'abord, cliquer sur Edit → Preferences et
cocher "Show advanced mode". Ensuite, il suffit de générer une clé en cliquant sur Keys → New Key.
Pour une raison que j'ignore, il n'est pas possible de générer une clé de taille supérieure à 2048
bits.

Dans le cas de WinPT, il vous obligera à créer une clé au premier démarrage, sans pouvoir spécifier
d'options. Pour spécifier les options, il suffira de générer une autre clé à partir du menu Key →
New → Expert.

# Chiffrer un e-mail

Le très intéressant blog de [®om](http://blog.rom1v.com/2009/05/gnupg-chiffrer-et-signer-sous-ubuntu-pour-les-nuls/)
propose une solution pour Evolution, client mail par défaut d'Ubuntu. Penchons-nous sur Thunderbird
et FireGPG.

## Thunderbird

Thunderbird n'intègre pas par défaut le chiffrement PGP, mais il est possible de lui ajouter cette
fonctionnalité via Enigmail. Cette extension est sûrement disponible dans les dépôts de votre
distribution Linux, mais également sur le
[site officel des modules](https://addons.mozilla.org/fr/thunderbird/addon/71) de Thunderbird. Outre
les fonctions basiques que sont le chiffrement, la signature et le déchiffrement d'un e-mail,
Enigmail vous permet de gérer votre liste de contact de façon à ce que la bonne clé soit
automatiquement sélectionnée en fonction du destinataire.

Après installation, le menu OpenPGP apparaitra dans la fenêtre principale de Thunderbird. Un rapide
coup d'œil dans Gestion de clés et vous trouverez vos clés privées et publiques. En fait, ce
gestionnaire vous permet de faire la majorité des opérations classiques (création, suppression,
exportation, modification...).

Dans les paramètres des comptes (Édition → Paramètres des comptes), il est possible de configurer
l'utilisation par défaut d'Enigmail pour chaque compte e-mail : clé privée, options cochées par
défaut...

[![05](/img/post/anonymity-communication/05-thumb.png#center)](/img/post/anonymity-communication/05.png)
[![06](/img/post/anonymity-communication/06-thumb.png#center)](/img/post/anonymity-communication/06.png)

Dans les préférences d'Enigmail (OpenPGP → Préférences), cochez Mode expert dans l'onglet Général,
et vous aurez accès à une gestion fine des clés via l'onglet Sélection clef. Si vous cliquez sur
Mofifier les règles, vous pourrez définir manuellement des règles d'envoi en choisissant les
destinataire et la clé à utiliser. Notez qu'Enigmail peut également utiliser les adresses e-mails
spécifiées dans les identifiants des clés publiques. Par exemple, si l'adresse azerty@exemple.com
est indiquée dans une des clés publiques, Enigmail utilisera automatiquement cette clé lorsqu'un
e-mail sera envoyé à azerty@exemple.com.

[![07](/img/post/anonymity-communication/07-thumb.png#center)](/img/post/anonymity-communication/07.png)
[![08](/img/post/anonymity-communication/08-thumb.png#center)](/img/post/anonymity-communication/08.png)

Pour envoyer un mail chiffré et signé, il suffit de cocher les cases adéquates lors de la rédaction.
Si le destinataire n'apparait ni dans les règles manuelles, ni dans les clés publiques, il vous sera
demandé de choisir une clef. Sinon, les règles définies auparavant seront appliquées.

[![09](/img/post/anonymity-communication/09-thumb.png#center)](/img/post/anonymity-communication/09.png)

## FireGPG

[FireGPG](https://addons.mozilla.org/fr/firefox/addon/4645) est une extension intégrant le
chiffrement et la signature de messages pour Firefox. Ceci se révèle très utile lors de
l'utilisation de divers webmails. Il suffit alors de sélectionner le texte à chiffrer/signer ou
déchiffrer, et de choisir l'action désirée dans le menu FireGPG apparaissant lors du clic droit.
FireGPG s'intègre avec Gmail, et de manière générale repère les textes chiffrés dans une page web
pour y ajouter un bouton de déchiffrement. En outre, un éditeur est disponible, ce qui peut être
pratique si des brouillons sont enregistrés à intervalles réguliers (l'extension les désactive par
défaut sur GMail).

Dans l'éditeur, tapez votre texte puis choisissez Chiffrer et signer. La clé publique de chiffrement
puis la clé privée de signature vous seront demandées. Cette extension est très simple d'utilisation
tout en restant très puissante. Elle permet également le chiffrement symétrique d'un message.

# Chiffrer ses conversation IM

Tout comme les e-mails, les conversations utilisant les messageries instantanées (MSN, GTalk, AIM,
ICQ, Jabber...) sont susceptibles d'être interceptées. Nous verrons ici comment il est possible
d'utiliser les chiffrement PGP pour les chiffrer.

## Pourquoi ne pas choisir MSN ?

Avant de vouloir chiffrer ses communications, il vaudrait mieux utiliser un logiciel et un protocole
sûr, n'est-ce pas ?

Si vous êtes un adepte d'MSN, vous avez surement déjà rencontré une personne vous envoyant des
messages automatiquement, signe qu'un virus avait infecté son logiciel. Vous avez peut-être
également connu [la censure](http://nsa06.casimages.com/img/2009/03/09/090309065324613392.png) de
Microsoft, censée vous protéger des virus mais prouvant que vos messages sont scannés en permanence.
Si ce n'est pas le cas, posez-vous tout de même la question de savoir si un protocole aussi fermé
que celui d'MSN (donc faisant potentiellement transiter des informations supplémentaires inconnues)
est bien approprié pour des discussions sécurisées. Si toutes les informations passent en plus par
les serveurs de Microsoft (vive la centralisation :/ ), la réponse est non.

Nettement moins connu, le protocole Jabber est :

*   open-source, donc gage de transparence
*   libre, donc l'utilisation de programmes différents est facilitée (utilisé entre autre par Google
    Talk)
*   décentralisé, donc assez facile d'éparpiller les traces laissées sur le réseau. Il est même
    possible de monter son propre serveur Jabber chez soi.

De plus, certains logiciels permettent l'utilisation du chiffrement PGP, de manière totalement
transparente une fois que les clés publiques ont été échangées. Il suffit de créer un compte sur un
serveur quelconque, par exemple celui de
l'[APINC](http://im.apinc.org/inscription/?apinc=1&server=im.apinc.org). Aucune information
confidentielle ne vous sera demandée, juste un nom d'utilisateur et un mot de passe.

## Gajim

Choix le plus judicieux pour le protocole Jabber quand on tourne sous Linux,
[Gajim](http://www.gajim.org/) intègre par défaut la possibilité de chiffrer ses conversations.
Après installation (disponible par défaut dans la majorité des distributions Linux) et ajout de
contacts, faire un clic droit sur le contact désiré et choisir Gérer le Contact → Assigner une clé
OpenPGP pour désigner la clé publique voulue. Le choix de la clé privée se fait dans Édition →
Comptes, onglet Informations personnelles.

Pour chiffrer une conversation, aller dans les options avancées (dernier bouton de la fenêtre de
conversation), et cochez Activer le chiffrement GPG. Rien de très compliqué dans tout cela, donc pas
de screenshots ;-)

Gajim permet également de chiffrer ses communications en se passant de GPG, via l'option "Activer le
chiffrement de bout-en-bout". Cette méthode est propre à Gagim, et ne fonctionne qu'entre 2 clients
Gajim. De plus, on perd toute la notion de signature.

Sous Windows, Gajim ne supporte pas le chiffrement, il faut donc se tourner vers
[Psi](http://psi-im.org/).

## Psi

[Psi](http://psi-im.org/) est le choix le plus judicieux pour les personnes utilisant Windows, car
il permet d'utiliser le chiffrement GPG. Il est donc possible d'utiliser le chiffrement entre un
client Gajim et un client Psi.

## Pidgin

Pidgin est le client par défaut sous Ubuntu, et a l'avantage d'être multi-protocole. Le plugin
pidgin-encryption est disponible dans les dépôts de la majorité des distributions, ou sur le
[site officiel](http://pidgin-encrypt.sourceforge.net/). Après installation, se rendre dans Outils →
Plugins et cocher Pidgin-Encryption. Dans la fenêtre de conversation, un petit cadenas apparait en
haut à droite pour chiffrer la conversation. L'avantage de l'utilisation de Pidgin est que la
génération ainsi que l'échange de clés se fait de manière automatique. Cette automatisation n'est
cependant pas idéale pour la sécurité des transmissions (les clés sont mises à jour automatiquement,
pas de système de signature...).

# Un petit mot sur S/MIME

[S/MIME](http://en.wikipedia.org/wiki/Smime) est une méthode de chiffrement différente de OpenPGP,
fonctionnant sur base de certificats, utilisée pour les e-mails. Ces certificats doivent être
obtenus auprès d'une autorité de certification, et sont souvent payants
([StartSSL](http://www.startssl.com/) en fournit cependant gratuitement). Les inconvénients majeurs
sont :

*   Les clients mails ne supportent pas toujours S/MIME.
*   L'accès d'un webmail à la clé privée peut poser des problèmes de sécurité.
*   S/MIME ne chiffre pas seulement le message, mais également les éventuels malwares.

En bref... Mieux vaut utiliser OpenPGP.

# Annexe : Gestion de clés en ligne de commande (tous les OS)

La ligne de commande de GnuPG est en principe universelle, donc vous pourrez l'utiliser sur
n'importe quel OS. Ce guide ne se veut pas exhaustif, mais donnera juste les exemples les plus
utilisés. Pour plus d'informations, la
[documentation du site d'Ubuntu-fr](http://doc.ubuntu-fr.org/gnupg) est très bien faite. Et
toujours, bien sûr, le [manuel](http://www.gnupg.org/gph/fr/manual.html) ainsi que la commande man !

## Générer une paire de clés

La génération de la clé est extrêmement simple : il suffit d'utiliser la commande `gpg --gen-key`.
Des questions identiques vous seront posées :

```
[wacken@desktop ~]$ gpg --gen-key
gpg (GnuPG) 1.4.9; Copyright (C) 2008 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Sélectionnez le type de clé désiré:
(1) DSA et Elgamal (par défaut)
(2) DSA (signature seule)
(5) RSA (signature seule)
Votre choix ? 1
La paire de clés DSA fera 1024 bits.
les clés ELG-E peuvent faire entre 1024 et 4096 bits de longueur.
Quelle taille de clé désirez-vous ? (2048) 4096
La taille demandée est 4096 bits
Spécifiez combien de temps cette clé devrait être valide.
0 = la clé n'expire pas
<n>  = la clé expire dans n jours
<n>w = la clé expire dans n semaines

<n>m = la clé expire dans n mois
<n>y = la clé expire dans n années
La clé est valide pour ? (0) 2y
La clé expire le lun. 23 mai 2011 16:45:23 CEST
Est-ce correct ? (o/N) o
Vous avez besoin d'un nom d'utilisateur pour identifier votre clé; le
programme le construit à partir du nom réel, d'un commentaire et d'une
adresse e-mail de cette manière:
"Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"
Nom réel: Wacken2
Adresse e-mail: wacken@exemple.com

Commentaire: Ceci est un autre exemple
Vous avez sélectionné ce nom d'utilisateur:
"Wacken2 (Ceci est un exemple) <wacken@exemple.com>"
Changer le (N)om, le (C)ommentaire, l'(E)-mail ou (O)K/(Q)uitter ? o
Vous avez besoin d'une phrase de passe pour protéger votre clé
secrète.
```

Il vous sera également demandé de taper au clavier pour augmenter le caractère aléatoire de clé.
Pour voir la liste des clés, un simple `gpg --list-key` :

```
[wacken@desktop ~]$ gpg --list-key
/home/wacken/.gnupg/pubring.gpg
--------------------------------
pub   1024D/C9619A0F 2009-05-23
uid                  Wacken (Ceci est un exemple) <wacken@exemple.com>
sub   4096g/86261ABE 2009-05-23

pub   1024D/9B06A561 2009-05-23 [expire: 2011-05-23]
uid                  Wacken2 (Ceci est un autre exemple) <wacken@exemple.com>

sub   4096g/44981553 2009-05-23 [expire: 2011-05-23]
```

Nos deux clés apparaissent comme on pouvait s'y attendre ;-)

## Échanger sa clé publique

Pour exporter une clé publique de Wacken dans le fichier `wacken_key.asc` :

```
[wacken@desktop ~]$ gpg --armor --export Wacken > wacken_key.asc
```

Il est également possible d'utiliser le numéro de la clé, dans notre cas :

```
[wacken@desktop ~]$ gpg --armor --export C9619A0F > wacken_key.asc
```

Exporter cette clé sur le serveur du MIT (numéro de la clé indispensable) :

```
[wacken@desktop ~]$ gpg --keyserver hkp://pgp.mit.edu:11371 --send-key C9619A0F
```

Pour importer une clé reçue par e-mail :

```
[wacken@desktop ~]$ gpg --import wacken_key.asc
```

Pour rechercher une clé (contenant le mot "stallman") sur un serveur :

```
[wacken@desktop ~]$ gpg --keyserver hkp://pgp.mit.edu:11371 --search-keys stallman
gpg: recherche de "stallman" du serveur hkp pgp.mit.edu
(1)    Atanu Datta (Stallman rocks) <lfyedit2@efyindia.com>

      1024 bit DSA key 89F2AFE2, créé: 2008-10-07
(2)    Richard Stallman (For Jabber) <richard.stallman@jabber.org>
      1024 bit DSA key A925536A, créé: 2008-07-26
(3)    Richard Stallman (Lots of flavour in an old cock) <richardstall815@gma
      1024 bit DSA key 373D44AF, créé: 2008-07-26
(4)    Nick Stallman <nick@nickstallman.net>
      1024 bit DSA key 358F2FE1, créé: 2007-03-13
(5)    James Martin (I heart Stallman) <jamie@jamescmartin.net>
      1024 bit DSA key AFB730F2, créé: 2004-06-22
(6)    Tim Stallman <timothy.stallman@ngc.com>
      1024 bit DSA key 8EC33185, créé: 2003-06-25
(7)    victorm (VMMB) <v.munoz@wanadoo.es>
    Frodo L. Stallman <fls@nic.nac.wdyn.de>

    Víctor Manuel Muñoz Berti <v.munoz@wanadoo.es>
    Víctor Manuel Muñoz Berti <v.munoz@telefonica.net>
    Víctor Manuel Muñoz Berti <victorm@matematicas.net>
    Víctor Manuel Muñoz Berti <frodolstallman@gmail.com>
    Frodo L. Stallman (a.k.a. victorm) <fls@nic-nac-project.de>
    Víctor Manuel Muñoz Berti (victorm) <victorm@socios.linuca.org>

      1024 bit DSA key 50483643, créé: 2003-05-02
Entrez le(s) nombre(s), S)uivant, ou Q)uitter >
```

On entre alors le numéro de la clé voulue pour l'importer.

Finalement, pour supprimer une clé :

```
gpg --delete-keys <identifiant>
```

## Signer une clé publique

Premièrement, repérer l'identifiant de la clé de chiffrement du correspondant et l'identifiant de la
clé de signature de l'expéditeur (si on a plusieurs clés privées) grâce à `gpg --list-key` :

```
[wacken@desktop ~]$ gpg --list-key
/home/wacken/.gnupg/pubring.gpg
--------------------------------
pub   1024D/C9619A0F 2009-05-23
uid                  Wacken (Ceci est un exemple) <wacken@exemple.com>
sub   4096g/86261ABE 2009-05-23

pub   1024D/9B06A561 2009-05-23 [expire: 2011-05-23]
uid                  Wacken2 (Ceci est un autre exemple) <wacken@exemple.com>
sub   4096g/44981553 2009-05-23 [expire: 2011-05-23]

pub   1024D/11F63C51 2002-02-28
uid                  Jamie Cameron <jcameron@webmin.com>
sub   1024g/1B24BE83 2002-02-28
```

Si nous voulons signer la clé de de Jamie Cameron avec notre clé privée Wacken :

```
[wacken@desktop ~]$ gpg -u Wacken --edit-key Jamie
gpg (GnuPG) 1.4.9; Copyright (C) 2008 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

pub  1024D/11F63C51  créé: 2002-02-28  expire: jamais      utilisation: SCA
                      confiance: inconnu       validité: inconnu
sub  1024g/1B24BE83  créé: 2002-02-28  expire: jamais      utilisation: E
[ inconnue] (1). Jamie Cameron <jcameron@webmin.com>

Commande> sign

pub  1024D/11F63C51  créé: 2002-02-28  expire: jamais      utilisation: SCA
                      confiance: inconnu       validité: inconnu
 Empreinte de la clé principale: 1719 003A CE3E 5A41 E2DE  70DF D97A 3AE9 11F6 3C51

     Jamie Cameron <jcameron@webmin.com>

Etes-vous vraiment sûr(e) que vous voulez signer cette clé
avec votre clé "Wacken (Ceci est un exemple) <wacken@exemple.com>" (C9619A0F)

Signer réellement ? (o/N)o
```

Dans le cas où vous auriez plusieurs clé avec le même identifiant, vous pouvez utiliser le numéro de
la clé. Notre exemple deviendrait alors :

```
[wacken@desktop ~]$ gpg -u C9619A0F --edit-key 11F63C51
```

Encore une fois, pas bien compliqué !

## Application : chiffrer/signer ou déchiffrer un fichier quelconque

Comme précédemment, repérer l'identifiant de la clé de chiffrement du correspondant et l'identifiant
de la clé de signature de l'expéditeur (si on a plusieurs clés privées) grâce à `gpg --list-key`.
Pour chiffrer et signer le fichier rapport_secret.pdf :

```
gpg -r Jamie -u Wacken -e -s rapport_secret.pdf
```

`-e` pour chiffrer, `-s` pour signer. Si `-s` n'est pas spécifié, `-u` est inutile. Le fichier
rapport_secret.pdf.gpg sera créé. Pour le déchiffrer :

```
gpg -d rapport_secret.pdf.gpg > rapport_déchiffré.pdf
```

La passphrase vous sera demandée.

Un jeu d'enfant !

**A suivre, partie 4 : [Sécuriser et rendre anonyme sa navigation](http://15minutesoffame.be/nico/blog/2009/06/securiser-et-rendre-anonyme-sa-navigation/).**
