// Adafruit Motor shield library
// copyright Adafruit Industries LLC, 2009
// this code is public domain, enjoy!
// Based on Motor Test Example
#include <AFMotor.h>

AF_DCMotor motor0(4);
AF_DCMotor motor120(3);
AF_DCMotor motor240(1);

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Motor test!");

  // turn on motor
  motor0.setSpeed(200);
  motor120.setSpeed(200);
  motor240.setSpeed(200);
 
  motor0.run(RELEASE);
  motor120.run(RELEASE);
  motor240.run(RELEASE);
}

void loop() {
  Serial.println("slow forward");
  motor0.run(FORWARD);
  motor120.run(FORWARD);
  motor240.run(FORWARD);
  motor0.setSpeed(128);
  motor120.setSpeed(128);
  motor240.setSpeed(128);  
  delay(3000);
  
  motor0.run(RELEASE);
  motor120.run(RELEASE);
  motor240.run(RELEASE);
  delay(500);
  
  Serial.println("fast forward");
  motor0.run(FORWARD);
  motor120.run(FORWARD);
  motor240.run(FORWARD);
  motor0.setSpeed(250);
  motor120.setSpeed(250);
  motor240.setSpeed(250);  
  delay(3000);
  
  motor0.run(RELEASE);
  motor120.run(RELEASE);
  motor240.run(RELEASE);
  delay(500);
  
  
  
  /*
  uint8_t i;
  
  Serial.print("tick");
  
  motor0.run(FORWARD);
  motor120.run(FORWARD);
  motor240.run(FORWARD);
  for (i=0; i<255; i++) {
    motor0.setSpeed(i);
    motor120.setSpeed(i);
    motor240.setSpeed(i);  
    delay(10);
 }
 
  for (i=255; i!=0; i--) {
    motor0.setSpeed(i);
    motor120.setSpeed(i);
    motor240.setSpeed(i);  
    delay(10);
 }
  
  Serial.print("tock");

  motor0.run(BACKWARD);
  motor120.run(BACKWARD);
  motor240.run(BACKWARD);
  for (i=0; i<255; i++) {
    motor0.setSpeed(i);
    motor120.setSpeed(i);
    motor240.setSpeed(i);  
    delay(10);
 }
 
  for (i=255; i!=0; i--) {
    motor0.setSpeed(i);
    motor120.setSpeed(i);
    motor240.setSpeed(i);
    delay(10);
 }
  

  Serial.print("tech");
  motor0.run(RELEASE);
  motor120.run(RELEASE);
  motor240.run(RELEASE);
  delay(1000);
  */
}
