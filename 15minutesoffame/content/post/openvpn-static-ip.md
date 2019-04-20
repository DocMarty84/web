+++
title = "Configuration OpenVPN : IP statiques et redirection de ports"
date = "2010-07-19T03:00:00+02:00"
tags = ["openvpn", "vpn", "anonymat"]
archives = "2010"
type = "article"
+++

Dans un [article précédent](/nico/blog2/?article16/creer-un-serveur-openvpn), nous avons présenté un
tutoriel pour la mise en place d'un serveur OpenVPN. Nous verrons à présent comment configurer ce
serveur pour qu'il attribue des adresses IP statiques aux différents clients, ainsi que la
redirection de ports via IPTables.

Tout d'abord, je me permets de faire un peu de pub gratuite pour le service de
[cloud computig d'OVH](http://www.kimsufi.com/cloud/), qui permet d'avoir accès à un prix très
intéressant à un serveur sur leur cloud. Outre le prix de base très avantageux (paiement à
l'utilisation), ce service se révèle très intéressant car il fournit une bande passante de 100 Mbps
illimitée. C'est une offre qui colle donc parfaitement à l'utilisation d'un serveur VPN.

Par ailleurs, ce tutoriel suppose que vous ayez déjà quelques notions techniques concernant OpenVPN.
Si ce n'est pas le cas, référez-vous d'abord à
[l'article précédent](/nico/blog2/?article16/creer-un-serveur-openvpn).

# Mise en place du serveur OpenVPN

Trêve de publicité, il faut tout d'abord mettre en place OpenVPN. Pour cela, on fait comme la
dernière fois :

```
marty@server:# apt-get install openvpn
marty@server:# cd /etc/openvpn
marty@server:# cp -r /usr/share/doc/openvpn/examples/easy-rsa/2.0 /etc/openvpn
marty@server:# mv 2.0/ VPN_static/
marty@server:# cd VPN_static/
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

On crée les certificats et clés nécessaires (se reporter à
[l'article précédent](/nico/blog2/?article16/creer-un-serveur-openvpn) pour les détails) :

```
marty@server:# ./build-ca
marty@server:# ./build-key-server server
marty@server:# ./build-dh
marty@server:# openvpn --genkey --secret keys/ta.key
marty@server:# ./build-key client1
```

A ce stade, nous avons créé tous les certificats et clés nécessaires au serveur et à un premier
client, nommé **client1**. Passons à présent à la configuration du serveur proprement dite.

# Configuration du serveur

Dans le cas d'adresses IP attribuées de manière statiques, l'idée est de créer, pour chaque client,
un fichier spécifiant l'adresse IP à lui attribuer. Voilà tout d'abord un exemple type de fichier de
configuration `server.conf` :

```
#Configuration serveur

mode server # c'est le fichier de configuration du serveur
proto udp # protocole UDP
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
server 10.8.0.0 255.255.255.0 # adresse IP attribuée sur le VPN
push "redirect-gateway def1 bypass-dhcp" # redirection du flux de données
push "dhcp-option DNS 208.67.222.222" # utilisation de DNS alternatifs
push "dhcp-option DNS 208.67.220.220"
keepalive 10 120 # ping toutes les 10 secondes,
                 # considéré comme down après 120 secondes sans réponses

client-config-dir /ccd # Copier le contenu dans le dossier du chroot
ccd-exclusive

#Divers
user nobody # on passe de l'utilisateur root a  nobody
group nogroup # nogroup est typique d'Ubuntu, groupe nobody pour les autres
chroot /etc/openvpn/ovpn_jail # chroot de openvpn
persist-key # n'accède plus a certaines options,
persist-tun # car réduction des privilèges utilisateur
comp-lzo # compression des données

#Log
verb 4 # verbosité du log (1-9, 4 recommandé)
mute 20 # ne répète pas plus de 20 fois un message
status openvpn-status.log # fichier de statut
log-append /var/log/openvpn.log # fichier de log
```

En gras, la partie qui diffère de la configuration dynamique utilisée précédemment. La première
ligne (`client-config-dir /ccd`) précise que les fichiers spécifiques aux clients se trouveront dans
le dossier `ccd`. La seconde ligne (ccd-exclusive) forcera l'utilisation de ces fichiers de
configuration, ce qui implique par ailleurs qu'un client n'ayant pas de fichier spécifique ne se
verra pas attribuer d'IP. Il est tout à fait possible de ne pas indiquer ce mot-clef, auquel cas les
clients n'ayant pas de fichier spécifique obtiendront un IP dynamique.

## Création des fichiers spécifiques aux clients

Créons le dossier ccd ainsi que le premier fichier client :

```
marty@server:# mkdir ccd
marty@server:# vi ccd/client1
```

Pour attribuer l'adresse IP 10.8.0.10 à ce client, on colle simplement :

```
ifconfig-push 10.8.0.10 10.8.0.11
```

Une petite astuce est nécessaire ici. Au cas où vous ne l'auriez pas remarqué, nous avons indiqué
dans notre fichier de configuration le répertoire `/ccd`, et non pas `ccd`. Cela vient de
l'utilisation du chroot. Cependant, OpenVPN ne copie pas automatiquement ce répertoire ccd lors de
la création du chroot, c'est-à-dire qu'il vous faudra le copier manuellement. On peut soit le copier
manuellement maintenant, soit le faire automatiquement au lancement du serveur. Pour la copie
manuelle :

```
marty@server:# mkdir -p /etc/openvpn/ovpn_jail
marty@server:# cp -r ccd /etc/openvpn/ovpn_jail
```

De plus, nous avons omis de préciser que le fichier du client doit porter le même nom que le Common
Name (CN) spécifié lors de la création du certificat du client. Par défaut, le CN est le nom donné
dans la commande de création du certificat, ici client1.

## Automatisation du lancement du serveur

Par défaut, OpenVPN lance automatiquement le fichier server.conf trouvé dans le dossier
`/etc/openvpn`. Le nôtre se trouvant dans le dossier `/etc/openvpn/VPN_static/`, il nous faut
changer ce comportement par défaut. Cela se fait en modifiant le fichier `/etc/init.d/openvpn` :

```
#CONFIG_DIR=/etc/openvpn
CONFIG_DIR=/etc/openvpn/VPN_static
```

On peut en profiter pour automatiser la copie du répertoire `ccd`, en ajoutant en début de fichier :

```
rm -rf /etc/openvpn/ovpn_jail
mkdir -p /etc/openvpn/ovpn_jail
cp -r /etc/openvpn/VPN_static/ccd /etc/openvpn/ovpn_jail
```

La commande `rm` est utilisée pour nettoyer le chroot, si nécessaire.

## Configuration du firewall

Nous utiliserons un script IPTables pour la configuration du firewall. Outre les règles habituelles
du VPN, nous pouvons ajouter le forward de certains ports spécifiques pour certains clients. Par
exemple, dans le fichier `/etc/init.d/iptables.sh` :

```
#!/bin/bash

# Nettoyage des règles
/sbin/iptables -F
/sbin/iptables -X

# Règles de base
/sbin/iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
/sbin/iptables -A INPUT -p tcp -i eth0 --dport ssh -j ACCEPT

# Règles générales pour le VPN
/sbin/iptables -A INPUT -p udp -i eth0 --dport 443 -j ACCEPT
/sbin/iptables -A FORWARD -i tun0 -j ACCEPT
/sbin/iptables -A FORWARD -o tun0 -j ACCEPT
/sbin/iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE

# Règles spécifiques pour le forward de données sur un port particulier
/sbin/iptables -A FORWARD -i eth0 -p tcp --dport 20000 -j ACCEPT
/sbin/iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 20000 -j DNAT --to 10.8.0.10:20000

/sbin/iptables -P INPUT DROP
/sbin/iptables -P FORWARD DROP

echo 1 > /proc/sys/net/ipv4/ip_forward

exit 0
```

Dans ce cas, nous forwardons ce qui arrive sur le port 20000 (protocole TCP) vers l'adresse IP
10.8.0.10, celle-ci ayant été attribuée à **client1**. Par la même occasion, nous activons le
forwarding, car il semble que dans certains cas la valeur de ip_forward se remette par défaut à zéro
lors d'un reboot. Reste à rendre ce fichier exécutable et à le lancer au démarrage :

```
marty@server:# chmod +x /etc/init.d/iptables.sh
marty@server:# update-rc.d iptables.sh defaults
```

Une autre utilisation possible est de créer des règles d'accès spécifiques, en fonction de l'adresse
IP. On peut par exemple définir des utilisateurs restreints ou des utilisateurs privilégiés
uniquement à partir de l'adresse IP qui leur est attribuée.

Dans tous les cas, n'oubliez pas d'ajouter vos propres règles, si nécessaire ;) De plus, par mesure
de sécurité, testez toujours votre script avant d'automatiser son lancement. Une erreur stupide et
votre serveur pourrait devenir purement et simplement inaccessible.

# Configuration du client

La configuration du client est totalement identique en IP dynamique ou statique (client1.conf) :

```
#Configuration client
client # mode client
dev tun
proto udp
remote XXX 443 # Remplacer XXX par l'adresse IP ou le nom d'hôte
resolv-retry infinite
nobind
persist-key
persist-tun

#Clefs
ca keys/ca.crt
cert keys/client1.crt
key keys/client1.key
tls-auth keys/ta.key 1 # 1 pour le client
cipher AES-256-CBC

comp-lzo
verb 3
```

Vous devrez fournir à chaque client les fichiers suivant :

*   client1.conf
*   keys/ca.crt
*   keys/client1.crt
*   keys/client1.key
*   keys/ta.key

Voili voilou...

# Conclusion

Dans cet article, nous avons vu comment il était possible d'attribuer aux utilisateurs qui se
connectent à un serveur OpenVPN une adresse IP fixe. Une IP fixe peut se révéler utile pour la
redirection de port ou le contrôle des accès. De plus, nous avons vu comment automatiser
complètement le lancement du serveur OpenVPN ainsi que l'application au démarrage des règles du
firewall.
