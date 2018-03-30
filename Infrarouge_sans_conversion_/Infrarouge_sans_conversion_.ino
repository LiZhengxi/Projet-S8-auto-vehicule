
void setup()
{
  pinMode(5,OUTPUT);
 TCCR0B = TCCR0B & 0xF8 | 1024;
 analogWrite(5, 32);
}
void loop()
{
}

