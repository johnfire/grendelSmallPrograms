

#include <Wire.h>
#include <Servo.h>

#define SLAVE_ADDRESS 0x04
#define UP_DWN_PIN 0x06
#define LR_PIN 0x05

int startbyte = 0;
int command = 0;
int dataOne = 0;
int dataTwo = 0;
int dataThree = 0;
int myData = 0;
int state = 0;

Servo updwnServo;
Servo lrServo;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // start serial for output
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.println("Ready!");
  updwnServo.attach(UP_DWN_PIN);
  lrServo.attach(LR_PIN);
}

void loop() {
  delay(100);
}

// callback for received data
void receiveData(int byteCount){
  while(Wire.available()) {
    startbyte = Wire.read();
    command = Wire.read();
    dataOne = Wire.read();
    dataTwo = Wire.read();
    dataThree = Wire.read();
    Serial.println("data received: ");
    Serial.println(startbyte);
    Serial.println(command);
    Serial.println(dataOne);
    Serial.println(dataTwo);
    Serial.println(dataThree);
    switch (command) {
      case 1:
        // move head left or right
        dataOne = map(dataOne, 0, 16, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
        lrServo.write(dataOne);                  // sets the servo position according to the scaled value
        delay(2);
        break;
      case 2:
        // move head right
        break;
      case 3:
        // move head up or down
        dataOne = map(dataOne, 0, 16, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
        updwnServo.write(dataOne);                  // sets the servo position according to the scaled value
        delay(2);
        break;
      case 4:
        // move head down
        break;
      case 5:
        // statements
        break;
      case 6:
        // statements
        break;
      case 7:
        // statements
        break;
      case 8:
        // statements
        break;
      case 9:
        // statements
        break;
      case 10:
        // statements
        break;
      case 11:
        // statements
        break;
      case 12:
        // statements
        break;
      case 13:
        // light on AND OFF
        if (command == 13){
          if (state == 0){
            digitalWrite(13, HIGH); // set the LED on
            state = 1;
          }
          else{
            digitalWrite(13, LOW); // set the LED off
            state = 0;
          }
        }
        break;
      case 14:
        // light off
        break;
      default:
        // statements
        break;
    }
  }
}

// callback for sending data
void sendData(){
  Wire.write(dataOne);
}
