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
  if (BTSerial.available())
  { 
    Serial.println("Available"); 
    char data = BTSerial.read(); // reading the data received from the bluetooth module 
    Serial.println(data); 
    if(data == 'f'){ //Forward
      digitalWrite(IN1, HIGH);  
      digitalWrite(IN2, LOW);  
      digitalWrite(IN3, HIGH);  
      digitalWrite(IN4, LOW); 
      analogWrite(ENA, 185); 
      analogWrite(ENB, 185);     
    } 
    if(data == 's'){ //Stop
      analogWrite(ENA, 0); 
      analogWrite(ENB, 0); 
   }
}
}

         
