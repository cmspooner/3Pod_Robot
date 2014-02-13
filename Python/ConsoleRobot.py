import serial, math
from ThreePod import ThreePod

robot = ThreePod(True)

if False: #XY Test
	print "255,0"
	robot.moveXY(255,0)
	print robot.drive()
	print

	print "255,255"
	robot.moveXY(255,255)
	print robot.drive()
	print

	print "0,255"
	robot.moveXY(0,255)
	print robot.drive()
	print

	print "-255,255"
	robot.moveXY(-255,255)
	print robot.drive()
	print

	print "-255,0"
	robot.moveXY(-255,0)
	print robot.drive()
	print

	print "-255,-255"
	robot.moveXY(255,255)
	print robot.drive()
	print

	print "0,-255"
	robot.moveXY(0,255)
	print robot.drive()
	print

	print "255,-255"
	robot.moveXY(255,255)
	print robot.drive()
	print

if False: #Polar Test
	print "255,0"
	robot.movePolar(255,0)
	print robot.drive()
	print
	
	print "255,15"
	robot.movePolar(255,15)
	print robot.drive()
	print
	
	print "255,90"
	robot.movePolar(255,90)
	print robot.drive()
	print
	
	print "-179,352"
	robot.movePolar(-179,352)
	print robot.drive()
	print
	
	
