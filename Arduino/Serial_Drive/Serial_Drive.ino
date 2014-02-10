// Based on Motor Test Example
#include <AFMotor.h>

AF_DCMotor motor0(3);
AF_DCMotor motor120(4);
AF_DCMotor motor240(1);

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Waiting for Serial Data");
  inputString.reserve(200);
}

void loop() {
  if (stringComplete) {
    Serial.println(inputString);
    runSerialCommand(inputString);
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}

void runSerialCommand(String command){
  int motorCommands[3] = {0,0,0};
  String tmpStr;
  int cmdNum = 0;
  for (int i = 0; i < command.length(); i++){
    if (command.charAt(i) == ','){
      motorCommands[cmdNum] = tmpStr.toInt();
      cmdNum += 1;
      tmpStr = "";
    } else {
      tmpStr += command.charAt(i);
    }
  }  
  motorCommands[cmdNum] = tmpStr.toInt();
  
  rawMotorDrive(motorCommands[0], motorCommands[1], motorCommands[2], true);
}


void rawMotorDrive(int m0, int m120, int m240){
 if (m0 > 0){
  motor0.run(FORWARD);
  if (m0 < 255){
    motor0.setSpeed(m0);
  } else {
    motor0.setSpeed(255);
  }
 } else if (m0 < 0){
   motor0.run(BACKWARD);
  if (m0 > -255){
    motor0.setSpeed(m0);
  } else {
    motor0.setSpeed(255);
  }
 } else {
   motor0.run(RELEASE);
 }
 
 if (m120 > 0){
  motor120.run(FORWARD);
  if (m120 < 255){
    motor120.setSpeed(m120);
  } else {
    motor120.setSpeed(255);
  }
 } else if (m120 < 0){
   motor120.run(BACKWARD);
  if (m120 > -255){
    motor120.setSpeed(m120);
  } else {
    motor120.setSpeed(255);
  }
 } else {
   motor120.run(RELEASE);
 }
 
 if (m240 > 0){
  motor240.run(FORWARD);
  if (m240 < 255){
    motor240.setSpeed(m240);
  } else {
    motor240.setSpeed(255);
  }
 } else if (m240 < 0){
   motor240.run(BACKWARD);
  if (m240 > -255){
    motor240.setSpeed(m240);
  } else {
    motor240.setSpeed(255);
  }
 } else {
   motor240.run(RELEASE);
 }
 
}

void rawMotorDrive(int m0, int m120, int m240, boolean debug){
 if (m0 > 0){
  motor0.run(FORWARD);
  if (debug) Serial.print("M0 F ");
  if (m0 < 255){
    motor0.setSpeed(m0);
    if (debug) Serial.print(m0);
  } else {
    motor0.setSpeed(255);
    if (debug) Serial.print(255);
  }
 } else if (m0 < 0){
   motor0.run(BACKWARD);
   if (debug) Serial.print("M0 B ");
  if (m0 > -255){
    motor0.setSpeed(abs(m0));
    if (debug) Serial.print(abs(m0));
  } else {
    motor0.setSpeed(255);
    if (debug) Serial.print(255);
  }
 } else {
   motor0.run(RELEASE);
   if (debug) Serial.print("M0 Stop");
 }
 if (debug) Serial.print(", ");
 
 if (m120 > 0){
  motor120.run(FORWARD);
  if (debug) Serial.print("M120 F ");
  if (m120 < 255){
    motor120.setSpeed(m120);
    if (debug) Serial.print(m120);
  } else {
    motor120.setSpeed(255);
    if (debug) Serial.print(255);
  }
 } else if (m120 < 0){
   motor120.run(BACKWARD);
   if (debug) Serial.print("M120 B ");
  if (m120 > -255){
    motor120.setSpeed(abs(m120));
    if (debug) Serial.print(abs(m120));
  } else {
    motor120.setSpeed(255);
    if (debug) Serial.print(255);
  }
 } else {
   motor120.run(RELEASE);
   if (debug) Serial.print("M120 Stop");
 }
 if (debug) Serial.print(", ");
 
 if (m240 > 0){
  motor240.run(FORWARD);
  if (debug) Serial.print("M240 F ");
  if (m240 < 255){
    motor240.setSpeed(m240);
    if (debug) Serial.println(m240);
  } else {
    motor240.setSpeed(255);
    if (debug) Serial.println(255);
  }
 } else if (m240 < 0){
   motor240.run(BACKWARD);
   if (debug) Serial.print("M240 B ");
  if (m240 > -255){
    motor240.setSpeed(abs(m240));
    if (debug) Serial.println(abs(m240));
  } else {
    motor240.setSpeed(255);
    if (debug) Serial.println(255);
  }
 } else {
   motor240.run(RELEASE);
   if (debug) Serial.println("M240 Stop");
 }
 
}
