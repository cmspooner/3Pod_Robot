#include <AFMotor.h>

// Adafruit Motor shield library
// copyright Adafruit Industries LLC, 2009
// this code is public domain, enjoy!
// Based on Motor Test Example
#include <AFMotor.h>

AF_DCMotor motor0(3);
AF_DCMotor motor120(4);
AF_DCMotor motor240(1);

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Motor test!");
}

void loop() {
  rawMotorDrive(0, 255, -255);
}

void rawMotorDrive(int m0, int m120, int m240){
 if (m0 > 0){
  motor0.run(FORWARD);
  Serial.println("Motor 0 Forward");
  if (m0 < 255){
    motor0.setSpeed(m0);
  } else {
    motor0.setSpeed(255);
  }
 } else if (m0 < 0){
   motor0.run(BACKWARD);
   Serial.println("Motor 0 Backward");
  if (m0 > -255){
    motor0.setSpeed(m0);
  } else {
    motor0.setSpeed(255);
  }
 } else {
   motor0.run(RELEASE);
   Serial.println("Motor 0 Stop");
 }
 
 if (m120 > 0){
  motor120.run(FORWARD);
  Serial.println("Motor 120 Forward");
  if (m120 < 255){
    motor120.setSpeed(m120);
  } else {
    motor120.setSpeed(255);
  }
 } else if (m120 < 0){
   motor120.run(BACKWARD);
   Serial.println("Motor 120 Backward");
  if (m120 > -255){
    motor120.setSpeed(m120);
  } else {
    motor120.setSpeed(255);
  }
 } else {
   motor120.run(RELEASE);
   Serial.println("Motor 120 Stop");
 }
 
 if (m240 > 0){
  motor240.run(FORWARD);
  Serial.println("Motor 240 Forward");
  if (m240 < 255){
    motor240.setSpeed(m240);
  } else {
    motor240.setSpeed(255);
  }
 } else if (m240 < 0){
   motor240.run(BACKWARD);
   Serial.println("Motor 240 Backward");
  if (m240 > -255){
    motor240.setSpeed(m240);
  } else {
    motor240.setSpeed(255);
  }
 } else {
   motor240.run(RELEASE);
   Serial.println("Motor 240 Stop");
 }
 
}
