import pygame,os,math
pygame.init()

#this will get the width and height of the screen depending on its size
os.environ['SDL_VIDEOCENTERED'] = "1"

screen_width = 1440
screen_height = 810


#this will create the screen that the game will run on
screen = pygame.display.set_mode((screen_width,screen_height))
timer = 0
clock = pygame.time.Clock()
running = True

#creates a contiunous game running loop
while running:
	# this is for closing the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		pygame.display.flip
		clock.tick(30)
		timer += (1/30)
