/*
 *  name: Arduino 
 *  date : 2018.04.20
 *  autheur : LiZhengxi
 *  comment : arduino receive the information sended by the raspberry and command 2 moteurs to do different things
 *  and also, receive the information from the ultrason 
 */
#include <Servo.h>  //Use the internal librairie ofarduino
#define Trig 2      //Pin Tring connect with IO D2
#define Echo 3      //Pin Echo connect with IO D3 
float cm;           //distance of the objet
float temp;         //time for the ultrason receive information
Servo myservo;      // creat an objet myservo(for the servomoteur)
Servo moteurContinu;//Creat an objet moteurContinu(for the DC motor)
const int ledPin = 13;
char info;        //information received
char info1;       //information received previously
void setup(){
  /*
   * initialize the pin and the communication between raspberry and arduino
   */
  pinMode(ledPin, OUTPUT);
  pinMode(Trig, OUTPUT);  
  pinMode(Echo, INPUT);
  myservo.attach(9);        // attaches the servo on pin 9 to the servo object
  moteurContinu.attach(8);  // attches the servo on pin 8 to the motor continue
  Serial.begin(250000);      // Set the baud-rate
  moteurContinu.write(1500);
  delay(4000);            //give some time for the arduino initialize the DC motor
}

void loop(){
   //This code explain how the ultrason works
  digitalWrite(Trig, LOW); //Send Trig a low level voltage
  delayMicroseconds(2);    //wait for 2ms
  digitalWrite(Trig,HIGH); //Send Trig a high level voltage
  delayMicroseconds(10);    //wait for 10ms
  digitalWrite(Trig, LOW); //Send Trig a low level voltage
  
  temp = float(pulseIn(Echo, HIGH)); //stocke the return time 
  //when the function pulseIn is HIGH,begin to record the time,waiting to the LOW stop the record
  
  //sound velocity:340m/1s conversion: 34000cm / 1000000μs => 34 / 1000
  //the time record sending  and receiving,in fact is the same distance for 2 times,so /2
  //distance(cm)  =  (time * (34 / 1000)) / 2
  //so (time * 17)/ 1000
  
  cm = (temp * 17 )/1000; 
  /*
   * if the distance <20cm, the car will stop
   * else the car will move according to the raspberry
   */
  if(cm<20)
  {
    moteurContinu.writeMicroseconds(1500);
  }
  
 else{
  /*
   * check the bus is available
   * 
   * comment : 
   * for the servomotor : myservo.write(x);
   * x=90 in center
   * x=45 turn left
   * x=135 turn right
   * for the dc motor : moteurContinu.writeMicroseconds(y);
   * y=1500 stop
   * y=1595 advance
   * y=1350 come back
   */
if (Serial.available()) {
  info=Serial.read();
   if(info=='i')
{ moteurContinu.writeMicroseconds(1500);
 
}
  else if(info=='m')
{ moteurContinu.writeMicroseconds(1500);
 myservo.write(135);
}

else if(info=='f')
{
  moteurContinu.writeMicroseconds(1500);
}

else if (info=='q')
{
  myservo.write(135); 
}
else if(info=='d')
{
   myservo.write(45);
}
else if(info=='c')
{
  myservo.write(90);
}

else if(info=='z')
{
  moteurContinu.writeMicroseconds(1595);

}
else
{ 
  moteurContinu.write(1350);
}
}
 }
}

