# Projet-S8 Système visuel de véhicule autonome

## Présentation de la voiture autonome 
L’école a choisi de mettre à notre disposition une voiture radiocommandé tout terrain électrique 1/10 -ème avec un émetteur à volant Absima CR2S.V2 déjà monté. La voiture nous a été livrée avec un pack Ni-Mh de 1800 mA. Celui-ci devra être chargé durant 4heures à l’aide du chargeur d’origine pour pouvoir profiter pleinement des différentes fonctionnalités de la voiture. La voiture est fournie avec une mécanique pré montée. Ce qui sous-entend quel n’a pas été choisi au hasard par l’école, vu l’objectif de mettre en place de l’électronique embarquée de notre part. La vitesse
maximale de la voiture est de 40 km/heures mais il sera difficile pour nous de la faire rouler à une telle vitesse sachant qu’elle devra détecter certains objets et que l’environnement choisie ne nous le permet pas. La voiture devra subir quelques modifications de notre part pour pouvoir rouler en toute 
![Vehicule](https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/Vehicule.jpg)
<img src="https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/Vehicule.jpg" width = "500"> 

## Présentation du matériel 
<img src="https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/materiel.png" width = "500"> 

## Logiciels utilisés
* Python 
* openCV(library)
* Tensorflow(traitement le panneu stop et les feux)
* Langage C/C++(arduino) 
* Soliworks(imprimant 3D) 
* Egale (Carte électronique)

<br>

<img src="https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/feux.png" width = "500"> 

## Travail en équipe
Nous avions choisi pour cela l’application Trello qui est un outil de gestion de projet en ligne. Il est basé sur une organisation des projets en planches listant des cartes, 
chacune représen-tant des taches que nous devions réaliser au fur et à mesure.
<img src="https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/trello.png" width = "500"> 

## Détection panneau stop et feux de signalisation
Au niveau de détection de panneau stop ou le feux, nous avons utilisé le même stratégie.
Tout d'abord, nous avons cherché la partie en rouge sur chaque photo. Une fois notre program détecte qu'il y 
a une partie en rouge de sufarce supérieur à un certain valeur. Le programme va considéré qu'il y a soit le panneau
soit le feux rouge.<br> 
Le prétraitement d'image est fait par openCV. Et la partie suivant est par une modèle de tensorflow qu'on a entrainné en avant. Et ce modèle va appliquer sur la partie qu'on a détecté en rouge. Et le programme va juger si c'est un panneau ou pas. Si c'est un panneau, la voiture va arrêter pendant 5s après redémarrer. Sinon, c'est-t-à dire forcément c'est le feux rouge. Donc, la voiture va attendre le feux vert allume et redémarrér 
#### Détection panneau stop

<img src="https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/feux.jpg" width = "500"> 
#### Détection feux de signalisation
<img src="https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/Panneur.jpg" width = "500"> 
## Détection le trajectoire
#### Recherché la ligne 
Cette méthode est un peu limitée parce qu’il ne peut que détecter les lignes d’une seule couleur. De plus, le résultat obtenu sera aussi perturbé par les autres objets qui ont le même couleur que la ligne. 2-1) Compter le nombre pixel 
Une fois, les traitements de couleur sont faits, nous pouvons compter le nombre pixel de certain couleur d’une image. Si celui à gauche est plus, la voiture va tourner à gauche, si-non à droite. Mais cette méthode n’est pas possible de faire sur le Raspberry. Comme la performance de Raspberry n’est pas assez pour traiter tous les pixels de chaque image. Nous avons testé le programme c’est super lent. Du coup, nous avons abandonné.


#### Chercher le barycentre 	
Cette fois-ci nous utilisons la même méthode de traitement image. Mais au lieu de calculer le nombre de pixel, nous cherchons le barycentre de contour que nous avons trouvé. Puis, commander la voiture d’après le barycentre.

#### Décider la direction 
1) Sélectionner trois régions intéresser (ROI) puis analyser le barycentre de chaque région
<img src="https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/3barrycentre.jpg" width="500" > 
2) Comparer avec les barycentres en précédent 
<img src="https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/ligne.png" width = "500"> 
3) Comparer les deux résultats et choisit le meilleur direction 