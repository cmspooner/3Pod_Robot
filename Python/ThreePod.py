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
		
		self.m0angle = self.angle - math.radians(0)
		self.m120angle = self.angle - math.radians(120)
		self.m240angle = self.angle - math.radians(240)
		
		self.m0speed = 0
		self.m120speed = 0
		self.m240speed = 0
		
	def __str__(self, coordSys = "polar"):
		if coodSys == "polar":
			return self.speed, self.angle
		if coodSys == "xy":
			return self.speedx, self.speedy, self.rot
			
	def movePolar(self, speed, angle, rotate = 0):
		self.speed = float(speed)
		if self.speed > 255:
			self.speed = 255
		if self.speed < -255:
			self.speed = -255
		self.angle = float(math.radians(float(angle)))
		self.speedRot = float(rotate)
		
		while (self.speed + self.speedRot > 255 
				or self.speed + self.speedRot < -255):
			if self.speed > 0:
				self.speed -= 10
			elif self.speed < 0:
				self.speed += 10
				
			if self.speedRot > 0:
				self.speedRot -= 10
			elif self.speedRot < 0:
				self.speedRot += 10
			
		self.speedx = math.cos(self.angle) * self.speed
		self.speedy = math.sin(self.angle) * self.speed
		
		self.moveRaw()
		
	def moveXY(self, x, y, rotate = 0):
		self.speedx = float(x)
		self.speedy = float(y)
		self.speedRot = float(rotate)
		
		self.speed = math.sqrt((self.speedx**2)+(self.speedy**2))
		if self.speed > 255:
			self.speed = 255
		if self.speed < -255:
			self.speed = -255
			
		while (self.speed + self.speedRot > 255 
				or self.speed + self.speedRot < -255):
			if self.speed > 0:
				self.speed -= 10
			elif self.speed < 0:
				self.speed += 10
				
			if self.speedRot > 0:
				self.speedRot -= 10
			elif self.speedRot < 0:
				self.speedRot += 10
			
		if self.debug: print "Speed: ", self.speed
		
		
		self.moveRaw()
		
	def moveRaw(self, m0 = None, m120 = None, m240 = None):
		self.m0angle = self.angle - math.radians(0)
		self.m120angle = self.angle - math.radians(120)
		self.m240angle = self.angle - math.radians(240)
		
		if not m0 or not m120 or not m240:
			self.m0speed = self.speed * math.sin(self.m0angle) + self.speedRot
			self.m120speed = self.speed * math.sin(self.m120angle) + self.speedRot
			self.m240speed = self.speed * math.sin(self.m240angle) + self.speedRot
		else:
			self.m0speed = m0
			self.m120speed = m120
			self.m240speed = m240
	
	def drive(self):				
		if self.debug: print "0======> ", math.degrees(self.m0angle), self.m0speed
		if self.debug: print "120====> ", math.degrees(self.m120angle), self.m120speed
		if self.debug: print "240====> ", math.degrees(self.m240angle), self.m240speed
		 
		moveString = "" 
		moveString += str(int(self.m0speed)) + ',' 
		moveString += str(int(self.m120speed)) + ',' 
		moveString += str(int(self.m240speed)) 
		
		return moveString
		
