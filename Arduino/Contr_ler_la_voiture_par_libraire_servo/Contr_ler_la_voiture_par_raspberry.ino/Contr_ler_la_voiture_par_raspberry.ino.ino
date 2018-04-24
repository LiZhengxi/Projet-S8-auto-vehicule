#include <Servo.h>  //Utiliser le librairie interne d'arduino
#define Trig 2      //Pin Tring connecter avec IO D2
#define Echo 3      //Pin Echo connecter avec IO D3 
float cm;           //La distance capturer par le capteur ultra-son
float temp;
Servo myservo;      // Creer un objet myservo(pour contrôler le servomoteur)
Servo moteurContinu;//Creer un objet moteurContinu(pour contrôler le moteur continu)
const int ledPin = 13;
char info;
char info1;
void setup(){
  pinMode(ledPin, OUTPUT);
  pinMode(Trig, OUTPUT);  
  pinMode(Echo, INPUT);
  myservo.attach(9);        // attaches the servo on pin 9 to the servo object
  moteurContinu.attach(8);  // attches the servo on pin 8 to the motor continue
  Serial.begin(250000);      // Configurer le baud-rate
  moteurContinu.write(1500);
  delay(4000);
}

void loop(){
   //给Trig发送一个低高低的短时间脉冲,触发测距
  digitalWrite(Trig, LOW); //给Trig发送一个低电平
  delayMicroseconds(2);    //等待 2微妙
  digitalWrite(Trig,HIGH); //给Trig发送一个高电平
  delayMicroseconds(10);    //等待 10微妙
  digitalWrite(Trig, LOW); //给Trig发送一个低电平
  
  temp = float(pulseIn(Echo, HIGH)); //存储回波等待时间,
  //pulseIn函数会等待引脚变为HIGH,开始计算时间,再等待变为LOW并停止计时
  //返回脉冲的长度
  
  //声速是:340m/1s 换算成 34000cm / 1000000μs => 34 / 1000
  //因为发送到接收,实际是相同距离走了2回,所以要除以2
  //距离(厘米)  =  (回波时间 * (34 / 1000)) / 2
  //简化后的计算公式为 (回波时间 * 17)/ 1000
  
  cm = (temp * 17 )/1000; //把回波时间换算成cm
  if(cm<20)
  {
    moteurContinu.writeMicroseconds(1500);
  }
  
 else{
if (Serial.available()) {
  info=Serial.read();
   if(info=='i')
{ moteurContinu.writeMicroseconds(1500);
 
}
  else if(info=='m')
{ moteurContinu.writeMicroseconds(1500);
 myservo.write(135);
}
/*
else if(info=='a')
{
  myservo.write(90);
  moteurContinu.writeMicroseconds(1595);
}*/
/*
else if(info=='r')
{
  myservo.write(75);
}
else if(info=='l')
{
  myservo.write(115);
}
*/
/*else if(info=='p')
{ 
  if(info1!='p')
  {
  moteurContinu.writeMicroseconds(1350);
  delay(3000);
  moteurContinu.writeMicroseconds(1600);
  delay(2000);
}
}
*/
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
  moteurContinu.writeMicroseconds(1600);

}
else
{ 
  moteurContinu.write(1350);
}
info1=info;
}
 }
}

