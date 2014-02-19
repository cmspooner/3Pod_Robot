import serial, math, time
from ThreePod import ThreePod

robot = ThreePod(True)
#serialPort = serial.Serial(0) #first port available

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
	
#serialPort.open()

input = ""
result = None
t = .5

def cleanInput(input):
	input = input.lower()
	
	clean = False
	previousC = ""
	while not clean:
		newInput = ""
		clean = True
		for c in input:
			clean = True
			if c == ",":
				newInput += " "
				clean = False
			elif c == " " and previousC == " ":
				clean = False
			else:
				newInput += c
			previousC = c
		input = newInput
	
	if " " in input:
		input = input.split(" ")
	else:
		input = [input]
		
	return input
	

def helper(command = None):
	print "help - Display this help message"
	print "xy <x> <y>  <rotation> [<time>] - Move on a cartesion plane, optional time in seconds, default time 0.5s"
	print "polar <speed> <angle> <rotation> [<time>] - Move on a Polar plane, optional time in seconds, default time 0.5s"
	
	return



if True: #serialPort.isOpen():
	while input != ["quit"]:
		t = .5
		input = cleanInput(raw_input("> "))		
		
		# Run command
		print input
		print
		if input[0] == "help":
			result = helper(input[1:])
		elif input[0] == "xy":
			if len(input) < 4 or len(input) > 5:
				print "Abnormal number of parameters, xy takes 2 or 3 arguments"
			else:
				robot.moveXY(input[1], input[2], input[3])
			if len(input) > 4:
				t = input[4]
		elif input[0] == "polar":
			if len(input) < 4 or len(input) > 5:
				print "Abnormal number of parameters, xy takes 2 or 3 arguments"
			else:
				robot.movePolar(input[1], input[2], input[3])
			if len(input) > 4:
				t = input[4]
		elif input[0] == "quit":
			robot.moveXY(0,0)
			t = 0
		
		# Send command
		result = robot.drive()
		print result
		#serialPort.write(result)
		t = float(t)
		print "waiting", t, "seconds"
		time.sleep(t)
		
		
