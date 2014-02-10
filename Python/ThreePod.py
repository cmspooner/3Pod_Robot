import math

class ThreePod():
	def __init__(self):
		#Cartesian Coordinate System 
		self.speedx = 0
		self.speedy = 0
		
		#Polar Coordinate System
		self.angle = 0
		self.speed  = 0
		
		#Rotation on Axis
		self.speedRot = 0
		
	def __str__(self, coordSys = "polar"):
		if coodSys == "polar":
			return self.speed, self.angle
		if coodSys == "xy":
			return self.speedx, self.speedy, self.rot
			
	def movePolar(self, speed, angle)
		self.speed = float(speed)
		self.angle = float(math.radians(angle))
		
		self.speedx = math.cos(self.angle)
		self.speedy = math.sin(self.angle)
		
	def moveXY(self, x, y):
		self.speedx = float(x)
		self.speedy = float(y)
		
		self.speed = math.sqrt((self.speedx**2)+(self.speedy**2))
		if self.speedx != 0:
			self.angle = arctan(self.speedy/self.speedx)
		else:
			if self.speedy > 0:
				self.angle = math.radians(90)
			elif self.speedy < 0:
				self.angle = math.radian(270)
			
	def moveRotate(self, speed):
		self.speedRot = speed
	
	def drive(self):
		moveString = ""
		 
		 # ~Math to convert speed to motor speeds 
		
		return moveString
		
