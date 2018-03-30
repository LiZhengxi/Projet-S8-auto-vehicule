int i;
int val;
int redpin=0;
void setup()
{
  pinMode(redpin,OUTPUT);
  Serial.begin(9600);
}
void loop()
{
  i=analogRead(redpin);;
  Serial.println(i);
  delay(100);
}

