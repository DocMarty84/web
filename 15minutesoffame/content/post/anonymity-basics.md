+++
title = "Quelques éléments de cryptographie"
date = "2009-05-17T03:00:00+02:00"
tags = ["anonymat"]
archives = "2009"
type = "article"
+++

Avec le développement de l'informatique et d'Internet, l'anonymat et la sécurité sur la toile sont
de plus en plus récurrents. Que ce soit au sujet de la protection de leurs données, de la
correspondance privée, de la constitution d'un profil sur base des traces laissées sur la toile
(voir le [portrait d'un internaute par le journal Le Tigre](http://www.lexpress.fr/actualite/high-tech/le-portrait-google-qui-met-le-feu-a-la-toile_732230.html)) ou du partage de musique ou films via les
logiciels de peer-to-peer (eMule ou Bittorrent), beaucoup d'internautes (à mon avis, pas encore
suffisamment ;-) ) commencent à prendre conscience que se trouver derrière un écran ne les rend pas
anonyme.

Dans les prochains articles, nous traiterons de l'anonymat et de la sécurité dans divers sujets :

*   les données personnelles (disque dur, clés USB...). Les clés USB, les disques durs externes ou
    même les PC portables étant des supports susceptibles d'être facilement volés ou perdus, il est
    nécessaire de protéger certaines données privées.
*   la correspondance privée (e-mails ou messagerie instantanée). On ignore souvent que les e-mails
    sont scannés à plusieurs reprises lorsqu'ils transitent, que ce soit par le fournisseur d'accès
    à Internet (FAI) ou par le service mail utilisé (Gmail, Hotmail, La Poste...).
*   les informations laissées sur la toile de manière délibérée ou à l'insu de l'utilisateur. Outre
    les sites communautaires comme Facebook, Orkut, Myspace ou Twitter où les utilisateurs
    fournissent délibérément des informations personnelles, n'importe quel site web peut connaitre
    l'endroit où vous vous trouvez, le site que vous venez de visiter ou encore votre FAI. Via les
    cookies, les sites web peuvent également connaitre vos habitudes en vous identifiant à chaque
    visite.
*   le partage de culture, ou piratage selon certains, via des logiciels tels qu'eMule ou Bittorent.
    La récente loi [HADOPI](http://fr.wikipedia.org/wiki/Loi_Hadopi) ainsi que la condamnation des
    créateurs du site
    [The Pirate Bay](http://www.ecrans.fr/The-Pirate-Bay-condamne-mais-le,6971.html) suscitent en
    effet l'inquiétude de nombreuses personnes.

Le point commun à la sécurité informatique est l'utilisation de la cryptographie, et sera donc le
sujet de ce premier article.

# La cryptographie, mais qu'est-ce donc ?

La cryptographie est une discipline s'attachant à protéger des messages en les modifiant de manière
telle qu'il soit difficilement compréhensible. Donnons un petit exemple en chiffrant le mot
"bonjour". Nous pouvons tout d'abord attribuer à chaque lettre sa position correspondante dans
l'alphabet, ce qui donnerait "2 15 14 10 15 21 18". C'est une première étape, mais il est assez
facile de décoder le message.

Pour compliquer la tâche, nous pouvons appliquer l
 [chiffre de César](http://fr.wikipedia.org/wiki/Chiffre_de_C%C3%A9sar) qui consiste à ajouter un
 nombre quelconque à chaque lettre du message. Il suffira au correspondant de soustraire le nombre
 ajouté pour déchiffrer le message. Si nous ajoutons par exemple 3, "2 15 14 10 15 21 18" devient
 donc "5 18 17 13 18 24 21" ce qui correspond à "erqmrxu" Cependant, chaque langue a ses lettres les
 plus utilisées (en français, le E et le R). Dès lors, en analysant l'occurrence de chaque lettre
 dans le message il est assez facile de "casser" le chiffrement.

Nous pouvons encore compliquer le chiffrement en introduisant la notion de clé. Au lieu d'ajouter 3,
nous pouvons ajouter alternativement 1 et 2. "2 15 14 10 15 21 18" devient "3 17 15 12 16 23 19",
donc "cqolpws". Il est alors nettement plus difficile de déchiffrer ce message, car il est inutile
d'analyser l'occurrence de chaque lettre. Plus la clé ("1 2" dans notre cas) sera longue, plus il
sera difficile de déchiffrer le message. C'est le principe du chiffrement symétrique.

# Chiffrement symétrique

Les algorithmes de chiffrement symétrique se fondent sur une même clé pour chiffrer et déchiffrer un
message, à l'image de l'exemple précédent. D'un point du vue imagé, ce chiffrement fonctionne comme
un coffre-fort classique où une clé est nécessaire pour l'ouvrir ou le fermer.

De [nombreux algorithmes](http://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Algorithme_de_cryptographie_sym%C3%A9trique)
existent et font appel à des opérations mathématiques plus ou moins compliquées qu'il est inutile de
détailler ici. Citons par exemple
[AES](http://fr.wikipedia.org/wiki/Standard_de_chiffrement_avanc%C3%A9),
[Blowfish](http://fr.wikipedia.org/wiki/Blowfish) ou
[Serpent](http://fr.wikipedia.org/wiki/Serpent_(cryptographie)) qui utilisent des clés de 128, 192
ou 256 bits. A l'instar de notre chiffrement basique, plus la clé est longue et plus il est
difficile de casser le chiffrement ; cependant, le temps de chiffrement augmente avec la taille de
la clé (les processeurs actuels permettent toutefois de traiter rapidement des quantités de données
importantes). Un avantage de ces algorithmes est de produire une chaine de caractère plus longue que
la chaine initiale. Par exemple, chiffrer symétriquement "bonjour" peut donner (selon l'algorithme
utilisé et le mot de passe) :

```
jA0EAwMCTuvQ66Iz1DZgyR2e9lZQpZoNqXQ4sJwpThRx7sY1jvukhaIAGiNgLA==
=NrNU
```

L'inconvénient principal de ce type de chiffrement est qu'il faut pouvoir faire passer la clé de
chiffrement à son correspondant de manière sure. De plus, dans l'idéal il est nécessaire d'utiliser
une clé par correspondant. Ces points faibles ont entrainé la nécessité du chiffrement asymétrique.

Le chiffrement symétrique est très bien adapté pour la protection de données qui ne sont pas
destinées à être échangées. Le chiffrement étant assez rapide, il est par exemple possible de
chiffrer des disques durs entiers en ayant un impact relativement faible sur les performances de
lecture ou d'écriture.

# Chiffrement asymétrique

Les algorithmes de chiffrement asymétrique fonctionnent avec deux clés : une clé pour chiffrer et
une clé pour déchiffrer un message. Ces deux clés sont mathématiquement liées, et à une clé publique
correspond une seule clé privée. Ce chiffrement fonctionne comme un coffre-fort pour lequel une clé
permettrait de le fermer et une autre pour l'ouvrir.

La force de
l'[algorithme](http://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Algorithme_de_cryptographie_asym%C3%A9trique)
([RSA](http://fr.wikipedia.org/wiki/Rivest_Shamir_Adleman) ou
[ElGamal](http://fr.wikipedia.org/wiki/Cryptosyst%C3%A8me_de_ElGamal) par exemple) tient dans la
difficulté de déduire la clé de déchiffrement (clé privée) à partir de la clé de chiffrement (clé
publique). En effet, il est en théorie possible de déduire une clé privée à partir de la clé
publique, mais c'est en pratique excessivement long (plusieurs centaines voire milliers d'années).
Il est nécessaire d'utiliser des clés de taille nettement supérieure aux clés utilisées pour le
chiffrement symétrique. 1024 bits est un minimum, 2048 bits est recommandé et 4096 bits est l'idéal.
Chiffrer "bonjour" avec une clé de 4096 bits peut donner :

```
hQQOAwa2rcfSQVdeEA//RyJ9gO0QBGU5S7nxIZ/lGK0nWi1uYGIPS/hyZfiemp5P
9/AJup4rQ6fpbOWzQUv+fIU4+oQWUtd5YxfsRL1Lx3GJ78XKa2w5Hz/+z5U9vfVH
/cxEjoC1tyX3nL/OHAM8W2rER2yUQQ4TXkHr3xo8bElkVxmw5KAJV+BQFK6CNXKp
e7y8YY79ZCYF9tqf1b/Y/neR6IGMIwDdi4kM9dF6WEPg7IU7OCxFHA2m6wxtyifl
mXjvaRF5h1wmf+CkAXpSJ/CwmBihWMUDOMtK8sBDq3ie0kEok1BigSZZtOWmcgkM
ZKMVNl7Aul53cKWAKh7KE4kQ2mVtbkZOKTRFr+33PkJeVaMNJRml4l/SGSOnOThI
6qfuJMcYKj9sZp3zlDHRbKwgZRhdhBuot4TS3u9U4ew6jkAdXJac7z56m33djCtu
fMlfpzxttyTwhiDzkxyj7vFzN671O5wqvnRo1YdOHDtaxwdGIWJR7sd1Y7JnnzmJ
QgyAZ/utS7Kd3gSytfGJZGCHvw9c5GbiF9oDwPahY1tcQBKgnJsN4M3VytYRoQR1
kStUg4fjYdI+MBAqVvbzc3GvYfNNbAeuq4zbMLD/0GCrqM4mWHZ/G7IL/FDi4tov
3R4WpZPJQyWk5qZaiNQWs8cEiWpnP7Y/x7oyloORCTjl6+8v9GiuJsqTpjbshEoP
/RkbT/HhohadU6dpTGCAFz88geGmJXA4espa+6i9ldAT48uhVBrp/WkbhrpHqfsP
kxWRPGfrWcmaYe5/BFNTMWP6k623/mGDf3XDUwRU3ADWyfl05/SGStE2Jhi/P+2O
JHtdcL6EatWyuuZwTmNM43H3kROvXyqmaAcSqJMD91tdkochSnYzml1fCk+yhpru
e9orcpU+uzTe1xg/anm7cSDmbeQwa8yfpzakHex8E6zeARpC7hPp9FPuvNWjIUH6
iuV5SF1LX0XdFVQyOq4AwN+wOLfRpBzbWKCB+xURdcQOK7QHP2MzH1GoOb8fIiEX
yFk5TDlC/GL9x6w2L83JvAR30vofu5sBxWWgSKfsYq6TTyShl9B+wiXMd22iwTXI
t4bGW9ftL0BOr0jUrN3lKgmByiNsDFmrDk6hIWzL3UL0Z/w24pBbd2p7eKOvBQPY
4up45euVOhDEUeaebhco44arrQ0kVDS2r6xiG3MYEhA57KObpAA2sEjcz+ALt0Nf
BTfimKV83wv12172bsSb3YTqTwV85JwpXu/Fp2QwCj12uilBWiX+Z3GSP4kxuwKb
dRYIBucBa0fFOa31jOuMPLPQCK4iTeiZ/SPQqGsOO/dl8tE9zb4CmyE2L3bxGjNo
9QgdYudKZHD4dMKRrGOSUTiuHcKcmh0VvllhxxKz/NNW0kIBZbFWsnRPiDknaGrb
h1ln3mXAvcNEUu0UXpH3maJO9a55Y3TIoGCo+6zqvEQjUSz9GINg75FTSzAWnTnL
V8tf+o4=
=GqSt
```

Une clé plus courte donnera un résultat plus court, comme on pourrait s'en douter ;-) .

L'avantage est qu'on peut sans problème fournir la même clé publique à tous ses contacts sans
précautions particulières, vu qu'il est presque impossible d'en déduire la clé privée. En
contrepartie, le temps de chiffrement est assez long. Le chiffrement asymétrique est donc bien
adapté pour la correspondance (pour des textes simples, le chiffrement est instantané) mais pas pour
des données plus importantes (images, vidéos...).

# Conclusion

Les méthodes de chiffrement présentées ci-dessus peuvent être appliquées à n'importe quel type de
données, et pas seulement à du texte. Il est donc tout à fait possible de faire du peer-to-peer
chiffré, ou de naviguer sur le web sans que personne ne puisse avoir accès aux données consultées, y
compris votre FAI. Il est cependant nécessaire de ne pas mélanger sécurité et anonymat : la sécurité
(liée au chiffrement) vous permet de faire transiter vos données sans que personne ne puisse y
accéder, alors que l'anonymat vous permet de faire transiter des données de telle manière qu'il soit
très difficile de savoir qui en sont l'expéditeur et le destinataire. Nous tenterons de combiner au
mieux ces deux aspects.

**A suivre, partie 2 : [protéger ses données personnelles](http://15minutesoffame.be/nico/blog2/?article10/proteger-ses-donnees-personnelles).**
