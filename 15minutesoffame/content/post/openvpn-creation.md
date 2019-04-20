+++
title = "Créer un serveur OpenVPN"
date = "2009-09-23T03:00:00+02:00"
tags = ["openvpn", "vpn", "anonymat"]
archives = "2009"
type = "article"
+++

Depuis quelques mois, les solutions de VPN payant type Ipredator ont fleuri sur la toile. Ces
solutions d'anonymat, séduisantes au premier abord, possèdent un gros point noir : qui se cache
réellement derrière ces VPN ? N'y a-t-il pas un risque que ces "bienfaiteurs de l'Internet libre" ne
revendent un jour toutes les données collectées ? Comme on n'est jamais mieux servi que par
soi-même, nous allons voir comment monter son propre serveur VPN grâce à OpenVPN. Par ailleurs, ce
VPN pourra aussi vous servir à passer les éventuelles restrictions mises en place sur votre lieu de
travail, ou sécuriser votre connexion lorsque vous devez vous connecter sur des réseaux publics peu
sécurisés.

# Configuration du serveur

Avant toute chose, vous devez avoir accès à un serveur, si possible avec une bande passante
suffisante. En effet, ce serveur va servir de relai entre vous et la cible distante : la bande
passante en upload du serveur deviendra votre bande passante en download maximale. Dès lors, mieux
vaut se tourner vers un service professionnel, offrant souvent une bande passante allant jusqu'à
100 Mb/s (environ 12 Mo/s). Cherchez donc du côté des [VPS](http://fr.wikipedia.org/wiki/Vps)
(Virtual Private server) : vous aurez toutes les possibilités d'un serveur dédié, mais à prix
(et performances) réduit. Un serveur OpenVPN est très léger, donc 128 Mo de RAM devraient être
suffisants. En France, [Gandi](http://www.gandi.net/hebergement/),
[OVH](http://www.ovh.com/fr/produits/offres_rps.xml) ou
[LWS](http://www.lws.fr/serveur_dedie_linux.php) ont des offres intéressantes à moins de 15 € par
mois. Partagée entre 2 ou 3 personnes de confiance, cette solution est rapidement plus avantageuse
qu'une solution type Ipredator. Attention tout de même car beaucoup de VPS promettent une bande
passante de 100 Mbits/s, mais en pratique ce n'est pas le cas. La bande passante n'est pas partagée
de manière équitable entre les différentes machines virtuelles, et résultat les performances
laissent à désirer (j'ai déjà eu le cas avec du 100 Mbits/s qui en pratique approchait péniblement
le 100 kbits/s...). Cherchez donc des solutions où la bande passante est moindre, mais assurée
(comme Gandi le propose).

Avant de mettre en place votre VPN, pensez à
[sécuriser votre serveur](/nico/blog/2009/08/ssh-la-connexion-a-distance-securisee/). Une machine
avec IP fixe accessible 24h/24 sera irrémédiablement la cible d'attaques.

## Installation de OpenVPN et création des clés et certificats

Installez tout d'abord OpenVPN, bien souvent disponible dans les dépôts de base de votre
distribution :

```
marty@server:# apt-get install openvpn
```

OpenVPN peut fonctionner avec plusieurs types d'authentification. Nous utiliserons
l'authentification par clés et certificats, plus sûre que le classique login/mot de passe. Pour
générer les clés et certificats nécessaires, des scripts ont été créés et se situent, sous
Ubuntu 9.04, dans le dossier `/usr/share/doc/openvpn/examples/easy-rsa/2.0`. Commençons par copier
tout ceci dans un répertoire de travail (tout le processus doit s'effectuer en tant que root) :

```
marty@server:# cd /etc/openvpn
marty@server:# cp -r /usr/share/doc/openvpn/examples/easy-rsa/2.0 /etc/openvpn
marty@server:# mv 2.0/ easy-rsa/
marty@server:# cd easy-rsa/
```

Modifiez tout d'abord les variables du fichiers vars :

```
export KEY_COUNTRY="US"
export KEY_PROVINCE="CA"
export KEY_CITY="SanFrancisco"
export KEY_ORG="Fort-Funston"
export KEY_EMAIL="me@myhost.mydomain"
```

Initialisez-le via la commande :

```
marty@server:# . ./vars
```

(vous devez bien écrire point/espace/point, ce n'est pas une erreur).

On efface les éventuelles clés présentes :

```
marty@server:# ./clean-all
```

On crée le certificat et la clé de l'Autorité de Certification (CA) :

```
marty@server:# ./build-ca
```

Les fichiers `ca.crt` et `ca.key` sont alors créés dans le dossier keys, et les variables
précédentes devront être confirmées. Ces fichiers sont les fichiers centraux de la sécurité de votre
serveur OpenVPN. La clé vous servira à signer les clés du (des) serveur(s) ainsi que des différents
clients, et le certificat servira de "carte d'identité" à laquelle serveur(s) et clients se
réfèreront.

On crée le certificat et la clé pour le serveur :

```
marty@server:# ./build-key-server server
```

Laissez toutes les options par défaut (y compris la demande de mot de passe), et répondez "yes" à la
question de la signature :

```
Certificate is to be certified until Sep  5 14:02:19 2019 GMT (3650 days)
Sign the certificate? [y/n]:y
1 out of 1 certificate requests certified, commit? [y/n]y
```

Le certificat du serveur sera alors signé avec la clé de l'Autorité de Certification. Les fichiers
server.crt et server.key seront créés.

On crée le certificat et la clé pour le client :

```
marty@server:# ./build-key client1
```

De la même manière que pour le serveur, on laisse toutes les options par défaut et on accepte la
signature par avec la clé de la CA. Les fichiers `client1.crt` et `client1.key` seront créés. Il est
recommandé de créer une paire certificat/clé par client, de manière à pouvoir les révoquer par la
suite si nécessaire (au cas où le client les perdrait).

Pour que notre serveur fonctionne, nous auront également besoin des paramètres de
[Diffie-Hellman](http://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman) :

```
marty@server:# ./build-dh
```

Le fichier dh1024.pem est créé. J'avoue, je n'ai pas compris à quoi cela servait précisément dans le
cas de OpenVPN...

Finalement, nous augmentons encore la sécurité de notre serveur grâce à
[tls-auth](http://www.openvpn.net/index.php/open-source/documentation/howto.html#security) :

```
marty@server:# openvpn --genkey --secret keys/ta.key
```

Le fichier `ta.key` est créé.

## Résumé des fichiers créés

Au terme dela génération de ces diverses clés et certificats, nous obtenons les fichiers suivants :

*   `ca.crt` : certificat de l'Autorité de Certification
*   `ca.key` : **clé de l'Autorité de Certification**
*   `server.crt` : certificat du serveur
*   `server.key` : **clé du serveur**
*   `client1.crt` : certificat du client1
*   `client1.key` : **clé du client1**
*   `dh1024.pem` : paramètres de Diffie-Hellman
*   `ta.key` : clé utilisée pour tls-auth

Les fichiers en gras sont les fichiers à garder secrets. Attention toute particulière au fichier
`ca.key` qui sert à signer tous les certificats. Il permet d'autoriser ou non un client, et il est
donc fondamental qu'il soit gardé secret !

En pratique, les fichiers nécessaires sont :

*   serveur : `ca.crt`, `server.crt`, `server.key`, `dh1024.pem` et `ta.key`
*   client1 : `ca.crt`, `client1.crt`, `client1.key` et `ta.key`

Notez bien que le fichier ca.key n'est nécessaire ni sur le serveur, ni chez aucun client !
Gardez-le en lieu sûr ;-)

## Fichier de configuration serveur

Toute la configuration s'effectue dans un fichier quelconque, ci-après `server.conf`. Voilà un
exemple typique :

```
#Configuration serveur

mode server # c'est le fichier de configuration du serveur
proto tcp # protocole TCP
port 443 # port 443 (https)
dev tun # mode routé

#Clefs
ca keys/ca.crt
cert keys/server.crt
key keys/server.key
dh keys/dh1024.pem
tls-auth keys/ta.key 0 # 0 pour le serveur
cipher AES-256-CBC # algorithme de chiffrement

#Configuration VPN
#client-to-client # permet la connexion entre clients
server 10.8.0.0 255.255.255.0 # adresse IP attribuées sur le VPN
push "redirect-gateway def1 bypass-dhcp" # redirection du flux de données
push "dhcp-option DNS 208.67.222.222" # utilisation de DNS alternatifs
push "dhcp-option DNS 208.67.220.220"
keepalive 10 120 # ping toutes les 10 secondes,
                 # considéré comme down après 120 secondes sans réponses

#Divers
user nobody # on passe de l'utilisateur root à nobody
group nogroup # nogroup est typique d'Ubuntu, groupe nobody pour les autres
chroot /etc/openvpn/ovpn_jail # chroot de openvpn
persist-key # n'accède plus à certaines options,
persist-tun # car réduction des privilèges utilisateur
comp-lzo # compression des données

#Log
verb 3 # verbosité du log (1-9, 4 recommandé)
mute 20 # ne répète pas plus de 20 fois un message
status openvpn-status.log # fichier de statut
log-append /var/log/openvpn.log # fichier de log
```

Tout d'abord, le port utilisé (443) a été choisi parce qu'il n'est jamais bloqué (port https). Vous
pouvez utiliser un autre port plus aléatoire si vous ne devez pas contourner de blocages
quelconques.

Le mode routé (dev tun) est préféré au mode bridgé pour sa plus grande simplicité de configuration.
Si vous avez une utilisation "basique" du VPN, ne vous préoccupez pas de ça.

De nombreux algorithmes de chiffrement sont disponibles. Nous choisissons ici le chiffrement AES 256
bits, qui est assez élevé. Si votre serveur rame, tentez de passer à du 128 bits.

client-to-client permet à deux clients de se connecter l'un à l'autre, par exemple via un serveur
NFS. Dans notre cas, cette ligne est commentée.

server 10.8.0.0 255.255.255.0 définit le range d'adresses IP locales qui seront attribuées. Le
serveur prendra l'adresse 10.8.0.1, et les clients 10.8.0.2, 10.8.0.3, 10.8.0.4... Attention : cette
adresse ne doit rentrer en conflit avec aucune autre. Évitez donc d'utiliser les habituelles
192.168.x.x ou 10.108.x.x.

La ligne contenant "redirect-getaway" spécifie que tout le flux doit être redirigé vers le VPN.
Attention à cette ligne qui peut différer d'une version à l'autre. Il semble que sous CentOS, il ne
faille pas mettre les mots clés "def1 bypass-dhcp", alors que sous Ubuntu 9.04 cela est obligatoire.

Par la suite, la sécurité est améliorée en diminuant les privilèges du programme (`user nobody`,
`group nogroup`) et en effectuant un chroot (le dossier spécifié doit être créé). De cette manière,
une éventuelle faille d'OpenVPN ne pourra être exploitée qu'en tant qu'utilisateur restreint, dans
un environnement restreint.

Vous pouvez faire un premier test, en commentant la ligne `log-append` pour que le log s'affiche
directement dans le terminal. Pour cela, on lance (en root, dans le dossier où se trouvent le
fichier `server.conf` ainsi que le répertoire keys) :

```
marty@server:# openvpn server.conf
OpenVPN 2.1_rc11 i486-pc-linux-gnu [SSL] [LZO2] [EPOLL] [PKCS11] built on Mar  9 2009
Diffie-Hellman initialized with 1024 bit key
/usr/bin/openssl-vulnkey -q -b 1024 -m <modulus omitted>

Control Channel Authentication: using 'keys/ta.key' as a OpenVPN static key file
Outgoing Control Channel Authentication: Using 160 bit message hash 'SHA1' for HMAC authentication
Incoming Control Channel Authentication: Using 160 bit message hash 'SHA1' for HMAC authentication
TLS-Auth MTU parms [ L:1560 D:168 EF:68 EB:0 ET:0 EL:0 ]
ROUTE default_gateway=XXX.XXX.XXX.XXX
TUN/TAP device tun0 opened
TUN/TAP TX queue length set to 100
/sbin/ifconfig tun0 10.8.0.1 pointopoint 10.8.0.2 mtu 1500
/sbin/route add -net 10.8.0.0 netmask 255.255.255.0 gw 10.8.0.2
Data Channel MTU parms [ L:1560 D:1450 EF:60 EB:135 ET:0 EL:0 AF:3/1 ]
chroot to '/etc/openvpn/ovpn_jail' and cd to '/' succeeded
GID set to nogroup
UID set to nobody
Listening for incoming TCP connection on [undef]:443
Socket Buffers: R=[87380->131072] S=[16384->131072]
TCPv4_SERVER link local (bound): [undef]:443
TCPv4_SERVER link remote: [undef]
MULTI: multi_init called, r=256 v=256
IFCONFIG POOL: base=10.8.0.4 size=62
MULTI: TCP INIT maxclients=1024 maxevents=1028
Initialization Sequence Complete
```

La ligne `TUN/TAP device tun0 opened` indique que l'interface `tun0` a bien été créée (c'est le
réseau virtuel), `chroot to...`, `GID set...` et `UID set...` que le chroot ainsi que le changement
de propriétaire ont bien fonctionné. Dans un autre terminal, le `ifconfig` donne :

```
eth0      Link encap:Ethernet  HWaddr 00:16:3e:51:5f:e9
 inet addr:XXX.XXX.XXX.XXX  Bcast:XXX.XXX.XXX.255  Mask:255.255.252.0
 inet6 addr: fe80::216:3eff:fe51:5fe9/64 Scope:Link
 UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
 RX packets:162377096 errors:0 dropped:0 overruns:0 frame:0
 TX packets:153812357 errors:0 dropped:0 overruns:0 carrier:0
 collisions:0 txqueuelen:1000
 RX bytes:4278174076 (4.2 GB)  TX bytes:2956197161 (2.9 GB)

lo        Link encap:Local Loopback
 inet addr:127.0.0.1  Mask:255.0.0.0
 inet6 addr: ::1/128 Scope:Host
 UP LOOPBACK RUNNING  MTU:16436  Metric:1
 RX packets:127075 errors:0 dropped:0 overruns:0 frame:0
 TX packets:127075 errors:0 dropped:0 overruns:0 carrier:0
 collisions:0 txqueuelen:0
 RX bytes:77312107 (77.3 MB)  TX bytes:77312107 (77.3 MB)

tun0      Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00
 inet addr:**10.8.0.1**  P-t-P:10.8.0.2  Mask:255.255.255.255
 UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1500  Metric:1
 RX packets:0 errors:0 dropped:0 overruns:0 frame:0
 TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
 collisions:0 txqueuelen:100
 RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
```

L'adresse IP du serveur sur le réseau virtuel (`tun0`) est bien 10.8.0.1.

En l'état, votre serveur ne fonctionnera pas. Pourquoi ? Parce que le firewall n'a pas été configuré
bien sûr ;-)

## Configuration du firewall

Avant toute chose, on s'assure que le forwarding est activé en tapant dans un terminal (en root) :

```
marty@server:# echo 1 > /proc/sys/net/ipv4/ip_forward
```

Comme dans la section précédente, nous utiliserons Webmin pour configurer le firewall.

Dans la section Packet filtering, on ajoute les règles :

```
Incoming packets (INPUT)
Accept     If protocol is TCP and destination port is 443
Accept     If input interface is tun0

Forwarded packets (FORWARD)
Accept     If input interface is tun0
Accept     If output interface is tun0
```

Et dans la section Network address translation :

```
Packets after routing (POSTROUTING)
Masquerade     If source is 10.8.0.0/24 and output interface is eth0
```

Adaptez évidemment en fonction du protocole, port et adresse IP choisis.

Avec Iptables, cela donne :

```
iptables -A INPUT --dport 443 -p tcp
iptables -A INPUT -i eth0
iptables -A FORWARD -i tun0 -j ACCEPT
iptables -A FORWARD -o tun0 -j ACCEPT
iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE
```

Ces règles sont peut-être un peu trop permissives, il est sûrement possible de les améliorer.

# Configuration du client

Configurer un client est très simple, car cela repose sur la création dun fichier `client.conf`, à
la manière du `server.conf`. Voilà le fichier client.conf associé au server.conf précédent :

```
#Configuration client
client # mode client
dev tun
proto tcp-client
remote XXX.XXX.XXX.XXX 443 #Remplacer XXX par l'adresse IP ou le nom d'hôte
resolv-retry infinite
nobind
persist-key
persist-tun

#Clefs
ca keys/ca.crt
cert keys/client1.crt
key keys/client1.key
tls-auth keys/ta.key 1 #1 pour le client
cipher AES-256-CBC

#Ces 3 lignes sont inutiles si spécifié dans la configuration du serveur
#redirect-gateway def1 bypass-dhcp
#dhcp-option DNS 208.67.222.222
#dhcp-option DNS 208.67.220.220

comp-lzo
verb 3
```

Il faut bien s'assurer que les options sont identiques entre client et serveur (compression, port,
protocole, chiffrement...), car une seule erreur et ça ne fonctionnera pas. Après avoir fourni les
clés fichiers nécessaires (voire section précédente) ainsi que le fichier `client.conf` au client
concerné, installé OpenVPN sur la machine cliente, il suffit de lancer dans un terminal (après avoir
préalablement lancé OpenVPN sur le serveur):

```
marty@client:# openvpn client.conf
OpenVPN 2.1_rc7 i486-pc-linux-gnu [SSL] [LZO2] [EPOLL] built on May  8 2009
WARNING: No server certificate verification method has been enabled.  See http://openvpn.net/howto.html#mitm for more info.
/usr/bin/openssl-vulnkey -q -b 1024 -m <modulus omitted>
Control Channel Authentication: using 'keys/ta.key' as a OpenVPN static key file
Outgoing Control Channel Authentication: Using 160 bit message hash 'SHA1' for HMAC authentication
Incoming Control Channel Authentication: Using 160 bit message hash 'SHA1' for HMAC authentication
LZO compression initialized
Control Channel MTU parms [ L:1560 D:168 EF:68 EB:0 ET:0 EL:0 ]
Data Channel MTU parms [ L:1560 D:1450 EF:60 EB:135 ET:0 EL:0 AF:3/1 ]
Local Options hash (VER=V4): '2f2c6498'
Expected Remote Options hash (VER=V4): '9915e4a2'
Attempting to establish TCP connection with XXX.XXX.XXX.XXX:443 [nonblock]
TCP connection established with XXX.XXX.XXX.XXX:443
Socket Buffers: R=[87380->131072] S=[16384->131072]
TCPv4_CLIENT link local: [undef]
TCPv4_CLIENT link remote: XXX.XXX.XXX.XXX:443
TLS: Initial packet from XXX.XXX.XXX.XXX:443, sid=4421b77a 4dc14e71
VERIFY OK: depth=1, /C=US/ST=CA/L=SanFrancisco/O=Fort-Funston/CN=Fort-Funston_CA/emailAddress=me@myhost.mydomain
VERIFY OK: depth=0, /C=US/ST=CA/L=SanFrancisco/O=Fort-Funston/CN=server/emailAddress=me@myhost.mydomain
Data Channel Encrypt: Cipher 'AES-256-CBC' initialized with 256 bit key
Data Channel Encrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
Data Channel Decrypt: Cipher 'AES-256-CBC' initialized with 256 bit key
Data Channel Decrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
Control Channel: TLSv1, cipher TLSv1/SSLv3 DHE-RSA-AES256-SHA, 1024 bit RSA
[server] Peer Connection Initiated with XXX.XXX.XXX.XXX:443
SENT CONTROL [server]: 'PUSH_REQUEST' (status=1)
PUSH: Received control message: 'PUSH_REPLY,redirect-gateway def1 bypass-dhcp,dhcp-option DNS 208.67.222.222,dhcp-option DNS 208.67.220.220,route 10.8.0.1,topology net30,ping 10,ping-restart 120,ifconfig 10.8.0.6 10.8.0.5'
OPTIONS IMPORT: timers and/or timeouts modified
OPTIONS IMPORT: --ifconfig/up options modified
OPTIONS IMPORT: route options modified
OPTIONS IMPORT: --ip-win32 and/or --dhcp-option options modified
TUN/TAP device tun0 opened

TUN/TAP TX queue length set to 100
ifconfig tun0 10.8.0.6 pointopoint 10.8.0.5 mtu 1500
route add -net XXX.XXX.XXX.XXX netmask 255.255.255.255 gw 192.168.1.1
route add -net 0.0.0.0 netmask 128.0.0.0 gw 10.8.0.5
route add -net 128.0.0.0 netmask 128.0.0.0 gw 10.8.0.5
route add -net 10.8.0.1 netmask 255.255.255.255 gw 10.8.0.5
Initialization Sequence Complete
```

et ça devrait fonctionner ! Pour vérifier, on tente d'abord un ifconfig qui devrait renvoyer quelque
chose de similaire à ce qui s'affiche sur le serveur, et vérifier son adresse IP sur
[http://checkip.dyndns.com](http://checkip.dyndns.com/). Vous devriez alors avoir l'adresse IP du
serveur. Par ailleurs, vérifiez également que vos DNS ont été changés (allez sur le site
[http://www.opendns.com/](http://www.opendns.com/), et si c'est le cas "You're using OpenDNS"
devrait être indiqué). Si ce n'est pas le cas, changez-les manuellement dans le fichier
`/etc/resolv.conf` ou via l'applet de configuration réseau.

# Un peu d'automatisation...

Côté serveur, on peut lancer OpenVPN grâce à la commande :

```
marty@server:# nohup openvpn server.conf &
```

`nohup` permet de ne pas terminer la commande (en l'occurence, `openvpn`) lorsqu'on coupera la
connexion SSH. Selon la distribution utilisée, il est possible qu'OpenVPN se lance automatiquement
au démarrage.

Côté client, il vous faudra installer le paquet `network-manager-openvpn` pour pouvoir effectuer la
configuration depuis l'applet réseau. Avec les versions récentes de ce dernier, il suffit de
glisser-déposer le fichier `client.conf` dans l'onglet VPN pour que la configuration soit
automatique. On activera/désactivera alors simplement la connexion via l'applet réseau.

# Conclusion

En principe, tout devrait être fonctionnel. Si ce n'est pas le cas, n'hésitez à pas demander de
l'aide au support de votre hébergeur, certains nécessitant une configuration supplémentaire pour
fonctionner.

Vous pouvez également vérifier le trafic réseau grâce à Wireshark (à lancer en root). Allez dans
Capture → Options, puis cliquez sur Start. Dans la colonne Info, vous devriez voir la mention
"Encrypted data" de nombreuses fois, et des transferts vers le port https (si vous avez choisi le
port 443, évidemment). Si c'est le cas, c'est que ça fonctionne !
