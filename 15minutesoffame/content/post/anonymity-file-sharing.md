+++
title = "Anonymat et partage de fichiers"
date = "2009-07-07T03:00:00+02:00"
tags = ["anonymat"]
archives = "2009"
type = "article"
+++

Il est temps à présent de s'attaquer à la partie la plus sensible du sujet : comment partager des
données anonymement. Nous verrons ici qu'il est tout à fait possible d'être anonyme grâce à la
décentralisation et au chiffrement des données. Les réseaux existants (Bittorrent, eDonkey2000,
etc.) n'ayant pas été prévu dans cette optique, il nous faudra en utiliser de nouveaux. Le point
fort de certains logiciels présentés est de combiner un réseau existant avec un réseau décentralisé,
de sorte que les nouveaux réseaux mis en place ne pêchent pas par leur manque de choix.

_Je vous rappelle qu'il est interdit d'utiliser ces logiciels à des fins illégales (piratage,
contrefaçon ou toute autre activité étant considérée hors-la-loi par les lois en vigueur dans votre
pays de résidence). Vous pouvez toutefois les utiliser pour toutes autres utilisations privées, ou
pour télécharger des données libres._

**Il faut être un minimum honnête avec les créateurs qu'on apprécie. Si vous aimez un disque, un
film ou un jeux, achetez-le, allez aux concerts ou au cinéma. Internet permet un accès à une culture
gigantesque, et la moindre des choses est d'encourager ceux qui vous font plaisir. Outre
l'honnêteté, ayez à l'esprit que c'est vous seul qui êtes responsable si un artiste arrête de
produire car il ne gagne plus assez.**

# Bittorrent : OneSwarm, un début prometteur

Mis en place en 2002, le protocole de [peer-to-peer](http://fr.wikipedia.org/wiki/Pair_%C3%A0_pair)
(P2P) [Bittorrent](http://fr.wikipedia.org/wiki/BitTorrent_(protocole)) a connu un succès fulgurant,
notamment pour les raisons suivantes :

*   Vitesses de téléchargement nettement supérieures à celles atteintes par les autres réseaux P2P
    ([quelques explications](http://www.infos-du-net.com/actualite/dossiers/54-bittorrent-p2p-telechargement.html)),
    notamment grâce à un système de "récompense" (plus on envoie vite, plus reçoit vite) assez
    agressif.
*   Nombre de fakes (fichier dont le contenu ne correspond pas au nom) réduit grâce à la
    centralisation des liens sur les trackers et l'impossibilité de renommer un fichier partagé.

De nombreuses distributions Linux ont alors pu être distribuées de cette façon. Le protocole étant
ouvert, de nombreux logiciels clients sont apparus, les plus célèbre étant
[µTorrent](http://www.utorrent.com/), Azureus ([Vuze](http://www.vuze.com/)) ou
[Deluge](http://deluge-torrent.org/). Une première avancée fut l'arrivée du chiffrement des
données : impossible alors pour le FAI de détecter que les données transitant étaient de l'échange
de fichier. Restait un problème majeur : la centralisation des adresses IP des utilisateurs sur les
trackers. Il suffit de se connecter à ce tracker pour connaître toutes les personnes partageant ce
fichier. Qui plus est, de nombreux sites (notamment les trackers privés) gardent des logs assez
complets, permettant de déterminer qui a partagé quoi (voir par exemple l'affaire de
[SnowTiger](http://www.zataz.com/news/19094/snowtiger.html)).

Récemment, [OpenBittorrent](http://openbittorrent.com/) (ainsi que [PublicBT](http://publicbt.com/)
ou encore [Torrage](http://torrage.com/)), un tracker Bittorrent ouvert à tous, a été lancé. L'idée
est tellement simple qu'on se demande pourquoi elle n'a pas été appliquée avant. Habituellement,
lorsque vous recherchez un fichier, vous devez naviguer sur le site du tracker (The Pirate Bay,
Demonoid, SnowTiger...), voire sur un méta-moteur (Btjunkie, Mininova...). L'inconvénient est que le
serveur qui gère les connexions Bittorrent est lié au serveur de recherche de fichiers. Si le
serveur de recherche de fichiers tombe sous le coup de la justice, il entraine celui qui gère les
connexions et les torrents sont perdus. OpenBittorrent est un tracker public, et ne détient aucune
information sur les fichiers dont il se fait le relai. Chacun peut, lorsqu'il crée son torrent,
ajouter le tracker OpenBittorrent et utiliser sa bande passante pour les connexions. Juridiquement
parlant, il est très difficile de condamner ce tracker car :

*   Il ne pourra matériellement pas garder des logs détaillés.
*   Il ne pourra effectuer aucune censure ou filtrage vu qu'il ne détiendra aucune information sur
    les fichiers qui lui sont ajoutés.
*   Il n'est lié d'aucune façon avec les personnes qui l'utilisent.

La partie la plus sensible vis-à-vis de la loi, c'est-à-dire l'indexation des fichiers, est donc
dissociée de tout serveur gérant les connexions. Si un moteur de recherche de fichiers torrent doit
fermer, cela n'aura aucun impact sur la santé du réseau car d'autres moteurs de recherches existent.
En théorie, OpenBittorrent serait donc intouchable juridiquement... De plus, le service d'indexation
des fichiers n'a aucune information sur les données que vous avez partagées. Un "miroir" de
OpenBittorrent a été mis en place, il s'agit de [PublicBT](http://publicbt.org/).

Plus fort que Openbittorrent,
[BitTorrent Hydra](http://torrentfreak.com/bittorrent-hydra-anonymous-hidden-tracker-via-tor-090725/)
est un tracker ouvert qui utilise le réseau Tor pour faire transiter les requêtes. Grâce à
l'anonymat fournit par Tor, il est impossible de savoir où se situe ce tracker. Attention, cela
fournit un anonymat au tracker, pas aux utilisateurs.

Notons aussi l'existence de proxys spécialisés dans le trafic Bittorrent, comme
[superchargemytorrent](http://superchargemytorrent.com/). Moyennant quelques euros, le serveur
servira de passerelle pour vos téléchargements, chiffrant par la même occasion l'entièreté du flux.
Il suffit de configurer le proxy dans les paramètres de votre client Bittorrent.

Lancé récemment, [OneSwarm](http://oneswarm.cs.washington.edu/) est un logiciel libre basé sur
Azureus. Entièrement compatible avec le réseau Bittorrent, il utilise également son propre réseau
totalement chiffré et décentralisé. Un fichier téléchargé sur le réseau Bittorrent classique sera
automatiquement mis en partage sur le réseau de OneSwarm, de sorte qu'il soit disponible sans passer
par le tracker. A l'instar de I2P ou Freenet, chaque utilisateur joue également le rôle de
passerelles entre les autres utilisateurs. Il est donc impossible de savoir d'où viennent réellement
les données, où elles vont et ce qu'elles sont réellement (car chiffrées de bout-en-bout). L'intérêt
majeur de OneSwarm est de pouvoir pratiquer le [friend-to-friend](http://fr.wikipedia.org/wiki/F2F)
(F2F) : on ne se connecte alors qu'à des personnes de confiance, ce qui rend l'utilisateur invisible
sur le réseau hors de son cercle d'ami.

OneSwarm est encore un peu jeune et n'est pas exempt de bugs. Cependant, il est activement développé
ce qui augure de très bonnes choses pour la suite

## Installation et configuration

Note du 10 mars 2010 : depuis la rédaction de cet article, le logiciel a fortement évolué.
Référez-vous au [site officiel](https://forum.oneswarm-fr.net/index.php) pour plus de détails.

[OneSwarm](http://oneswarm.cs.washington.edu/download.html) est open-source et disponible pour
Windows, Linux et Mac OS (Java est requis). Après installation (une simple décompression du fichier
compressé sous Linux), lancez l'exécutable et vous verrez apparaître l'interface dans votre
navigateur Web. A ce sujet, il semble que ça ne fonctionne pas trop avec Internet Explorer, à
vérifier. En l'état, il n'est possible que d'utiliser le réseau Bittorrent classique. Vous pourrez
ajouter des fichiers .torrent comme vous le faisiez avec d'autres logiciels.

Pour utiliser le réseau chiffré anonyme, il vous faudra ajouter des amis dans votre liste. Si vous
n'avez pas d'amis, cliquez sur Add Friend et choisissez l'option "Subscribe to a friend feed from a
community server". Configurez comme sur la figure ci-dessous, et des amis vous seront ajoutés
automatiquement. Cette liste sera régulièrement mise-à-jour, et vous pourrez à tout moment ajouter
d'autres serveurs. Vous noterez que lors de l'ajout d'amis, l'option "Limited" est cochée par
défaut. En fait, un ami ajouté avec cette option ne pourra pas voir votre liste de fichiers. C'est
donc fondamental pour la sécurité d'enlever ce statut limité aux personnes de confiance uniquement.

[![01](/img/post/anonymity-file-sharing/01-thumb.png#center)](/img/post/anonymity-file-sharing/01.png)
[![02](/img/post/anonymity-file-sharing/02-thumb.png#center)](/img/post/anonymity-file-sharing/02.png)

Vous pouvez également ajouter ajouter un ami manuellement, grâce à l'option "Add friends manually
using public keys". OneSwarm fonctionne sur le principe de
[chiffrement asymétrique](http://15minutesoffame.be/nico/blog/2009/05/quelques-elements-de-cryptographie/#chiffrement-asymetrique).
Vous échangez votre clé publique avec celle de votre ami, et le tour est joué.

[![03](/img/post/anonymity-file-sharing/03-thumb.png#center)](/img/post/anonymity-file-sharing/03.png)

Il est tout de même conseillé d'avoir quelques amis pouvant accéder à vos données, de manière à ce
que vos fichiers puissent également être partagés. OneSwarm gère également les groupes d'amis via
"More actions → Manage visibility". Vous pourrez alors partager certains fichiers avec un groupe en
particulier uniquement.

Après avoir ajouté des amis, il vous suffit de faire une recherche dans le champ dédié. Le choix est
encore un peu maigre, mais les dernières nouveautés arrivent assez vite compte tenu de l'utilisation
parallèle du réseau Bittorrent.

# eMule : utilisation de I2P avec iMule

Apparu en 2000, le réseau [eDonkey2000](http://en.wikipedia.org/wiki/EDonkey2000) (sur lequel se
base [eMule](http://en.wikipedia.org/wiki/Emule)) est un réseau encore largement utilisé pour le
partage de fichiers. Son succès est dû principalement au grand choix de fichiers disponibles. En
effet, contrairement au réseau Bittorrent centré sur le partage d'un nombre limité de fichiers, le
réseau eDonkey2000 permet :

*   Le partage d'une grande quantité de fichiers, avec un système poussé de gestion de file
    d'attente.
*   Une vitesse moindre. Si cela semble être un handicap, en pratique l'utilisateur laissera un
    fichier plus longtemps en partage.
*   Une décentralisation des données, car les utilisateurs n'ont pas besoin de se connecter à un
    tracker unique pour être mis en relation. Cependant, on trouve plus facilement des fakes, car il
    suffit de renommer un fichier.
*   Un outil de recherche intégré au logiciel

Le plus célèbre des logiciels supportant le protocole eDonkey2000, eMule, propose deux réseaux
pouvant fonctionner de manière indépendante ou en parallèle. Tout d'abord le réseau eDonkey2000
classique, pour lequel des serveurs permettent de mettre en relation les utilisateurs et centraliser
la liste des fichiers partagés par toutes les personnes connectées. Ensuite le réseau
[Kademlia](http://en.wikipedia.org/wiki/Kademlia), où les serveurs sont inutiles car les
utilisateurs font également office de "mini-serveurs" pour mettre en relation les utilisateurs
connus.

eMule étant un logiciel libre, de nombreux MOD sont apparus (versions d'eMule modifiées apportant
certaines options). Parmi eux, aMule a été porté sous Linux, puis a servi d'inspiration pour
[iMule](http://www.imule.i2p.tin0.de/). iMule utilise un troisième réseau pour partager les
fichiers : le réseau
[I2P](http://15minutesoffame.be/nico/blog/2009/06/securiser-et-rendre-anonyme-sa-navigation/#i2p).
Tout comme pour Kademlia, les utilisateurs servent de relai pour mettre en relation les
utilisateurs, mais ils servent également de relai pour faire transiter les données d'une personne à
l'autre (comme OneSwarm). Cependant, il semble qu'il ne soit pas possible (pour le moment)
d'utiliser iMule comme un client eMule classique, en parallèle de son utilisation sur le réseau I2P.

Je n'ai, à ce jour, pas encore testé iMule (il vous faut une distribution récente ou Windows, ce que
je n'ai pas). Le site du créateur est assez lent, et il n'est pas rare qu'il soit injoignable.
Parcourez le [forum de I2P](http://forum.i2p2.de/viewforum.php?f=30), vous y trouverez surement un
sujet parlant de la
[dernière version en date](http://forum.i2p2.de/viewtopic.php?t=3665&sid=6e134f2d58cdbf42cc55cb247a14598e)
et des liens pour la télécharger.

# Direct Download, ou DDL (RapidShare, MegaUpload...) : toujours tranquille ?

Apparus récemment, les sites de partage de fichiers volumineux ont rapidement été détournés pour le
partage illégal de fichiers. En effet, contre quelques euros par mois, ces sites proposent une
vitesse de téléchargement inégalable en P2P, tout en assurant l'anonymat des utilisateurs.
Cependant, il persiste plusieurs inconvénients :

*   Le prix de l'abonnement : même faible, il n'est pas nul. De plus, il faudra faire un choix parmi
    les nombreux sites existants, et les limitations sont excessives si on n'est pas abonné.
*   Trouver un fichier en particulier n'est pas toujours chose facile, car il existe de nombreuses
    "boards" (sites où sont centralisés les liens).
*   Sur plainte d'un éditeur, un fichier sera purement et simplement supprimé des serveurs, et il
    faudra attendre que quelqu'un veuille bien le remettre.
*   La centralisation des informations : pour trouver un fichier, on devra d'abord s'inscrire sur
    une board pour avoir accès à la liste des fichiers proposés (les IP sont très souvent
    enregistrées). Ensuite, payer l'abonnement au site de partage pour télécharger dans de bonnes
    conditions (utilisation d'une carte de crédit → très facile de retrouver son propriétaire). Si
    pour l'instant, ces sites promettent de ne pas stocker les logs permettant de savoir qui a
    téléchargé quoi, qui sait ce qui se passera dans le futur.

Pour celui qui en a les moyens, RapidShare et ses équivalents sont très pratiques une fois que les
boards intéressantes ont été trouvées. Malheureusement, ceci implique de laisser de nombreuses
traces de son passage, et rien ne dit qu'à l'avenir les utilisateurs ne soient pas inquiétés.
N'oublions pas qu'aucun de ces services n'est hébergé dans un pays laxiste en matière de piratage
(RapidShare est basé en Allemagne, MegaUpload aux USA...), donc un minimum de collaboration des
forces de police pourrait faire mal.

# L'ancêtre : Usenet

[Usenet](http://fr.wikipedia.org/wiki/Usenet) est l'ancêtre de nos forums, et est apparu en 1979,
soit bien avant le World Wide Web. Il est articulé autour du principe de "groupes de discussions"
(ou _newsgroups_) : un groupe de discussion est un groupe rassemblant les articles d'un sujet
précis, ces articles étant stockés sur des serveurs communicant ensemble. S'il est possible de
déposer des articles sur ces serveurs, ils est également possible d'y déposer des fichiers. Moins
populaire que les logiciels de P2P, cette méthode est toujours utilisée par quelques irréductibles
qui apprécient les vitesses de téléchargement élevées et l'anonymat relatif.

Cependant, qui dit serveur centralisant les fichiers, dit service payant. Pour avoir accès à ces
newsgroups, il faudra s'abonner chez un fournisseur proposant plusieurs offres dont le prix varie en
fonction du volume de transfert alloué. Notons que certains FAI, comme Free, proposent un service de
newsgroup inclus dans l'abonnement.

## Installation et configuration

Après avoir pris un abonnement chez un fournisseur (par exemple
[Giganews](http://www.giganews.com/)), vous devrez choisir parmi les
[nombreux newsreader](http://en.wikipedia.org/wiki/List_of_Usenet_newsreaders). Choisissez-en un qui
gère facilement les fichiers, car ce n'est pas le cas de tous (rappelons qu'à la base, Usenet est
fait pour l'échange d'articles, pas le téléchargement de fichiers). Parmi ceux qui reviennent
souvent, [GrabIt](http://www.shemes.com/) sous Windows et [Pan](http://pan.rebelbase.com/) sous
Linux. La configuration du logiciel varie de l'un à l'autre, mais reste assez facile : vous aurez
besoin de l'adresse du serveur du fournisseur, du port, de votre nom d'utilisateur et mot de passe.
Ensuite, partez à la recherche des fichiers NZB (ce sont les fichiers rassemblant les informations
qui permettent de télécharger les différentes parties du fichier désiré) sur les moteurs de
recherches comme [Binsearch](http://www.binsearch.info/), [Newzleech](http://www.newzleech.com/) ou
[MegaNZB](http://www.meganzb.com/). Une fois sauvé, ouvrez le NZB avec votre logiciel, et le tour
est joué.

# Un VPN pour cacher son IP

Déjà présenté dans un
[précédent article](http://15minutesoffame.be/nico/blog/?p=311&preview=true#les-reseaux-prives-virtuels-ou-vpn),
l'utilisation d'un VPN vous permettra de masquer votre adresse IP, que ce soit lors de l'utilisation
du P2P ou du direct download, tout en conservant une vitesse de téléchargement correcte. Outre le
fait qu'il faille faire confiance aux propriétaires de ce VPN concernant les données et logs
conservés, le paiement de ce service entrainera irrémédiablement des traces de votre passage.

# Les réseaux alternatifs

En marge des réseaux de P2P les plus connus que sont Bittorrent et eDonkey2000, de nombreux réseaux
parallèles ont vu le jour. Historiquement pionnier dans le domaine,
[GNUnet](http://www.gnunet.org/index.php?xlang=French) est un logiciel de P2P conçu pour résister à
la censure : chiffrement bout-à-bout, décentralisation des données, utilisateurs servant de relais
pour brouiller les pistes, friend-to-friend, etc. Toutes ces recettes ont été reprises dans
OneSwarm, ou dans d'autres logiciels comme [Ants P2P](http://antsp2p.sourceforge.net/) ou
[MUTE](http://mute-net.sourceforge.net/).

Malgré la grande qualité des idées fondamentales de ces projets, ces réseaux pêchent par le manque
de choix, et par un développement nettement moins actif que OneSwarm. La dernière version de Ants
P2P date de 2007, celle de MUTE de 2008, et aucun développement ne semble être prévu. Le
développement de GNUnet est plus actif, mais mon dernier essai s'est soldé par un échec car le
logicel ne semblait pas très stable.

# Les solutions hybrides

Et si nous pouvions combiner les avantages du P2P (décentralisation, recherche aisée, choix) avec
ceux du téléchargement direct (rapidité et anonymat) ? Séduisant n'est-ce pas ? C'est ce que
proposent des proxys Bittorrent comme [Furk](https://www.furk.net/),
[Torrent Relay](http://www1.torrentrelay.com/fresh/web.pl?d=) ou même
[ImageShack](http://imageshack.us/) (ce dernier nécessite une inscription pour voir apparaitre
l'option). Le proxy se charge de télécharger le fichier à votre place, et quand cela est fait il ne
vous reste plus qu'à le récupérer comme un téléchargement classique. Les connexions sont évidemment
sécurisées, les taux de téléchargement très bons et vous évitez les éventuels filtrage par votre
FAI. Notons que Furk garde sur ses serveurs les fichiers déjà téléchargés par d'autres utilisateurs,
et vous y donne accès gratuitement (avec des restrictions sur la vitesse, cependant). Tout cela est
bien évidemment payant, avec les risques que cela comporte.

Je ne suis cependant sceptique quant à la légalité de la chose... Si les sites habituels de DDL
comme RapidShare peuvent avoir un fond de commerce tout à fait légal, ces sites ne sont là
principalement que pour faciliter le téléchargement d'œuvre protégées. Ce n'est d'ailleurs pas pour
rien qu'il sont situés au Canada ou aux Pays-Bas, pays plus laxistes en la matière. J'ai donc de
gros doutes sur leur pérennité.

# Conclusion : peer-to-peer ou direct download, que choisir&nbsp;?

Impossible de donner une réponse précise, car comme nous l'avons vu chaque méthode a ses avantages
et ses inconvénients. Tentons de faire un petit récapitulatif...

Les avantages du peer-to-peer :

*   Une décentralisation des données, rendant difficile l'élimination des fichiers mis en partage.
*   Une visibilité temporaire : dès qu'on ne partage plus le fichier, on disparait de la liste des
    utilisateurs (mais gare aux trackers privés Bittorrent gardant des logs détaillés). Cependant,
    il faut tempérer cette "visibilité" : si toutes les personnes téléchargeant un fichier peuvent
    connaitre votre adresse IP, il leur faudra intenter une action en justice pour mettre un nom
    dessus. Notons que grâce aux nouveaux réseaux, cette visibilité devient quasi nulle.
*   Une notion de partage et de communauté plus forte : l'utilisateur n'est pas un simple
    consommateur, il peut partager avec les autres membres ce qu'il apprécie.
*   Un service gratuit.

Les inconvénients du peer-to-peer :

*   L'introduction de fakes est plus ou moins aisée (très facile dans le cas d'eMule, plus difficile
    dans le cas de Bittorrent).
*   Une vitesse pas toujours au rendez-vous.
*   Les risques juridiques plus élevés : en mettant à disposition des autres utilisateurs du contenu
    non-libre de droit, des sanctions supplémentaires sont à craindre. On est largement hors du
    cadre de la "copie privée". Notons que les condamnations ont toujours été faites sur base de la
    mise à disposition illégale de contenu.

Les avantages du direct download :

*   Une vitesse maximale.
*   Un anonymat relatif : seuls les responsables du site ou newsgroup sur lequel vous téléchargez
    savent ce que vous faites.
*   Très peu de fakes, car les liens sont référencés sur des boards où les participants n'ont aucun
    intérêt à donner de faux liens aux autres, sous peine d'être rapidement éjectés.
*   Les risques juridiques moindres car vous n'avez pas mis en partage vos données.

Les inconvénients du direct download :

*   Un service payant.
*   Des traces nombreuses, au risque qu'elles soient permanentes, rendant votre identification
    facile et la liste de vos actions aisément consultable.
*   Un contenu susceptible de disparaitre des serveurs en cas de plainte de l'ayant-droit.

Pour le moment, les solutions payantes semblent les plus sures d'un point de vue juridique : ne
partageant rien vous-même, vous risquez moins que si vous mettez à disposition des données.
Cependant, ces solutions sont aussi les plus jeunes, contrairement aux utilisateurs des réseaux P2P
qui ont déjà subi plusieurs attaques des ayants-droits (voir par exemple le
[jugement de cette américaine](http://www.numerama.com/magazine/13205-Condamnee-a-payer-2-millions-de-dollars-pour-24-chansons-telechargees.html)).
Rien ne dit que la facilité avec laquelle vos téléchargements peuvent être listés ne se retournera
pas contre vous un jour ou l'autre...
