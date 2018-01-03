import numpy


class Bewegung(object):

    def __init__(self):

        self.position = [1,1]
        self.speed = 0.00005
        self.counter = 0
        self.waypoints = numpy.array([(100,0),(1,1),(100,50),(50,250)])


    def get_heading(self):

        richtungsvektor = [self.waypoints[0] - self.position[0], self.waypoints[1] - self.position[1]]
        betrag = numpy.sqrt(richtungsvektor[0]**2 + richtungsvektor[1]**2)
        normalvektor = [(richtungsvektor[0] / betrag), (richtungsvektor[1] / betrag)]
        return richtungsvektor 

    def step(self):
        
        richtung = self.get_heading()
        self.position[0] += self.speed * richtung[0]
        self.position[1] += self.speed * richtung[1]

        return self.position
        
    def check_waypoints(self):

        x2 = round(self.waypoints[self.counter][0], 2)
        y2 = round(self.waypoints[self.counter][1], 2)
        x1 = self.position[0] 
        y1 = self.position[1]

        if x1 == x2 and y1 == y2:

            self.counter += 1



