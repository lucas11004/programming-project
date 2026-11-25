import pygame
import math
import random

"""class body:
	def __init__(myxpos,myypos,mycol,mysurf):
		xposition = myxpos
		yposition = myypos
		colour = mycol
		surface = mysurf
		
    def setxpos(xposition):
        xposition = 0
		
    def setypos(yposition):
        yposition = 0

	def getxpos(xposition):
			return xposition

	def getypos():
		return yposition

	def changecolour(newcol):
		colour = newcol

	def updatepos(newx,newy):
		xposition = newx
		yposition = newy #I will have to run body.draw() after this each time when it is animated
    
    #initialises the body object
    def draw(surface,colour,xposition,yposition):
	    pygame.draw.rect(surface,colour,[xposition,yposition])
        #draws the body as a circle on the given surface with a specific colour

"""

class human:
	def __init__(myhealth,myspeed):
		health = myhealth
		speed = myspeed
#defines the human class for my player and zombies

	def get_health():
        return health 

def set_health(newhealth):
	health = newhealth
#this health can be adjusted for the zombies

class player inherits human:
	def __init__(mylives):
		lives = mylives

	def get_lives():
		return lives

	def set_lives(newlives):
		lives = newlives
#This provides the 3 lives system using a variable that can be changed in the main program

class zombie(human):
	def __init__(mydifficulty):
		difficulty = mydifficulty
		
	def setdifficulty(difficulty):
		if difficulty == "easy":
			health = 80
			speed = 1
		elif difficulty == "hard":
			health = 120
			speed = 3
		else: 
			health = 100
			speed = 2
#This defines the different difficulties for the player, and adjusts the zombie health and speed to ensure there is a fair diffculty for every player

	def moveZombie(human)
		dirvect = pygame.math.Vector(player.rect.x - self.rect.x,player.rect.y - self.rect.y)
	dirvect.normalise()
	dirvect.scale_to_length(speed)
	self.rect.move_ip(dirvect)
#This is used to figure out the zombie's position relative to the player and creates a direction vector for the ai to use to be attracted towards the player's position
class items inherits body:
public procedure new(mybandage,mymedkit)
	 	bandage = mybandage
		medkit = mymedkit
#defines how the health items will work and how much health they give to the player

	procedure get_bandage
		return bandage

	function set_bandage
		if lives< 3:
			return lives + 0.5
		

class weapons inherits items
	public procedure new(myfiresound,myammo)
	firesound = myfiresound
	ammo = myammo
#this defines the firesound and the ammo the user has

	prcoedure shoot()
		
if ammo > 0:
 		if event.type == pygame.KEYDOWN and Gun.image == NOGUN: 
if event.key == pygame.K_SPACE and Gun.image == NOGUN: 
#Initialize Bullet so it's not null 
Bullet.rect.center = Player.rect.center 
if Player.direction == 0: 
Bullet.direction = 0 

if Bullet != null 
Bullet.X += 10 
if Bullet.X > ScreenWidth() 
Bullet = null

pygame.mixer.Sound("myfiresound")
pygame.mixer.music.stop()
ammo = ammo -1

	#this will play the sound associates with firing and remove 1 bullet from the user's total

