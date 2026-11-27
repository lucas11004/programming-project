import pygame,os,math
from classes import *
from buttons import *
pygame.init()

#this chooses the monitor for the game
os.environ['SDL_VIDEOCENTERED'] = "1"

screen_width = 1440
screen_height = 810


#load buttons
play_img = pygame.image.load('play-button.png').convert_alpha()
lead_img = pygame.image.load('leaderboard-button.png').convert_alpha()



#this will create the screen that the game will run on
screen = pygame.display.set_mode((screen_width,screen_height))
timer = 0
clock = pygame.time.Clock()
running = True
back = pygame.image.load("images/background.png")
back = pygame.transform.scale(back,(1440,810))
#creates a contiunous game running loop
while running:
	# this is for closing the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		clock.tick(30)
		timer += (1/30)
	game_display = screen.blit(back,(0,0))
	pygame.display.update()