background_image_filename = "Dresden_Map.svg"
lachmann_image_filename = "lachmann.svg"
oertel_image_filename = "oertel.png"
festerling_image_filename = "festerling.svg"
tonnenanwalt_image_filename = "tonnenanwalt.svg"


import pygame 
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
pygame.init()
import numpy

screen = pygame.display.set_mode((1024, 888), 0, 32)
pygame.display.set_caption("Scheiss Pegida")

clock = pygame.time.Clock()

speed = 20.
position = numpy.array((30.0,50.0))
magnitude = [509., 141., 128., 409., 293., 330., 251., 532.]
heading = numpy.array([(0.7,0.73),(0.71,0.71),(0.78,0.63),(-0.52,0.65),(0.97,0.24),(0.58,-0.82),(-0.88,-0.48),(0.08,-0.99)])




background = pygame.image.load(background_image_filename).convert()
lachmann = pygame.image.load(lachmann_image_filename).convert_alpha()
oertel = pygame.image.load(oertel_image_filename).convert_alpha()
festerling = pygame.image.load(festerling_image_filename).convert_alpha()
tonnenanwalt = pygame.image.load(tonnenanwalt_image_filename).convert_alpha()


while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
			
	screen.blit(background, (0.0,0.0))
	screen.blit(lachmann, position)
	screen.blit(oertel, (300,30))
	screen.blit(festerling, (500,30))
	screen.blit(tonnenanwalt,(800,30))
	
	time_passed = clock.tick()
	time_passed_seconds = time_passed / 1000.0
	
	
	
	

	route = time_passed_seconds * speed
	position += heading[0] * route
	
	if route >= magnitude[0]:
		route = 0
		route1 = time_passed_seconds * speed
		position += heading[1] * route1	
		if route1 >= magnitude[1]:
			route2 = time_passed_seconds * speed
			position += heading[2] *route2
			if route2 >= magnitude[2]:
				route3 = time_passed_seconds * speed
				position += heading[3] * route3
				if route3 >= magnitude[3]:
					route4 = time_passed_seconds * speed
					position += heading[4] * route4
		
		
		
	
	
	pygame.display.update()
