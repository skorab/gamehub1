background_image_filename = "Dresden_Karte1.png"
lachmann_image_filename = "lachmann.png"
oertel_image_filename = "oertel.png"
festerling_image_filename = "festerling.png"
tonnenanwalt_image_filename = "tonnenanwalt.png"


import pygame 
from pygame.locals import *
from sys import exit
pygame.init()
import numpy

screen = pygame.display.set_mode((1024, 888), 0, 32)
pygame.display.set_caption("Scheiss Pegida")

clock = pygame.time.Clock()

speed = 2.
position = numpy.array((30.0,50.0))
magnitude = [509., 141., 128., 409., 293., 330., 251., 532.]
#heading = numpy.array([(0.7,0.73),(0.71,0.71),(0.78,0.63),(-0.52,0.65),(0.97,0.24),(0.58,-0.82),(-0.88,-0.48),(0.08,-0.99)])

waypoints = numpy.array[(0,0), (640, 300)]


background = pygame.image.load(background_image_filename).convert()
lachmann = pygame.image.load(lachmann_image_filename).convert_alpha()
oertel = pygame.image.load(oertel_image_filename).convert_alpha()
festerling = pygame.image.load(festerling_image_filename).convert_alpha()
tonnenanwalt = pygame.image.load(tonnenanwalt_image_filename).convert_alpha()

route1 = 0
route2 = 0
route3 = 0
route4 = 0
time = 0
start = (300,30)

def get_heading(nextpoint):
    position_ = lachman.get_pos()
    print(position_)
    richtungsvektor = waypoints[nextpoint] - position
    print(richtungsvektor)
    return richtungsvektor 

def step():

    return 0

start = (300,30)
while True:
    counter = 0
    time += 0.01
    for event in pygame.event.get():
	    
        if event.type == QUIT:
            exit()
			
        screen.blit(background, (0.0,0.0))
        screen.blit(lachmann, start)
        screen.blit(oertel, (300,30))
        screen.blit(festerling, (500,30))
        screen.blit(tonnenanwalt,(800,30))
    
        route = time * speed
        position += heading[0] * route
        pygame.display.update()
