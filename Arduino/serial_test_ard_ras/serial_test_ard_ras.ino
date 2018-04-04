#include <Servo.h>  //Utiliser le librairie interne d'arduino
#define Trig 2      //Pin Tring connecter avec IO D2
#define Echo 3      //Pin Echo connecter avec IO D3 
float cm;           //La distance capturer par le capteur ultra-son
Servo myservo;      // Creer un objet myservo(pour contrôler le servomoteur)
Servo moteurContinu;//Creer un objet moteurContinu(pour contrôler le moteur continu)
const int ledPin = 13;
char info;

void setup(){
  pinMode(ledPin, OUTPUT);
  pinMode(Trig, OUTPUT);  
  pinMode(Echo, INPUT);
  myservo.attach(9);        // attaches the servo on pin 9 to the servo object
  moteurContinu.attach(8);  // attches the servo on pin 8 to the motor continue
  Serial.begin(9600);      // Configurer le baud-rate
  moteurContinu.write(1500);
  delay(4000);
}

void loop(){
  
if (Serial.available()) {
  info=Serial.read();
   if(info=='i')
{ moteurContinu.writeMicroseconds(1500);
 
}
else if (info=='q')
{
  myservo.write(125); 
}
else if(info=='d')
{
   myservo.write(65);
}
else if(info=='c')
{
  myservo.write(90);
}

else if(info=='z')
{
   moteurContinu.writeMicroseconds(1585);

}

else if(info=='i')
{ moteurContinu.writeMicroseconds(1500);
 
}
else
{ 
  moteurContinu.writeMicroseconds(1350);
}

}
}

