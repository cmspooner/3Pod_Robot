// Adafruit Motor shield library
// copyright Adafruit Industries LLC, 2009
// this code is public domain, enjoy!
// Based on Motor Test Example
#include <AFMotor.h>

AF_DCMotor motor0(1);
AF_DCMotor motor120(3);
AF_DCMotor motor240(4);

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Motor test!");

  // turn on motor
  motor0.setSpeed(200);
  motor0.setSpeed(200);
  motor0.setSpeed(200);
 
  motor0.run(RELEASE);
  motor120.run(RELEASE);
  motor240.run(RELEASE);
}

void loop() {
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
}
