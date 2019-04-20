+++
title = "SSH : la connexion à distance sécurisée"
date = "2009-08-27T03:00:00+02:00"
tags = ["anonymat"]
archives = "2009"
type = "article"
+++

Dans cet article, nous aborderons la connexion à distance vers un PC sous GNU/Linux. L'intérêt
premier est évidemment l'administration d'une machine à distance, mais cela peut également être
utile pour la récupération de fichiers lors de
[voyages à l'étranger](http://www.israelvalley.com/news/2009/08/14/23881/israel-securite-pillages-de-donnees-en-israel-faut-il-etre-parano-lors-de-vos-passages-en-douane-avec-un-ordinateur-reponse-pas-plus-que-l-aeroport-de-shangai).
Outre la mise en place d'un serveur SSH, nous traiterons de la gestion firewall, du routeur éventuel
ainsi que de l'adresse IP dynamique.

# Configuration du serveur

Le serveur est la machine à laquelle vous voulez vous connecter, et qui retiendra la majorité de
notre attention. Cette machine devra être équipée d'une distribution GNU/Linux quelconque. Une
installation sous Windows est possible, mais semble être plus du bricolage qu'autre chose.

## IP fixe sur le LAN

Par défaut, l'attribution de l'adresse IP sur le réseau local (LAN) se fait par
[DHCP](http://fr.wikipedia.org/wiki/Dynamic_host_configuration_protocol), et est donc variable. Cela
peut poser des problèmes lorsque, par exemple, le routeur devra transférer les données vers votre
serveur. La première chose à faire est donc d'attribuer une IP fixe à votre serveur. Pour cela, vous
devez connaitre l'adresse IP de votre passerelle ainsi que la gamme d'adresses IP attribuées. Par
exemple, chez la passerelle est 192.168.1.1 et les IP sont attribuées entre 192.168.1.2 et
192.168.1.254. La configuration à appliquer dans votre système devra ressembler à ça :

[![01](/img/post/openssh-intro/01-thumb.png#center)](/img/post/openssh-intro/01.png)

Cette fenêtre varie d'une distribution à l'autre, mais elle est souvent accessible via un clic sur
l'applet de connexion réseau. Vous devrez peut-être aussi indiquez les serveurs DNS (permettant de
faire le lien entre une adresse IP et le nom de domaine) ; indiquez ceux d'OpenDNS, à savoir
208.67.222.222 et 208.67.220.220.

## Installation du serveur SSH

Installons tout d'abord le serveur SSH, à savoir OpenSSH. Sous debian/Ubuntu :

```
marty@serveur:~$ sudo apt-get install openssh-server
```

À ce stade, le serveur est déjà opérationnel, mais allons tout d'abord faire un tour dans les
options de configuration du fichier `/etc/sshd.conf`. La majorité des options par défaut sont
bonnes, mais nous allons en modifier quelques unes. Tout d'abord le port d'écoute, par défaut 22,
peut être modifié :

```
Port 12345
```

Changer le port par défaut permet de réduire les tentatives de connexion par des robots. Évidemment,
une personne physique effectuant un scan de port complet pourra facilement trouver les ports
ouverts. Ensuite, s'assurer que la connexion en root est impossible :

```
PermitRootLogin no
```

Root est le seul utilisateur commun à toutes les distributions (excepté Ubuntu, pour lequel il est
désactivé par défaut et remplacé par sudo). Par conséquent, interdire la connexion à root obligera
un attaquant éventuel à trouver un nom d'utilisateur existant. Et finalement, désactiver
l'authentification par mot de passe :

```
PasswordAuthentication no
UsePAM no
```

Comment allons-nous nous connecter au serveur ? Et bien en utilisant ce que nous avons appris
précédemment, à savoir une paire de clés ! De manière similaire à ce que nous faisions avec GnuPG,
nous génèrerons une paire de clé sur chaque client, et nous fournirons la clé publique au serveur.
De cette façon, seuls les clients ayant une clé enregistrée sur le serveur pourront s'y connecter.
Notez que dans un premier temps, vous devrez avoir un accès physique au serveur pour copier la clé
publique. Si ce n'est pas le cas, laissez les paramètres précédents sur "yes" le temps d'enregistrer
votre clé.

Quand ces modifications ont été appliquées, relancez le démon ssh :

```
marty@serveur:~$ sudo /etc/init.d/ssh restart
```

## Routeur et configuration du firewall via Webmin

Si vous êtes derrière un routeur, et que votre serveur doit être accessible depuis d'extérieur de
votre LAN, vous devez transférer le port choisi vers votre serveur. Concernant le firewall, si vous
savez comment configurer le votre, ouvrez simplement le port que vous avez attribué, sous le
protocole TCP. Si ce n'est pas le cas ou que vous voulez découvrir Webmin, lisez donc la suite ;-)

Tout bon serveur qui se respecte se doit d'avoir un firewall bien configuré. Sous GNU/Linux, le
firewall intégré au système est Netfilter. Il existe plusieurs possibilités pour le configurer :

*   en ligne de commande, grâce à iptables ou shorewall
*   en utilisant le firewall Firestarter
*   grâce à [Webmin](http://www.webmin.com/), un outil d'administration graphique assez général

Si Firestarter reste la solution la plus simple, c'est aussi la moins "propre" vu ses possibilités
limitées et sa configuration basique. Iptables requiert quant à lui un peu d'expérience pour être
manipulé correctement. Reste alors Webmin, assez simple d'accès tout en proposant des possibilités
de configuration poussées. C'est celui-ci que nous allons utiliser. Notez que les firewalls
graphiques n'enregistrent pas leur configuration directement dans Netfilter : ils ont besoin d'être
lancés pour que les règles soient appliquées. En outre, si deux firewalls fonctionnent en même
temps, ce sont les règles du dernier ayant été lancé qui seront appliquées. Veillez donc à n'avoir
qu'un firewall bien configuré sur votre machine pour éviter les embrouilles ;-)

[Procurez-vous](http://www.webmin.com/download.html) tout d'abord Webmin, celui-ci étant disponible
pour de nombreuses distributions. Après installation, rendez vous sur la page
[https://localhost:10000/](https://localhost:10000/) via votre navigateur web. L'utilisateur est
root, et votre mot de passe est votre mot de passe root. Pour les utilisateurs d'Ubuntu, veuillez
vous référer à [cette page](http://doc.ubuntu-fr.org/root) pour activer le compte root. Rendez à la
page Networking → Linux Firewall.

Dans la partie Incoming packets (INPUT), voici les 5 règles de base à appliquer :

```
Accept     If state of connection is ESTABLISHED,RELATED
Accept     If source is 127.0.0.1 and input interface is lo
Accept     If protocol is ICMP
Log packet     Always
Drop     Always
```

La règle "Log packet" va, comme son nom l'indique, établir un log des paquets qui seront rejetés
dans /var/log/messages. Pour les retrouver facilement, je conseille d'ajouter dans la case
"Additional parameters" (lors de la création de la règle) l'instruction :

```
--log-prefix "[IPTABLES DROP]: "
```

Dans la partie Forwarded packets (FORWARD), on refuse tout :

```
Drop     Always
```

Je laisse la partie Outgoing packets (OUTPUT) vide, ce qui signifie que toutes les connexions
sortantes sont autorisées. Vous devriez trouver assez facilement comment créer ces règle, ce n'est
pas bien compliqué. Veillez tout de même à sélectionner "Equals" au lieu de "Ignored" pour les cases
modifiées. L'ordre des règle est très important : elles seront appliquées de haut en bas. Il faut
donc toujours que la règle "Drop Always" soit la dernière !

Pour SSH, la règle à appliquer dans Incoming packets (INPUT) est :

```
Accept     If protocol is TCP and destination port is 12345
```

Nous parlons bien de **port de destination**. En effet, comme ce sont les paquets entrant, leur
destination est bien notre serveur. 12345 est évidemment à remplacer par le port que vous avez
choisi. Cliquez finalement sur "Apply Configuration", et choisissez "Yes" pour "Activate on boot".

## Protection contre les attaques "brute force" : fail2ban

Une attaque par "[force brute](http://fr.wikipedia.org/wiki/Attaque_par_force_brute)" est une
attaque tout ce qu'il y a de plus basique. Elle consiste à essayer toutes les combinaisons possibles
de lettres/chiffres jusqu'à trouver le bon mot de passe. Elle est souvent combinée à une
[attaque par dictionnaire](http://fr.wikipedia.org/wiki/Attaque_par_dictionnaire) pour améliorer la
vitesse de cassage. On comprend facilement que l'efficacité de ce type d'attaque dépend de la
solidité du mot de passe choisi : `banane76` risque d'être découvert beaucoup plus rapidement que
`a0D€8È}~v£2%ï2`.

Pour se prémunir d'une telle attaque sur son serveur SSH, les précautions précédentes (pas de
connexion en root, changement du port pour limiter les attaques par des robots) permettent déjà de
limiter les risques. Si la connexion par mot de passe est désactivée, ces attaques seront totalement
inefficaces. Cependant, on peut vouloir laisser cette possibilité active pour une raison ou une
autre. Fail2ban va nous aider à nous protéger contre les attaquants éventuels (et n'ayez crainte,
vous devrez y faire face très rapidement). Le principe est simple : bannir les adresses IP qui ont
effectué trop de tentatives infructueuses de connexion, via une règle dans le firewall.

Tout d'abord, installer fail2ban :

```
marty@serveur:~$ sudo apt-get install fail2ban
```

Ouvrez ensuite le fichier /etc/fail2ban/jail.conf, et cherchez les parties suivantes :

```
[DEFAULT]
ignoreip = 127.0.0.1
bantime  = 900
findtime = 600
maxretry = 3

[ssh]
enabled = true
port    = ssh
filter  = sshd
logpath  = /var/log/auth.log
maxretry = 6
```

La partie `[DEFAULT]` contient les options par défaut, alors que la partie `[ssh]` les options
propres à SSH (sans déconner !). Passons-les en revue :

*   `ignoreip` permet d'ignorer les connexions venant d'une certaine adresse IP, ici l'adresse IP
locale
*   `bantime` est la durée de bannissement d'une adresse attaquant
*   `findtime` est le laps de temps pendant lequel les connexions d'une même IP vont être analysée
*   `maxretry` est le nombre maximum de tentative de connexions infructueuses avant bannissement

Dans mon cas, si le serveur reçoit 6 connexions infructueuses (maxretry) en moins de 10 minutes
(findtime), l'adresse IP sera bannie 15 minutes (bantime). Dans le cas de SSH, un mot de passe est
demandé 3 fois à chaque connexion, ce qui fait au maximum 72 essais par heure et par adresse IP.

Après configuration, relancez fail2ban :

```
marty@serveur:~$ sudo fail2ban-client reload
```

Vous pouvez également vérifier s'il fonctionne correctement :

```
marty@serveur:~$ sudo /etc/init.d/fail2ban status
```

Voilà, avec ça vous devriez être tranquille.

## Adresse IP dynamique

Si votre FAI vous attribue une adresse IP dynamique (adresse IP de votre ordinateur sur Internet,
pas sur le réseau local !), vous aurez besoin d'un service comme [DynDNS](http://www.dyndns.com/).
Celui-ci vous permettra d'associer à votre serveur un nom de domaine, et ce gratuitement. L'adresse
IP sera mise à jour grâce au logiciel ddclient que nous installerons plus tard.

Vous devez tout d'abord vous [créer un compte](https://www.dyndns.com/account/entrance/) sur le site
de DynDNS. Allez ensuite sur la page
"[Host Services](https://www.dyndns.com/account/services/hosts/)", et cliquez sur
"Add New Hostname". Choisissez un nom de domaine, sélectionnez "Host with IP address" et indiquez
votre adresse IP. Pour mettre à jour l'IP, trois possibilités :

*   le faire manuellement via l'interface de DynDNS (peu pratique)
*   via l'interface de votre modem/routeur/\*box : certains appareils disposent en effet de la
possibilité d'enregistrer un compte et de mettre à jour votre IP automatiquement
*   en installant ddclient

Installez ddclient :

```
marty@serveur:~$ sudo apt-get install ddclient
```

La configuration du fichier `/etc/ddclient.conf` devrait ressembler à ceci :

```
## ddclient configuration file
daemon=300                  # check every 300 seconds
syslog=yes                  # log update msgs to syslog
pid=/var/run/ddclient.pid   # record PID in file.
ssl=yes

## Detect IP with our CheckIP server
use=web, web=checkip.dyndns.com/, web-skip='IP Address'

## Default options
protocol=dyndns2

## DynDNS username and password here
server=members.dyndns.org
login=YYYYYYYY
password='XXXXXXXX'

## Dynamic DNS hosts
blablabla.tatata.com
```

Indiquez votre login, mot de passe (entre guillemets simples) ainsi que le(s) nom(s) de domaine.
J'ai choisi de faire la mise à jour toutes les 5 minutes.

# Configuration du client

Côté client, la configuration est très simple. Après installation du paquet openssh-client,
connectez-vous grâce à la commande :

```
marty@client:~$ ssh -p 12345 login@blablabla.tatata.com
```

où `login` est votre login sur le serveur et 12345 à remplacer par le port choisi. Notez que si vous
vous connectez depuis votre réseau local, il y a de fortes chances pour que l'utilisation du nom de
domaine ne fonctionne pas. Il faudra plutôt utiliser l'adresse IP fixe du serveur. Si vous avez
laissé le port par défaut (22), l'option -p est inutile.

## Authentification par clé publique/privée

Rappelez-vous : nous devions utiliser la connexion par clé publique/privée ! Dans le cas où la
connexion via mot de passe est désactivée, cette commande ne fonctionnera pas. Générons la paire de
clé :

```
marty@client:~$ ssh-keygen -t dsa
```

Laissez les options par défaut, et indiquez une phrase de passe. Ensuite, vous devrez copier le
contenu du fichier `~/.ssh/id_dsa.pub` dans le fichier `/home/<login>/.ssh/authorized_keys` de votre
serveur. Si la connexion par mot de passe n'est pas désactivée, vous pouvez utiliser la ligne :

```
marty@client:~$ ssh login@blablabla.tatata.com "echo $(cat ~/.ssh/id_dsa.pub) >> .ssh/authorized_keys"
```

Grâce à la même commande que précédemment, connectez-vous sur votre serveur. Votre phrase de passe
vous sera demandée à la place de votre mot de passe, et si cela fonctionne, vous pouvez désactiver
l'autorisation par mot de passe si ce n'est déjà fait (soyez tout de même sûr de pouvoir accéder
physiquement au serveur au cas où votre clé privée serait perdue).

Taper sa phrase de passe, c'est chiant... Oui, je sais. Nous allons donc utiliser ssh-agent pour
nous faciliter la vie. Dans un terminal, tapez :

```
marty@client:~$ ssh-add
```

et entrez votre phrase de passe. Connectez vous sur votre serveur et là, magie, votre phrase de
passe ne vous est plus demandée ! C'est là un énorme avantage d'utiliser l'authentification par clé
publique/privée plutôt que par mot de passe. Il suffit d'entrer sa phrase de passe en début de
session, et on est tranquille toute la journée ;-) Il est possible de fournir la même clé publique
sur plusieurs serveurs SSH : une fois la passphrase enregistrée, les connexions se font sans mot de
passe. Qui plus est, on n'a pas à retenir un mot de passe différent pour chaque serveur.

## Transfert de fichiers

Il est possible de transférer des fichiers via SSH grâce à la commande scp. Pour envoyer un fichier
sur le serveur :

```
marty@client:~$ scp -P 12345 fichier marty@serveur:/dossier/serveur
```

Pour récupérer un fichier du serveur :

```
marty@client:~$ scp -P 12345 marty@serveur:/dossier/fichier /dossier/client
```

Attention, c'est bien un P majuscule !

Le logiciel gftp permet de faire graphiquement la même chose que scp. Il se présente sous la forme
de deux fenêtres, une pour le client et une pour le serveur.

[![02](/img/post/openssh-intro/02-thumb.png#center)](/img/post/openssh-intro/02.png)

Faites attention de sélectionner le bon type de fichier (ASCII -- fichier texte simple -- ou
Binaire -- le reste) dans le menu "FTP".

## Et les autres OS ?

Le noyau de Mac OS X étant un dérivé de BSD, les lignes de commandes devraient être identiques. Sous
Windows, allez voir du côté de [PuTTY](http://www.putty.org/) pour la ligne de commande et
[WinSCP](http://winscp.net/eng/docs/lang:fr) comme équivalent de gftp.
