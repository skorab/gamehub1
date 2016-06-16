background_image_filename = "Dresden_Map.svg"
lachmann_image_filename = "lachmann.svg"
oertel_image_filename = "oertel.svg"
festerling_image_filename = "festerling.svb"
tonnenanwalt_image_filename = "tonnenanwalt.svg"


import pygame
from math import *
from pygame.locals import *
from sys import exit
pygame.init()
import numpy

screen = pygame.display.set_mode((1024, 888), 0, 32)
pygame.display.set_caption("Scheiss Pegida")


background = pygame.image.load(background_image_filename).convert()
lachmann = pygame.image.load(lachmann_image_filename).convert_alpha()
oertel = pygame.image.load(oertel_image_filename).convert_alpha()
festerling = pygame.image.load(festerling_image_filename).convert_alpha()
tonnenanwalt = pygame.image.load(tonnenanwalt_image_filename).convert_alpha()

def get_heading(nextpoint, position_):
    
    #print(nextpoint[0])
    #print(position_[0])
    richtungsvektor = [0,0]
    normalvektor = [0,0]
    
    richtungsvektor = [nextpoint[0] - position_[0],
        nextpoint[1] - position_[1]]
    
    betrag = sqrt( richtungsvektor[0]**2 + richtungsvektor[1]**2 )

    normalvektor = [(richtungsvektor[0] / betrag ),(richtungsvektor[1] / betrag)]

    print("Richtungsvektor:")
    print(richtungsvektor)
    
    print("NormalVektor:")
    print(normalvektor)
    return richtungsvektor 


def step(state, speed):
    old = start

    start[0] += (heading[0] * speed)
    start[1] += (heading[1] * speed)
    return start


def check_waypoint(counter_):
    global counter, heading
    a1 = round(waypoints[counter_][0], 2)
    a2 = round(waypoints[counter_][1], 2)

    b1 = round(start[0], 2)
    b2 = round(start[1], 2)
    if a1  == b1 and a2 == b2:
        print("hi")
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
