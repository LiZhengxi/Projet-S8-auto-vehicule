# Projet-S8-Système visuel de véhicule autonome

## Présentation de la voiture autonome 
L’école a choisi de mettre à notre disposition une voiture radiocommandé tout terrain électrique 1/10 -ème avec un émetteur à volant Absima CR2S.V2 déjà monté. La voiture nous a été livrée avec un pack Ni-Mh de 1800 mA. Celui-ci devra être chargé durant 4heures à l’aide du chargeur d’origine pour pouvoir profiter pleinement des différentes fonctionnalités de la voiture. La voiture est fournie avec une mécanique pré montée. Ce qui sous-entend quel n’a pas été choisi au hasard par l’école, vu l’objectif de mettre en place de l’électronique embarquée de notre part. La vitesse
maximale de la voiture est de 40 km/heures mais il sera difficile pour nous de la faire rouler à une telle vitesse sachant qu’elle devra détecter certains objets et que l’environnement choisie ne nous le permet pas. La voiture devra subir quelques modifications de notre part pour pouvoir rouler en toute 
![Vehicule](https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/Vehicule.jpg)

## Présentation du matériel 
![Materiel](https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/materiel.png)

## Logiciels utilisés
* Python 
* openCV(library)
* Tensorflow(traitement le panneu stop et les feux)
* Langage C/C++(arduino) 
* Soliworks(imprimant 3D) 
* Egale (Carte électronique)

<br>

![Feux](https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/feux.png)


## Travail en équipe
Nous avions choisi pour cela l’application Trello qui est un outil de gestion de projet en ligne. Il est basé sur une organisation des projets en planches listant des cartes, 
chacune représen-tant des taches que nous devions réaliser au fur et à mesure.
![Trello](https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/trello.png)


## Détection panneau stop et feux de signalisation
Au niveau de détection de panneau stop ou le feux, nous avons utilisé le même stratégie.
Tout d'abord, nous avons cherché la partie en rouge sur chaque photo. Une fois notre program détecte qu'il y 
a une partie en rouge de sufarce supérieur à un certain valeur. Le programme va considéré qu'il y a soit le panneau
soit le feux rouge.<br> 
Le prétraitement d'image est fait par openCV. Et la partie suivant est par une modèle de tensorflow qu'on a entrainné en avant. Et ce modèle va appliquer sur la partie qu'on a détecté en rouge. Et le programme va juger si c'est un panneau ou pas. Si c'est un panneau, la voiture va arrêter pendant 5s après redémarrer. Sinon, c'est-t-à dire forcément c'est le feux rouge. Donc, la voiture va attendre le feux vert allume et redémarrér 
![Feux detection](https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/feux.jpg)
![Panneur detection](https://github.com/LiZhengxi/Projet-S8-auto_vehicule/blob/master/Panneur.jpg)