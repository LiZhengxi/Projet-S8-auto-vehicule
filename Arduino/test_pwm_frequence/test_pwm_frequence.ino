int pinMS = 6;//pin pour commander le servo moteur
int pinMC = 5;//pin pour commander le moteur continue   
int pinIF=0;//pin A0
int i;
int val;
void setup()  
{   pinMode(pinIF,OUTPUT);
    pinMode(pinMC, OUTPUT);
    pinMode(pinMS, OUTPUT);  
    Serial.begin(9600);
    TCCR0B = TCCR0B & 0xF8 |5; //Reconfigurer le timer 0(changer la fréquence sur les PWM en PIN5 , 6. Par contre il va changer le temps de delay() )
    analogWrite(pinMC, 24);   //16 pour 1ms, 32 pour 2ms, 24 pour 1.5ms
    analogWrite(pinMS, 24);
}     
void loop()  
{  
  i=analogRead(pinIF);
  Serial.println(i);
  if(i<500)
  {
    analogWrite(pinMC,16);
  }
  else
  {
    analogWrite(pinMC,32);
  }
  delay(100);
 
}


