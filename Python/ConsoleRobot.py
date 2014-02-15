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
	
	# ~ go though input and remove non-numerals and mae comas spaces
	
	if " " in input:
		input = input.split(" ")
	else:
		input = [input]
	

def helper(command = None):
	pass
	
def XY(x, y):
	robot.moveXY(x,y)
	return robot.drive()
	

def Polar(command = None):
	pass


if True: #serialPort.isOpen():
	while input != ["quit"]:
		t = .5
		input = cleanInput(raw_input("> "))		
		
		# Run command
		if input[0] == "help":
			result = helper(input[1:])
		elif input[0] == "xy":
			if len(input) < 2:
				print "XY takes at least two arguments"
			else:
				result = XY(input[1], input[2])
			if len(input) >= 3:
				time = input[3]
		elif input[0] == "polar":
			result = Polar(input[1:])
			
		# Send command
		#serialPort.write(result)
		time.sleep(t)
		
		
