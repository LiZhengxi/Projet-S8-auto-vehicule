/* Nom: ultra-son + avancer 
*  Description : La voiture avance si la voiture rencontre les obstacles. La voiture va arrêter.
*  Date : 03.30
*  Version : 1.0
*/

#include <Servo.h>  //Utiliser le librairie interne d'arduino
#define Trig 2      //Pin Tring connecter avec IO D2
#define Echo 3      //Pin Echo connecter avec IO D3 
float cm;           //La distance capturer par le capteur ultra-son
Servo myservo;      // Creer un objet myservo(pour contrôler le servomoteur)
Servo moteurContinu;//Creer un objet moteurContinu(pour contrôler le moteur continu)

void setup() { 
  pinMode(Trig, OUTPUT);  
  pinMode(Echo, INPUT);
  myservo.attach(9);        // attaches the servo on pin 9 to the servo object
  moteurContinu.attach(8);  // attches the servo on pin 8 to the motor continue
  Serial.begin(9600);      // Configurer le baud-rate

   moteurContinu.write(1500);              // Initialiser le signal pour le moteur(1500: bouge pas)
   delay(2000);             // attendre 2s pour finir la inialisation
}

void loop() {
  //pour tourner à gauche : myservo.write(45);
  //pour tourner à droite : myservo.write(135);
  //au centre : myservo.write(0);
  //avancer en vitesse lante :moteurContinu.writeMicroseconds(1585);
  //reculer en vitesse lante :moteurContinu.writeMicroseconds(1350);
  digitalWrite(Trig, LOW); //envoyer un low('0') vers Trig
  delayMicroseconds(2);    //attends 2us
  digitalWrite(Trig,HIGH); //envoyer un high('1')
  delayMicroseconds(10);    //attends 10us
  digitalWrite(Trig, LOW); //remettre le trig à '0'
  
  temp = float(pulseIn(Echo, HIGH)); // stocker le tps de retour
  cm = (temp * 17 )/1000;           // conversion de temps de retour vers la distance
       Serial.println(cm);         //permet de lire la résulat sur le console
        if(cm>100)                  // si la distance est >1m, le robot avance
        {
         moteurContinu.writeMicroseconds(1585);      
        }
        else
        {    
               moteurContinu.writeMicroseconds(1500);              //sinon il va arrêter
        }
     delay(300);
  }


  


