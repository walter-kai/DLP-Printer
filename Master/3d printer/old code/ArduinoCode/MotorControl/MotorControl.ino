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

  Serial.begin(9600);
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
    int distanceX = 0, distanceY = 0, distance = 0;
    
    stringPointer = &readString[0];
    
    if(strstr(stringPointer, "G1"))
    {
      TCCR3B &= ~7;
      TCCR3B |= 2;
      TCCR4B &= ~7;
      TCCR4B |= 2;
    }   

    if(strstr(stringPointer, "G0"))
    {
      TCCR3B &= ~7;
      TCCR3B |= 3;
      TCCR4B &= ~7;
      TCCR4B |= 3;
    }   

    stringPointer = &readString[0];
    if(strstr(stringPointer, "X"))
    {
      char* e = strchr(&readString[0], 'X');
      int index = (int)(e - stringPointer);
      stringPointer = &readString[index + 1];
      String buffer = "";
      digitalWrite(enableX, LOW); 
      while(*stringPointer)
      {
        buffer += *stringPointer;
        stringPointer++;
      }
      
      distanceX = buffer.toInt();
    }
    
    stringPointer = &readString[0];
    if(strstr(stringPointer, "Y"))
    {
      char* e = strchr(&readString[0], 'Y');
      int index = (int)(e - stringPointer);
      stringPointer = &readString[index + 1];
      String buffer = "";
      digitalWrite(enableY, LOW);
      while(*stringPointer)
      {
        buffer += *stringPointer;
        stringPointer++;
      }
      
      distanceY = buffer.toInt();
    }
    
    if(distanceX < 0)
    {
      digitalWrite(directionX, LOW);
    }
    else
    {
      digitalWrite(directionX, HIGH);
    }
    
    if(distanceY < 0)
    {
      digitalWrite(directionY, LOW);
    }
    else
    {
      digitalWrite(directionY, HIGH);
    }
    
    (abs(distanceX) > abs(distanceY)) ? (distance = distanceX) : (distance = distanceY);
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
       
       if(i == abs(distanceX))
         digitalWrite(enableX, HIGH);
         
       if(i == abs(distanceY))
         digitalWrite(enableY, HIGH);
    } 
    digitalWrite(enableX, HIGH);
    digitalWrite(enableY, HIGH);
    
    delay(1);
    Serial.println("OK");
   
    readString = "";
  }
     
}
