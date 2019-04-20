+++
title = "Cache DNS local avec Dnsmasq"
date = "2015-08-02T03:00:00+02:00"
tags = ["dns", "dnscrypt", "anonymat", "dnsmasq"]
archives = "2015"
type = "article"
+++

Dans [un article précédent](/nico/blog2/index.php?article22/securiser-ses-dns-dnscrypt-et-cache-local-avec-bind),
nous avons vu comment configurer DNSCrypt combiné à un cache local géré par Bind. Un gentil
commentateur m'a indiqué l'existence de Dnsmasq, qui semble en effet plus adapté.

Suite à l'article concernant
[la sécurisation des DNS](/nico/blog2/index.php?article22/securiser-ses-dns-dnscrypt-et-cache-local-avec-bind),
un lecteur (AP) m'a pointé Dnsmasq comme alternative à Bind. J'étais déjà tombé dessus lors de mes
recherches de cache DNS, mais sa capacité à faire serveur DHCP et TFTP m'avait rapidement détourné
de lui. Honte à moi, j'aurais dû creuser plus que 3 minutes.

L'intérêt principal par rapport à Bind est sa légèreté. Bind est une référence en terme de serveur
DNS, mais c'est le canon pour tuer la mouche. Dnsmasq, simplement configuré, permet de jouer
efficacement le rôle de cache DNS. Petit bonus : il s'intègre très bien avec Resolvconf et DNSCrypt.
Dans [cet article](http://www.drazzib.com/docs/admin/dnsmasq.html), on y apprend que Resolvconf va
fournir à Dnsmasq les serveurs de noms (nameserver) externes. En effet, Resolvconf va générer un
fichier spécifique (`/var/run/dnsmasq/resolv.conf`) qui contient l’ensemble des adresses des
serveurs de noms. Dnsmasq va utiliser automatiquement ce fichier à la place du classique
`/etc/resolv.conf`. Et ça, c'est très bien quand on utilise DNSCrypt : en effet, le script `init.d`
de DNSCrypt va utiliser Resolvconf pour s'annoncer en tant que serveur de noms. Du coup, il ne
faudra plus modifier ce script init.d comme avec Bind. Youpi !

Si vous voulez combiner DNSCrypt et Dnsmasq, vous pouvez suivre l'
[article précédent](/nico/blog2/index.php?article22/securiser-ses-dns-dnscrypt-et-cache-local-avec-bind)
jusqu'au point "Configuration avancée : serveur DNS aléatoire" inclus, puis continuer cet article.

# Installation

Une vraie promenade de santé :

```
apt-get install dnsmasq
```

Par défaut, le service va écouter sur l'adresse 127.0.0.1, port 53. Il suffit donc de paramétrer
cette adresse dans vos DNS (aussi en IPv6), et le tour est joué.

**Attention** : par défaut, Bind utilise la même adresse/port. Il vous faudra donc soit virer Bind,
soit changer l'interface de l'un ou l'autre.

# Configuration

La configuration se trouve dans "/etc/dnsmasq.conf". Sous Ubuntu, le fichier est déjà très complet,
et entièrement commenté. On va dé-commenter uniquement ces lignes :

```
domain-needed
bogus-priv
expand-hosts
cache-size=500
```

Explication des paramètres utilisés :

*   **domain-needed** : ne transmet pas les requêtes ne contenant pas un nom de domaine complet. Par
    exemple, "google" ne sera pas transmis aux serveurs de noms, alors que "google.com" le sera.
*   **bogus-priv** : fausse résolution inverse pour les réseaux privés. Toutes les requêtes DNS
    inverses pour des adresses IP privées (par exemple 192.168.x.x) qui ne sont pas trouvées dans
    `/etc/hosts` ou dans le fichier de baux DHCP se voient retournées une réponse "pas de tel
    domaine" au lieu d’être transmises aux serveurs de noms.
*   **expand-hosts** : utilise le contenu de `/etc/hosts`.
*   **cache-size=500** : augmente la taille du cache DNS à 500 entrées au lieu de 150 par défaut.

Il suffit de redémarrer le service. On peut aussi vérifier que le serveur DNSCrypt, par défaut
127.0.2.1, est bien utilisé dans `/var/run/dnsmasq/resolv.conf`. Si vous n'utilisez pas DNSCrypt,
vous pouvez utiliser le paramètre `server=` pour indiquer les serveurs de noms à utiliser, par
exemple 8.8.8.8 pour celui de Google.

On va tester l'efficacité de notre cache :

```
for i in {1..10}; do dig youporn.com | grep time ; done
;; Query time: 169 msec
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

C'est même nettement moins que ce qu'on obtenait avec Bind pour la première requête : avec cette
configuration, la première requête prend moins de 200 ms, alors qu'avec Bind on en était à plus de
2 secondes.
