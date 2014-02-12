import serial, math
from ThreePod import ThreePod

robot = ThreePod()

robot.moveXY(255,0)
print robot.drive()

robot.moveXY(0,255)
print robot.drive()

robot.moveXY(255,255)
print robot.drive()

