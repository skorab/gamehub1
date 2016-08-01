class movement(object):
	
	def __init__(self):
		
		
		self.position = [1,1]
		self.speed = 0.00005
		self.counter = 0
		self.waypoints = numpy.array([(100,0), (1,1), (100,50), (50,250)])	
	
			
		
	def get_heading(self):
       
		richtungsvektor = [self.waypoints[0] - self.position[0], self.waypoints[1] -self.position[1]]
    
		betrag = sqrt(richtungsvektor[0]**2 + richtungsvektor[1]**2 )
		
		normalvektor = [(richtungsvektor[0] / betrag ),(richtungsvektor[1] / betrag)]
    
		return richtungsvektor

		
		

	def step(self):
			"""step() fuehrt einen einzelnen schritt in richtung des naechsten wegpunktes aus. 
			Die Fkt. addiert das Heading * Geschwindigkeit auf die Aktuelle position. 
			Folglich verschiebt sich die Position einen Schritt in richtung des naechsten Wegpunktes"""

			self.position[0] += (heading[0] * self.speed)
			self.position[1] += (heading[1] * self.speed)
			
			return position


			
			

	def check_waypoint(self):


			x1 = round(self.waypoints[self.counter][0], 2)	
			y1 = round(self.waypoints[next_counter][1], 2)
			x2 = round(self.position[0], 2)
			y2 = round(self.position[1], 2)
    
			if x1  == x2 and y1 == y2:
				self.counter += 1
				heading = get_heading(waypoints[self.counter], self.position)

			

		
		
		
		
		
