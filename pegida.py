<<<<<<< HEAD
<<<<<<< HEAD
background_image_filename = "Altstadt.png"
=======
background_image_filename = "Dresden_Map.png"
>>>>>>> aaa2228f77fc12d55426627d772c8f519e628de2
=======
background_image_filename = "Dresden_Karte1.png"
>>>>>>> 98124704bddb97a7deb7224088f14f0b95dde1f3
lachmann_image_filename = "lachmann.png"
oertel_image_filename = "oertel.png"
festerling_image_filename = "festerling.png"
tonnenanwalt_image_filename = "tonnenanwalt.png"

import pygame
from math import *
from pygame.locals import *
from sys import exit
import numpy

pygame.init()
screen = pygame.display.set_mode((1920, 1080), 0, 32)
pygame.display.set_caption("Scheiss Pegida")

background = pygame.image.load(background_image_filename).convert()
lachmann = pygame.image.load(lachmann_image_filename).convert_alpha()
oertel = pygame.image.load(oertel_image_filename).convert_alpha()
festerling = pygame.image.load(festerling_image_filename).convert_alpha()
tonnenanwalt = pygame.image.load(tonnenanwalt_image_filename).convert_alpha()

def get_heading(nextpoint, position_):

#get_heading berechnet den Richtungsvektor und den Normierten-Vektor 
#zwischen der aktuellen Position (position_) und dem naechsten Wegpunkt (nextpoint).
#Get heading muss nur ein einziges mal pro Wegpunkt ausgefuehrt werden.
    
    richtungsvektor = [0,0]
    normalvektor = [0,0]
    richtungsvektor = [nextpoint[0] - position_[0],
        nextpoint[1] - position_[1]]
    
    betrag = sqrt( richtungsvektor[0]**2 + richtungsvektor[1]**2 )
    normalvektor = [(richtungsvektor[0] / betrag ),(richtungsvektor[1] / betrag)]

    return richtungsvektor 


def step(state, speed):
    """step() fuehrt einen einzelnen schritt in richtung des naechsten wegpunktes aus. 
       Die Fkt. addiert das Heading * Geschwindigkeit auf die Aktuelle position. 
       Folglich verschiebt sich die Position einen Schritt in richtung des naechsten Wegpunktes"""

    old = start

    start[0] += (heading[0] * speed)
    start[1] += (heading[1] * speed)
    return start


def check_waypoint(counter_):
    """check_waypoint prueft ob der Wegpunkt erreicht wurde. 
    Er vergleicht die x und y koordinaten von position und wegpunkt, sind sie identisch wurde der Wegpunkt
    erreicht. Aufgrund von Rundungsfehlern werden die Koordinaten im vorraus auf 2 stellen nach dem Komma 
    gerundet."""

    global counter, heading
    x1 = round(waypoints[counter_][0], 2)
    y1 = round(waypoints[counter_][1], 2)
    x2 = round(start[0], 2)
    y2 = round(start[1], 2)
    
    if x1  == x2 and y1 == y2:
        counter += 1
        heading = get_heading(waypoints[counter], start)

waypoints = numpy.array([(100,0), (1,1), (100,50), (50,250)])
time = 0
start = [1,1] 
old = []
heading = get_heading(waypoints[0],start)
counter = 0

while True:
    time += 0.01
    for event in pygame.event.get():
	    
        if event.type == QUIT:
            exit()
			
    screen.blit(background, (0.0,0.0))
    screen.blit(lachmann, step(1,0.0005))
    screen.blit(oertel, (300,30))
    screen.blit(festerling, (500,30))
    screen.blit(tonnenanwalt,(800,30))

    check_waypoint(counter)
    pygame.display.update()
