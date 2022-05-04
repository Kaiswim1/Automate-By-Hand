#include <SoftwareSerial.h>  

SoftwareSerial BTSerial(0, 1);  

#define ENA 5
#define ENB 6
#define IN1 7
#define IN2 8
#define IN3 9
#define IN4 11 
void setup() {
  // put your setup code here, to run once:
  pinMode(ENA, OUTPUT);  
  pinMode(ENB, OUTPUT); 
  pinMode(IN1, OUTPUT); 
  pinMode(IN2, OUTPUT);  
  pinMode(IN3, OUTPUT); 
  pinMode(IN4, OUTPUT);    

  Serial.begin(9600);
  BTSerial.begin(9600);   
  Serial.println(BTSerial.available()); 
}

void loop() {     
  int speed = 155;
  if (BTSerial.available())
  { 
    Serial.println("Available"); 
    char data = BTSerial.read(); // reading the data received from the bluetooth module 
    Serial.println(data); 
    if(data == 'r'){ //right  
      digitalWrite(IN1, HIGH);  
      digitalWrite(IN2, LOW);  
      digitalWrite(IN3, HIGH);  
      digitalWrite(IN4, LOW); 
      analogWrite(ENA, speed); 
      analogWrite(ENB, speed);     
    }  
    if(data == 'l'){  //left
      digitalWrite(IN1, LOW);  
      digitalWrite(IN2, HIGH);  
      digitalWrite(IN3, LOW);  
      digitalWrite(IN4, HIGH); 
      analogWrite(ENA, speed); 
      analogWrite(ENB, speed);   
    } 
    if(data == 'u'){  //up 
      digitalWrite(IN1, HIGH);  
      digitalWrite(IN2, LOW);  
      digitalWrite(IN3, LOW);  
      digitalWrite(IN4, HIGH); 
      analogWrite(ENA, speed); 
      analogWrite(ENB, speed);   
    } 
     if(data == 'd'){  //down 
      digitalWrite(IN1, LOW);  
      digitalWrite(IN2, HIGH);  
      digitalWrite(IN3, HIGH);  
      digitalWrite(IN4, LOW); 
      analogWrite(ENA, speed); 
      analogWrite(ENB, speed);   
    } 
    if(data == 'w'){ //right 90 
      digitalWrite(IN1, HIGH);  
      digitalWrite(IN2, LOW);  
      digitalWrite(IN3, HIGH);  
      digitalWrite(IN4, LOW);  
      analogWrite(ENA, 255); 
      analogWrite(ENB, 255);    
      delay(311);
      analogWrite(ENA, 0); 
      analogWrite(ENB, 0);  
    }   
     if(data == 'q'){ //right 90
      analogWrite(ENA, 0); 
      analogWrite(ENB, 0);  
      delay(40); 
      digitalWrite(IN1, LOW);  
      digitalWrite(IN2, HIGH);  
      digitalWrite(IN3, LOW);  
      digitalWrite(IN4, HIGH);   
      analogWrite(ENA, 255); 
      analogWrite(ENB, 255);    
      delay(311);
      analogWrite(ENA, 0); 
      analogWrite(ENB, 0);  
    }  
    if(data == 's'){ //Stop
      analogWrite(ENA, 0); 
      analogWrite(ENB, 0); 
   }
}
}
         
