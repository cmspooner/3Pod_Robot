import math

class ThreePod():
	def __init__(self, debug = False):
		#Cartesian Coordinate System 
		self.speedx = 0
		self.speedy = 0
		
		#Polar Coordinate System
		self.angle = 0
		self.speed  = 0
		
		#Rotation on Axis
		self.speedRot = 0
		
		self.debug = debug
		
	def __str__(self, coordSys = "polar"):
		if coodSys == "polar":
			return self.speed, self.angle
		if coodSys == "xy":
			return self.speedx, self.speedy, self.rot
			
	def movePolar(self, speed, angle):
		self.speed = float(speed)
		self.angle = float(math.radians(angle))
		
		self.speedx = math.cos(self.angle)
		self.speedy = math.sin(self.angle)
		
	def moveXY(self, x, y):
		self.speedx = float(x)
		self.speedy = float(y)
		
		self.speed = math.sqrt((self.speedx**2)+(self.speedy**2))
		if self.speed > 255:
			self.speed = 255
		if self.speed < -255:
			self.speed = -255
			
		if self.debug: print "Speed: ", self.speed
		
		if self.speedx != 0:
			self.angle = math.atan(self.speedy/self.speedx)
		else:
			if self.speedy > 0:
				self.angle = math.radians(90)
			elif self.speedy < 0:
				self.angle = math.radian(270)
			
	def moveRotate(self, speed):
		self.speedRot = speed
	
	def drive(self):		
		m0angle = self.angle + math.radians(0)
		m120angle = self.angle + math.radians(120)
		m240angle = self.angle + math.radians(240)
		
		m0speed = self.speed * math.sin(m0angle)
		m120speed = self.speed * math.sin(m120angle)
		m240speed = self.speed * math.sin(m240angle)
		if self.debug: print "0======> ", math.sin(m0angle)
		if self.debug: print "120====> ", math.sin(m120angle)
		if self.debug: print "240====> ", math.sin(m240angle)
		 
		moveString = "" 
		moveString += str(int(m0speed)) + ',' 
		moveString += str(int(m120speed)) + ',' 
		moveString += str(int(m240speed)) 
		
		return moveString
		
