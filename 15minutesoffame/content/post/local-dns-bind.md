+++
title = "Sécuriser ses DNS : dnscrypt et cache local avec bind"
date = "2015-08-01T03:00:00+02:00"
tags = ["dns", "dnscrypt", "anonymat", "bind"]
archives = "2015"
type = "article"
+++

On va jouer les cow-boys aujourd'hui : on chiffre ses DNS avec DNSCrypt, puis on se fait un petit
cache local avec Bind pour améliorer les perfs.

Les [DNS](https://fr.wikipedia.org/wiki/Domain_Name_System) font régulièrement la une des news
numériques, pour la simple et bonne raison que c'est souvent via une méthode de
[DNS menteur](https://fr.wikipedia.org/wiki/Manipulation_de_l%27espace_des_noms_de_domaine) que le
sites webs controversés sont bloqués. Et par site controversé on entend surtout les sites de
partage, en particulier Bittorrent. D'ailleurs si vous ne l'avez pas encore fait, commencez déjà
par changer vos DNS pour ne plus utiliser ceux de votre FAI, par exemple ceux de Google. Il existe
une chiée de tutoriels un peu partout, on va pas revenir là-dessus.

# Quels DNS choisir m'sieur?

C'est bien cool de changer ses DNS, mais si on se préoccupe un peu de sa vie privée, utiliser les
DNS de Google, ça pue franchement. Google connaît déjà le contenu de ma boîte mail et de mon agenda,
manquerait plus qu'il trace aussi tous les sites web auxquels j'accède. Une initiative intéressante
est celle d'[OpenNIC](https://www.opennicproject.org/), qui vous propose une liste des DNS
accessibles [les plus proches de chez vous](https://www.opennicproject.org/nearest-servers/). Tant
qu'à faire, configurez aussi les DNS en IPv6, y'a des
[convertisseurs](https://www.ultratools.com/tools/ipv4toipv6).

# Chiffrer ses requêtes DNS : DNSCrypt

Changer ses DNS, c'est bien joli, mais les requêtes passent toujours en clair par votre FAI. Et ce
même si vous vous connectez en HTTPS, voire que vous utilisez un VPN. Bref, ça fait un peu chier. On
va chiffrer tout ça grâce à [DNSCrypt](http://dnscrypt.org/). C'est un petit soft qui a pour but de
chiffrer les communications DNS entre le client (vous) et le serveur DNS. Double avantage : votre
FAI ne peut plus lorgner sur vos requêtes DNS, et en plus de ça ça évite les attaques type MITM.

## Installation

Sur Ubuntu et dérivés, il existe un PPA qu'il est bien :
[PPA DNSCrypt](https://launchpad.net/~xuzhen666/+archive/ubuntu/dnscrypt). Pour installer, rien de
bien sorcier :

```
sudo add-apt-repository ppa:xuzhen666/dnscrypt
sudo apt-get update && sudo apt-get install dnscrypt-proxy
```

Par défaut, le service va écouter sur l'adresse 127.0.2.1, port 53. Il suffit donc de paramétrer
cette adresse dans vos DNS (aussi en IPv6), et le tour est joué.

## Configuration de base : choisir un autre serveur

Par défaut, DNSCrypt passe par OpenDNS. Niveau neutralité, c'est pas ce qu'il y a de mieux... Mais
c'est cool, on peut le changer facilement. DNSCrypt est livré avec un beau fichier qui contient
toute une série de DNS alternatifs compatibles :

```
/usr/share/dnscrypt-proxy/dnscrypt-resolvers.csv
```

C'est pas très joli à lire dans le terminal, le plus facile est peut-être de l'ouvrir avec
LibreOffice Calc :

[![01](/img/post/local-dns-bind/01-thumb.png#center)](/img/post/local-dns-bind/01.png)

Il suffit de faire son marché là-dedans, et copier le nom dans le fichier
`/etc/default/dnscrypt-proxy`, variable `DNSCRYPT_PROXY_RESOLVER_NAME`. Par exemple ipredator:

```
...
# Remote DNS(Crypt) resolver.
# You can find a list of resolvers at
# /usr/share/dnscrypt-proxy/dnscrypt-resolvers.csv.
DNSCRYPT_PROXY_RESOLVER_NAME=ipredator
...
```

Il faut bien sûr redémarrer le service dnscrypt-proxy.

## Configuration avancée : serveur DNS aléatoire

Juste parce qu'on a envie de faire les malins, on va ajouter un autre serveur. Pour ça, il suffit
d'ajouter une ligne dans le CSV. On peut on trouver à ces endroits :
[https://dns.d0wn.biz/](https://dns.d0wn.biz/) ou
[http://meo.ws/dnsrec.php/](http://meo.ws/dnsrec.php/). Comme je suis un vrai cow-boy de l'Internet,
mon œil torve a été attiré par cette petite note, dans le premier lien :

> \[DNSCrypt Randomizer\]
>
> DNS-Server:	ns1.random.dns.d0wn.biz\
> IPv4:		178.17.170.133\
> Location:	Moldova\
> Provider-Key:	9970:E22D:7F6C:967F:8AED:CEEB:FBC1:94B9:AF54:376E:2BF7:39F1:F466:CBC9:AFDB:2A62\
> Provider-Name:	2.dnscrypt-cert.d0wn.biz\
> Ports:		54 80 443 1053 5353 27015\
>
> Our randomizer randomize your dns queries through our and the ovpn.to DNSCrypt servers (currently
> 18!).\
> This randomizer is only useable with DNSCrypt and still in BETA testing.\
> All traffic between you and the randomizer is encrypted. Also all traffic between our randomizer
> and the dns resolver is encrypted.\
> The dns resolver never get your own IP.

Ouais, on n'a pas peur, on va ajouter le randomizer. En gros, chaque requête va être envoyée à un serveur DNS différent, parmi un choix de 18 serveurs. C'est pas très compliqué, on ajoute cette ligne au fichier dnscrypt-resolvers.csv :

```
d0wn-md-rnd1,Randomizer d0wn server in Moldova,Server provided by Martin 'd0wn' Albus,Moldova,,https://dns.d0wn.biz,1,no,yes,yes,178.17.170.133:54,2.dnscrypt-cert.d0wn.biz,9970:E22D:7F6C:967F:8AED:CEEB:FBC1:94B9:AF54:376E:2BF7:39F1:F466:CBC9:AFDB:2A62,
```

Et puis on change la variable `DNSCRYPT_PROXY_RESOLVER_NAME` dans `/etc/default/dnscrypt-proxy` :

```
DNSCRYPT_PROXY_RESOLVER_NAME=d0wn-md-rnd1
```

On redémarre, et on peut tester sur cette page :
[https://www.dnsleaktest.com/](https://www.dnsleaktest.com/). Choisissez Extended test, et vous
devriez voir apparaître une bonne dizaine de serveurs DNS différents. Yeah baby!

**EDIT : Suite à un commentaire, j'ai testé Dnsmasq, bien plus performant que Bind. Je laisse la
suite de l'article pour information, mais si vous voulez configurer le cache local, mieux vaut aller
[par ici](http://15minutesoffame.be/nico/blog2/index.php?article23/cache-dns-local-avec-dnsmasq).**

## Configuration de ouf : empêcher DNSCrypt de pourrir resolv.conf

Notez que DNSCrypt est un vicieux petit enculé, parce qu'il va automatiquement s'ajouter comme
serveur DNS sans que vous n'ayez rien à faire dans /etc/resolv.conf. Ça se passe dans /etc/init.d/dnscrypt-proxy :

```
...
            if [ -x /sbin/resolvconf ]; then
                echo "nameserver ${DNSCRYPT_PROXY_LOCAL_ADDRESS}" \
                    | cut -d ':' -f 1 \
                    | /sbin/resolvconf -a lo.dnscrypt-proxy
            fi
...
```

C'est pratique, mais c'est pas très cool, parce que ça va écraser la configuration que vous pourriez
faire via Network Manager par exemple. Un conseil : on va commenter ces lignes.

# Cache DNS : Bind

Utiliser un randomizer situé en Moldavie pour dispatcher ses requêtes à d'autres serveurs situés
partout dans le monde, c'est bien. Mais ça a un putain de coût en terme de performance.

Si je fais 10 requêtes DNS en passant par le DNS de Google, le temps par requête est environ 25 ms :

```
for i in {1..10}; do dig @8.8.8.8 youporn.com | grep time ; done
;; Query time: 27 msec
;; Query time: 26 msec
;; Query time: 25 msec
;; Query time: 25 msec
;; Query time: 33 msec
;; Query time: 24 msec
;; Query time: 26 msec
;; Query time: 28 msec
;; Query time: 21 msec
;; Query time: 26 msec
```

La même chose avec ma configuration DNSCypt :

```
for i in {1..10}; do dig @127.0.2.1 youporn.com | grep time ; done
;; Query time: 153 msec
;; Query time: 325 msec
;; Query time: 778 msec
;; Query time: 628 msec
;; Query time: 241 msec
;; Query time: 1768 msec
;; Query time: 86 msec
;; Query time: 201 msec
;; Query time: 217 msec
;; Query time: 173 msec
```

C'est moche... Très moche. Parfois plus d'une seconde et demi pour résoudre un nom de domaine, ça
sent la crevette moisie. On va s'installer un petit cache DNS pour améliorer tout ça, et on va faire
ça avec Bind.

## Installation

Là c'est du gâteau :

```
apt-get install bind9
```

Par défaut, le service va écouter sur l'adresse 127.0.0.1, port 53. Là aussi il suffit donc de
paramétrer cette adresse dans vos DNS (aussi en IPv6), et le tour est joué.

**Attention** : si vous utilisez Bind, il faut vraiment empêcher DNSCrypt de pourrir resolv.conf,
sinon ça va merder.

## Configuration

L'idée est que Bind va passer par DNSCrypt pour résoudre les adresses. Pour ça, on enfile ses
santiags et on va configurer `/etc/bind/named.conf.options` :

```
        forwarders {
                127.0.2.1;
        };
```

En clair, Bind va interroger DNSCrypt lorsqu'il ne connaît pas le nom de domaine à résoudre. Une
fois le nom résolu, il va utiliser son cache local. Et là, on va avoir une putain d'amélioration des
performances :

```
for i in {1..10}; do dig @127.0.0.1 youporn.com | grep time ; done
;; Query time: 3302 msec
;; Query time: 0 msec
;; Query time: 0 msec
;; Query time: 0 msec
;; Query time: 0 msec
;; Query time: 0 msec
;; Query time: 0 msec
;; Query time: 0 msec
;; Query time: 0 msec
;; Query time: 0 msec
```

La première requête est assez longue car on passe par Bind, qui appelle ensuite DNSCrypt. Mais
ensuite, ça passe comme dans du beurre car on utilise le cache local.
