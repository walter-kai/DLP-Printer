#include <String.h>

#define pulseX      (5)
#define directionX  (6)
#define enableX     (7)

String readString;
char* stringPointer;

void setup()
{
  pinMode(pulseX, OUTPUT);
  pinMode(directionX, OUTPUT);
  pinMode(enableX, OUTPUT);

  analogWrite(pulseX, 127);
  digitalWrite(directionX, HIGH);
 
  Serial.begin(115200);
  // initialize timer1 
  cli();           // disable all interrupts
  TCCR1A = 0;      // Clean the registers
  TCCR1B = 0; 


  TCCR1B |= (1 << CS12) | (1 << CS10); // Prescaler 1024
  TIMSK1 |= (1 << TOIE1);   // enable timer overflow interrupt
  sei();             // enable all interrupts
}


ISR(TIMER1_OVF_vect)        // interrupt service routine 
{
  digitalWrite(enableX, HIGH);
}


void loop()
{
  
  while (Serial.available()) {
    delay(3);  //delay to allow buffer to fill 
    if (Serial.available() >0) {
      
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    } 
  }

  if (readString.length() > 0) 
  {
    stringPointer = &readString[0];
    
    if(strstr(stringPointer, "M"))
    {
      digitalWrite(enableX, LOW);
    }
  }
}

