#include <String.h>

const int pulseX = 5;
const int directionX = 6;
const int enableX = 7;

const int pulseY = 8;
const int directionY = 9;
const int enableY = 10; 

const int counter = 4;

////Variables//////
String readString;
char* stringPointer;
int stepsPerRevolution = 3200;
int stepsPerMicroMeter = 415;
///////////////////

///////////
// Negative is outwards X-1000 ie. outwards 1mm
// Positive is inwards X1000 ie. inwards 1mm
///////////

void setup()
{
  pinMode(pulseX, OUTPUT);
  pinMode(directionX, OUTPUT);
  pinMode(enableX, OUTPUT);
  pinMode(pulseY, OUTPUT);
  pinMode(directionY, OUTPUT);
  pinMode(enableY, OUTPUT);
  pinMode(counter, INPUT);
  
  digitalWrite(enableX, HIGH);
  digitalWrite(enableY, HIGH);
  /*TCCR3B &= ~7;
  TCCR3B |= 3;
  TCCR4B &= ~7;
  TCCR4B |= 3;*/

  Serial.begin(115200);
}

void loop()
{
  analogWrite(pulseX, 127); 
  analogWrite(pulseY, 127);
  digitalWrite(directionX, HIGH);
  digitalWrite(directionY, HIGH);
  
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
    String buffer;
    int distance = 0;
    
    if(strstr(stringPointer, "M"))
    {
      stringPointer++;
      while(*stringPointer)
      {
        buffer += *stringPointer;
        stringPointer++;
      }
      
      distance = buffer.toInt();
    }       
    stringPointer = &readString[0];
    if(strstr(stringPointer, "X"))
    {
       digitalWrite(enableX, LOW); 
    }
    
    if(strstr(stringPointer, "Y"))
    {
      digitalWrite(enableY, LOW);
    }
    
    if(distance < 0)
    {
      digitalWrite(directionX, LOW);
      digitalWrite(directionY, LOW);
    }
    else
    {
      digitalWrite(directionX, HIGH);
      digitalWrite(directionY, HIGH);
    }
    
    for(int i = 0; i < abs(distance); i++)
    {
       int j = 0, tmp = 0;
       
       while(j < (stepsPerMicroMeter * 2))
       {
          if(digitalRead(counter) != tmp)
          {
            j++;
          } 
       }
    } 
    digitalWrite(enableX, HIGH);
    digitalWrite(enableY, HIGH);
    
    Serial.println("OK");
    
    buffer = "";
    readString = "";
  }    
  
  
  
}
