+++
title = "Streaming auto-hébergé : KooZic, un nouveau venu"
date = "2016-10-08T03:00:00+02:00"
tags = ["odoo", "streaming"]
archives = "2016"
type = "article"
+++

En marge des services tels que Spotify, Deezer ou LastFM, certains irréductibles préfèrent garder la
main sur leur collection musicale et y accéder à distance via un serveur de streaming auto-hébergé.

# Solutions actuelles

Dans les gros bonnets, on trouve Subsonic et Ampache. Subsonic était libre et open-source jusqu'en
version 5, puis est passé du côté closed-source de la force à partir de la version 6. J'ai longtemps
utilisé Subsonic, en tous cas en version 5. Et puis j'ai tenté la version 6, et j'ai déchanté. J'ai
été affecté par [ce bug](http://forum.subsonic.org/forum/viewtopic.php?f=2&t=12583), et le manque de
réactivité de l'auteur m'a fait quitté le sous-marin. Le bug ? Un détail... La musique ne s'ajoute
plus dans la collection. Un peu emmerdant pour un logiciel de streaming musical d'être incapable
d'ajouter le moindre morceau dans la collection...

J'aurais pu rester sur la version 5, mais cette expérience m'a refroidi. J'ai donc été voir
ailleurs, chez Ampache. Je ne suis probablement pas objectif là-dessus, mais j'ai pas aimé. Après
avoir galéré pour installer et configurer le tout, j'ai trouvé l'interface fouillie, et remplie
d'options dont je n'ai pas compris l'intérêt. Bref, j'ai passé 2 heures à l'installer, le
configurer, puis après 30 minutes de test, j'ai tout viré. Donc ouais, je suis pas objectif sur
Ampache...

Chez les challengers, CherryMusic et Sonerezh creusent petit à petit leur réputation. J'ai accroché
quelques jours sur CherryMusic, moins abouti que Subsonic, mais centré sur l'essentiel. Avec son
interface rapide et simple, je me suis dit que je pourrais peut-être contribuer au projet proposant
le support de l'API Subsonic. Et en creusant dans le code, j'ai déchanté... J'avoue ne pas avoir
installé Sonerezh, mais la perspective de devoir me farcir à nouveau l'installation/configuration
d'un serveur web m'a un peu refroidi. Pour ce que j'en ai vu sur serveur de démo, l'interface est
plutôt jolie et rapide. A voir si il tient la charge avec une collection de plusieurs milliers de
titres et l'utilisation lorsqu'on a une collection musicale moyennement bien organisée.

# Et si je faisais mon propre truc ?

Le point commun négatif à tous ces projets, c'est le support moyen (Subsonic, Sonerezh) voire
inexistant (CherryMusic) des tags ID3. D'accord, les infos sont toujours disponibles d'une manière
ou d'une autre, mais quand on veut filtrer ou trier dessus, c'est mort. Je veux la liste de mes
albums de jazz ? Filtrer par artiste et trier par date ? Pas possible via la recherche, quelque soit
le soft.

Avec une vie professionnelle et personnelle déjà bien chargée, il était exclu de me lancer dans un
projet "from scratch". Ce genre de projet qui requiert déjà plusieurs centaines d'heures de travail
avant d'obtenir quelque chose de vaguement utilisable aurait fini aux oubliettes au bout de quelques
semaines. Je suis donc parti sur une base que je connais, à savoir Odoo (anciennement OpenERP), et
j'ai créé mon propre module. Avec cette approche, je suis parvenu à un résultat viable en quelques
dizaines d'heures de travail. L'avantage est clairement la rapidité de développement, avec la
disponibilité out-of-the-box d'un moteur de recherche puissant, la gestion d'utilisateurs, droits
d'accès ou encore tâches automatisées (cron), sous une interface utilisateur sobre mais efficace.

Et comme ça est né KooZic, qui sera présenté plus en détails dans un prochain article.
