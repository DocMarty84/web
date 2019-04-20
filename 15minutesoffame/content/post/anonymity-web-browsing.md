+++
title = "Sécuriser et rendre anonyme sa navigation"
date = "2009-06-21T03:00:00+02:00"
tags = ["anonymat"]
archives = "2009"
type = "article"
+++

Dans cette quatrième partie consacrée à la sécurité et l'anonymat sur Internet, nous étudierons les
possibilités existantes pour la navigation sur la toile. Avant toute chose, précisons tout de même
qu'être anonyme à 100 % est tout simplement impossible. Théoriquement il est toujours possible de
remonter jusqu'à vous, mais en pratique il est possible de rendre les choses très difficiles.

# Le protocole HTTPS

Le HTTPS n'est rien d'autre que le [protocole](http://fr.wikipedia.org/wiki/Protocole_de_communication)
[HTTP](http://fr.wikipedia.org/wiki/Http) classique (celui utilisé pour la navigation web) auquel on
a ajouté une méthode de chiffrement [TLS](http://fr.wikipedia.org/wiki/Transport_Layer_Security). En
d'autres termes, il s'agit de la navigation web où les transfert sont chiffrés entre le client
(vous) et le serveur. En pratique, cela fonctionne en 3 étapes :

1.  Le client se connecte au serveur.
2.  Le serveur envoie un certificat numérique [X.509](http://fr.wikipedia.org/wiki/X.509) ainsi que
    sa clé de chiffrement symétrique.
3.  Le client vérifie que (i) le certificat est valide, (ii) qu'il a été fourni par une
    [authorité de certification](http://fr.wikipedia.org/wiki/Autorit%C3%A9_de_certification)
    connue, (iii) qu'il n'a pas été altéré et (iv) que le
    [nom de domaine](http://fr.wikipedia.org/wiki/Nom_de_domaine) correspond.

Si tout s'est bien passé, le client et le serveur peuvent communiquer de manière chiffrée grâce à la
clé qui a été échangée. Si un "pirate" venait à intercepter les données, il ne pourrait rien en
faire. C'est la méthode utilisée sur la majorité des sites de vente en ligne ou des banques. On
reconnait l'utilisation du HTTPS à :

*   l'utilisation de https au lieu de http dans la barre d'adresse (exemple de site
[non sécurisé](http://www.ixquick.com/fra/), et [sécurisé](https://www.ixquick.com/fra/))
*   la présence d'un petit cadenas, en bas à droite (pour Firefox)

Le HTTPS est sensiblement plus lent que le HTTP vu l'opération supplémentaire de chiffrement. Il
n'assure en rien l'anonymat, mais permet de communiquer des informations à un serveur en toute
sécurité.

# Utilisation de proxys

Un proxy est une passerelle entre vous et le site web que vous désirez visiter. Au lieu d'envoyer
directement les demandes au serveur, vous passerez par le proxy qui se chargera de les communiquer
au site final. Certains proxys permettent l'utilisation du protocole HTTPS. Les avantages sont les
suivants :

*   Anonymat au niveau du site visité : le site que vous visitez ne sait pas qui a demandé au proxy
    de lui transmettre des informations.
*   Anonymat au niveau de votre FAI : votre FAI voit que vous vous connectez au proxy, mais ne
    connait pas la page finale que vous désirez voir. Ceci est d'autant plus vrai si le proxy
    utilise le protocole HTTPS. En outre, vous pouvez contourner les éventuelles restrictions mises
    en place par certaines sociétés (aller sur Youtube, Myspace, Facebook...).
*   Sécurité : le proxy dispose très souvent d'un firewall bloquant les éventuelles attaques
    provenant de sites malveillants.

Il y a cependant quelques inconvénients à l'utilisation de proxys :

*   Le proxy connait les sites que vous visitez, et revendra éventuellement ces informations. Rien
    n'est totalement gratuit...
*   Un proxy malveillant pourrait collecter les mots de passes de connexion, ou toute autre
    information transitant par lui.

Un proxy est donc plus centré sur l'anonymat que sur la sécurité, à moins de connaitre
personnellement celui qui l'a mis en place. Il est aussi intéressant de changer régulièrement de
proxy, de manière à éviter qu'un proxy ne collecte trop d'informations sur vous.

[![01](/img/post/anonymity-web-browsing/01-thumb.png#center)](/img/post/anonymity-web-browsing/01.png)

## Le proxy simple

Après la théorie, passons à la pratique. Tout d'abord, il faudra trouver un proxy, par exemple sur
[proxy.org](http://proxy.org/) ou encore [atproxy.net](http://www.atproxy.net/). Après avoir fait
votre choix dans la liste (certains ne fonctionnent pas ou sont très lents), rendez-vous sur la page
correspondante ([exemple](http://anonymouse.org/anonwww.html)), indiquez l'adresse que vous désirez
visiter et validez. Une barre d'options est souvent ajoutée en haut de la page de navigation.

Pour faciliter l'utilisation de proxys, il existe plusieurs modules pour Firefox. Mon préféré est
[Phzilla](https://addons.mozilla.org/fr/firefox/addon/3239), très simple d'utilisation mais dont le
développement a récemment été abandonné.
[FoxyProxy](https://addons.mozilla.org/fr/firefox/addon/2464) est lui un outil très complet, un peu
trop pour moi d'ailleurs vu mon utilisation très ponctuelle de proxys.

## Tor et Privoxy

Et si au lieu d'utiliser un seul relai, nous en utilisions plusieurs ? C'est le principe de
[Tor](http://www.torproject.org/index.html.fr), qui couplé à [Privoxy](http://www.privoxy.org/) vous
permet d'atteindre un très haut niveau d'anonymat. Tor est composé d'un ensemble connu de relais qui
seront utilisés pour atteindre un site désiré. Le chemin suivi à travers les proxys change
régulièrement, de sorte qu'il est pratiquement impossible de savoir d'où viennent et où vont les
données.

[![02](/img/post/anonymity-web-browsing/02-thumb.png#center)](/img/post/anonymity-web-browsing/02.png)

Privoxy est un proxy web permettant un filtrage avancé du contenu, mais il ne nous servira qu'à
masquer la requête [DNS](http://fr.wikipedia.org/wiki/Domain_Name_System). En fait, lorsque vous
vous connectez à un site web (par exemple www.google.com), vous passez tout d'abord par un serveur
DNS qui fera le lien entre l'adresse demandée et son adresse IP (en l'occurence, 208.69.34.231).
Ceci a deux avantages :

*   facilité pour retenir le site : en effet, il est beaucoup plus facile de retenir un nom
    (www.google.com) qu'une série de 5 nombres (208.69.34.231)
*   indépendance vis-à-vis de l'adresse IP : un site peut changer d'adresse IP, ceci sera totalement
    transparent pour l'utilisateur

Lorsqu'on désire utiliser Tor, la première chose qui est faite est de demander au serveur DNS
(souvent celui du FAI) quelle est l'adresse IP correspondante. Ceci est un gros trou dans
l'anonymat : si le FAI ne voit pas les connexions avec le site sur lequel on veut se connecter, il
sait tout de même qu'on a demandé quelle était son adresse IP. Privoxy permet de combler ce trou.

#### Installation et configuration

Dans le cas où vous utilisez Ubuntu, Tor n'est pas inclu dans la version 9.04 et il faudra ruser
pour l'installation. Je vous laisse consulter la
[page dédiée](http://doc.ubuntu-fr.org/tor#installation_de_tor). Dans le cas d'autres distributions,
l'installation de Tor et Privoxy ne devrait poser aucun problème. Après installation, il faudra
modifier les fichiers de [configuration de Privoxy](http://doc.ubuntu-fr.org/privoxy) pour qu'il
communique avec Tor. Éditez le fichier /etc/privoxy/config en root et ajoutez la ligne :

```
forward-socks4a / localhost:9050 .
```

Pour trouver la ligne adéquate, cherchez la chaîne "forward-socks" dans le fichier. Lancez ensuite
les deux services, par exemple sous Ubuntu :

```
sudo /etc/init.d/tor restart
sudo /etc/init.d/privoxy restart
```

Il ne reste plus qu'à configurer votre navigateur web. Dans le cas de Firefox, allez dans Éditions →
Préférences, allez dans la section Avancé, onglet réseau, puis cliquez sur paramètres et configurez
comme suit :

[![03](/img/post/anonymity-web-browsing/03-thumb.png#center)](/img/post/anonymity-web-browsing/03.png)

Vous pouvez vérifier que Tor fonctionne bien en visitant le lien
[http://check.torproject.org/](http://check.torproject.org/). Il existe également des modules pour
Firefox, permettant de switcher facilement sur Tor (comme
[Torbutton](https://addons.mozilla.org/fr/firefox/addon/2275) ou
[FoxyProxy](https://addons.mozilla.org/fr/firefox/addon/2464)).

Il est possible de monter un serveur Tor chez soi, de manière à renforcer l'anonymat. En effet,
impossible alors de savoir si ce qui a transité par votre PC était bien de votre volonté ou un
transfert d'un proxy à un autre.

Remarque importante : Tor permet l'anonymat, mais pas la sécurisation des données. En effet, même si
les données sont chiffrées entre tous les nœuds du réseau, elles ne le sont pas entre le nœud final
et le site auquel on veut accéder. Prudence donc...

## I2P

A première vue, [I2P](http://fr.wikipedia.org/wiki/I2P) propose des fonctionnalités similaires à
Tor, mais son fonctionnement est quelque peu différent. Tor est composé d'un ensemble de proxys
connus (donc centralisé), chacun permettant d'accéder au web. Son but avoué est d'offrir l'anonymat
sur la toile. I2P est plutôt centré sur la communication chiffrée d'une extrémité à l'autre entre
deux personnes, tout en utilisant plusieurs passerelles. Chaque utilisateur de I2P joue le rôle de
passerelle (donc décentralisé), mais à la différence de Tor seules quelques rares passerelles
("outproxy") offrent un lien vers le web. I2P semble donc plus destiné à une forme de peer-to-peer
qu'au surf anonyme, même s'il le permet également.

#### Installation et configuration

Téléchargez l'[installeur graphique](http://www.i2p2.de/download.html) sur le site officiel, et
exécutez-le. Sous Linux, tapez en ligne de commande :

```
java -jar i2pinstall_0.7.4.exe
```

Rien de bien sorcier à ce niveau, il vous suffira de choisir un répertoire d'installation. Après
quelques secondes, la page de configuration ([http://127.0.0.1:7657/](http://127.0.0.1:7657/))
devrait s'ouvrir dans votre navigateur web. Vous pourrez contrôler l'état de votre passerelle, et
éventuellement changer la configuration. Si votre "Reachability" est indiquée comme étant
"Firewelled", vous devrez configurez votre routeur pour qu'il transfère le port 8887 (TCP et UDP)
vers votre PC. Ce n'est nullement obligatoire, mais cela aide à la santé du réseau.

La configuration de Firefox est identique à celle lorsque Tor est utilisé, sauf que vous devrez
indiquer le port 4444 au lieu de 8118.

Remarque : les eepsites sont des sites du réseau I2P, accessibles uniquement à partir de I2P. Leur
intérêt est qu'ils ne nécessitent pas l'utilisation de passerelle spécifique accédant au web.

# Les réseaux privés virtuels, ou VPN

Il existe deux inconvénients majeurs à l'utilisation de proxys :

*   la lenteur du surf
*   certains programmes ne fonctionnent pas avec Tor

Un [réseau virtuel privé](http://fr.wikipedia.org/wiki/R%C3%A9seau_priv%C3%A9_virtuel) (VPN) permet
de se connecter à un réseau externe comme si vous étiez matériellement sur ce réseau. Ceci est
souvent utilisé en entreprise pour que les employés puissent accéder à leurs données
professionnelles depuis l'extérieur. Les avantages sont une plus grande flexibilité par rapport à un
proxy, un cryptage complet des données transitant entre l'utilisateur et le VPN, mais surtout le
fait que tous les programmes fonctionnent comme si vous étiez situé sur ce réseau, et ce sans aucune
configuration particulière.

En réponse aux lois contre le téléchargement prises récemment en Suède et en France, deux VPN ont
été mis en place : [Ipredator](http://ipredator.se/) et [Ipodah](http://ipodah.net/) (encore à
l'essai à l'heure où j'écris ces lignes). Le principe est que vous vous connectez à ces réseaux qui
serviront de passerelle pour toutes les données transférées, que ce soit du surf classique ou du
peer-to-peer. Le principe est donc identique au proxy, si ce n'est que vous ne serez pas limités à
l'anonymat sur le web mais aussi lors des échanges P2P (nous y reviendront dans un prochain
article). Selon les créateurs, aucune trace ne sera enregistrée, ce qui confère une sécurité
parfaite.

En principe, les serveurs mis en places devraient être capables de soutenir une charge importante,
et ne réduire que faiblement le taux de transfert des données. Notez que ces services sont payants
(environ 5 € par mois). Vous devrez également faire une confiance aveugle aux créateurs de ces
services :

*   rien ne vous dit qu'ils n'intercepteront pas vos données
*   rien ne vous dit qu'ils ne gardent pas des traces de tout ce qui passe par les serveurs

De plus, ayez toujours à l'esprit que si ces serveurs sont saisis par la justice et que des traces
sont gardées, remonter jusqu'à vous sera très facile même si vous n'étiez pas l'objet
d'investigations. Gardez aussi à l'esprit que si ces services sont payants, des traces du paiement
persisteront toujours quelque part.

# Les réseaux alternatifs : le cas Freenet

Les solutions précédentes sont des suppléments ajoutés au réseau Internet. Finalement, ce ne sont
que des rustines utilisées pour combler les trous de sécurité et d'anonymat du réseau. En parallèle
à Internet, il existe des réseau alternatifs, conçus à la base pour être anonyme et sécurisés. Le
plus célèbre d'entre eux est [Freenet](http://freenetproject.org/). Les caractéristiques principales
du réseau sont :

*   la décentralisation totale des données : chaque utilisateur joue le rôle de serveur car une
    petite partie de Freenet est stockée chez chacun. Dès lors, les pages non visitées tendent à
    disparaitre, mais il est quasi impossible de supprimer des données tant que des utilisateurs les
    consultent.
*   un anonymat extrême : chaque utilisateur joue aussi le rôle de passerelle entre d'autres
    utilisateurs (à l'image de I2P). En outre, il est possible de choisir soi-même les personnes à
    qui on va se connecter.
*   un niveau de sécurité important : toutes les données stockées par Freenet sont chiffrées sur le
    disque, avec une clé inconnue de l'utilisateur. Ce dernier peut donc nier en toute bonne foi
    savoir ce qui se trouve sur son disque dur.

Notez bien que Freenet ne permet pas d'accéder au web classique : c'est un réseau parallèle. Ces
caractéristiques en font un refuge idéal pour les personnes vivant dans des régimes totalitaires,
mais malheureusement une vitrine parfaite pour tout ce qui est illégal. Il n'est donc pas rare de
tomber sur des "recettes" de poison maison, des sites néo-nazis ou encore de la pédo-pornographie.
Il faut donc utiliser ce réseau intelligemment, et résister à la curiosité malsaine. En effet, en
consultant ces sites vous favorisez leur développement car chaque utilisateur (qu'il soit
l'intéressé ou simple passerelle) stocke un petit morceau du réseau chez lui. Le meilleur moyen de
lutter contre la prolifération de ce contenu est de simplement passer son chemin, en espérant que le
site sombre lentement mais surement pour disparaître du réseau.

#### Installation et configuration

Après la mise en garde, passons à l'installation. Suivez les instructions sur
[le site officiel](http://freenetproject.org/download.html) selon votre OS, et installez Java si ce
n'est pas déjà fait. Sous Linux, tapez dans un terminal :

```
wget http://freenet.googlecode.com/files/new_installer_offline_1222.jar -O new_installer_offline.jar
java -jar new_installer_offline.jar
```

Après la configuration (choisissez "normal" à toutes les propositions), vous pourrez accéder à
Freenet via n'importe quel navigateur en allant à l'adresse
[http://127.0.0.1:8888/](http://127.0.0.1:8888/). Attention au cache de votre navigateur : si
Freenet chiffre toutes les données stockées, votre navigateur ne le fait sûrement pas. Pensez donc à
désactiver le cache, voire à utiliser un autre navigateur (dans Firefox, allez dans Édition →
Préférences → Vie privée → Décocher "Conserver mon historique").

**A suivre, partie 5 : [Anonymat et partage de fichiers](http://15minutesoffame.be/nico/blog2/?article13/anonymat-et-partage-de-fichiers).**
