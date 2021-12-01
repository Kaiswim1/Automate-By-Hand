#include <SoftwareSerial.h> 
#include <SPI.h> 
#include <SD.h>

SoftwareSerial BTSerial(6, 7); 
Sd2Card card;
SdVolume volume;
SdFile root;  
File myFile;
int i;  

void Read(String v)
{
  myFile = SD.open(v); 
  if(myFile){
    while (myFile.available()) { 
      Serial.write(myFile.read());
    }
    // close the file:
    myFile.close();
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening test.txt");
  }
} 

void Write(String v, int i)
{
  myFile = SD.open(v, FILE_WRITE);

  // if the file opened okay, write to it:
  if (myFile) {
    Serial.print("Writing to test.txt...");
    myFile.println("testing 1, 2, 3.");
    // close the file:
    myFile.close();
    Serial.println("done.");
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening test.txt");
  }
}

void setup()
{   
   i=0;
   Serial.begin(9600); 
   BTSerial.begin(9600);
   pinMode(13, OUTPUT); // put your setup code here, to run once: 
   while (!Serial) {;} // wait for serial port to connect. Needed for native USB port only   
   Serial.print("Initializing SD card...");
   Serial.println("initialization done.");
}


void loop()
{
   // put your main code here, to run repeatedly:

   if (BTSerial.available() > 0)
   {
      char data = BTSerial.read(); // reading the data received from the bluetooth module
      switch (data)
      { 
         case 'v': myFile = SD.open("internal.txt", FILE_WRITE); Write("internal.txt", 0); break;  
         case 'x': myFile = SD.open("internal.txt"); Serial.print(myFile.read()); break;
         case 'a': digitalWrite(13, HIGH); myFile.println("a\n"+String(i)); break; // when a is pressed on the app on your smart phone
         case 'd': digitalWrite(13, LOW); myFile.println("d\n"+String(i)); break; // when d is pressed on the app on your smart phone
         default : break;
      }
   }
   delay(1); 
   i++;
}
