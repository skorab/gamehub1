background_image_filename = "./pictures/Altstadt.png"
lachmann_image_filename = "./pictures/lachmann.png"
oertel_image_filename = "./pictures/oertel.png"
festerling_image_filename = "./pictures/festerling.png"
tonnenanwalt_image_filename = "./pictures/tonnenanwalt.png"


import pygame
from math import *
from pygame.locals import *
from sys import exit
import numpy
import Klasse_Bewegung as KB

screen_size = (980, 735)
screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
pygame.init()
pygame.display.set_caption("Scheiss Pegida")

background = pygame.image.load(background_image_filename).convert()
lachmann = pygame.image.load(lachmann_image_filename).convert_alpha()
oertel = pygame.image.load(oertel_image_filename).convert_alpha()
festerling = pygame.image.load(festerling_image_filename).convert_alpha()
tonnenanwalt = pygame.image.load(tonnenanwalt_image_filename).convert_alpha()

BW = KB.Bewegung()

while True:
    for event in pygame.event.get():
	    
        if event.type == QUIT:
            exit()
        if event.type == VIDEORESIZE:
        	screen_size = event.size
        	screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
        	
        screen_width, screen_height = screen_size
        for y in range(0, screen_height, background.get_height()):
        	for x in (0, screen_width, background.get_width()):
        		screen.blit(background, (x,y))
			
    screen.blit(background, (0.0,0.0))
    screen.blit(lachmann, BW.step())
    screen.blit(oertel, (300,30))
    screen.blit(festerling, (500,30))
    screen.blit(tonnenanwalt,(800,30))

    BW.check_waypoints()
    pygame.display.update()
