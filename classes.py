import pygame
import math
import random

class body:
    def __init__(self,myxpos,myypos,mycol,mysurf):
        self.xposition = myxpos
        self.yposition = myypos
        self.colour = mycol
        self.surface = mysurf
        
    def setxpos(xposition):
        xposition = 0
        
    def setypos(yposition):
        yposition = 0

    def getxpos(xposition):
            return xposition

    def getypos(yposition):
        return yposition

    def changecolour(newcol):
        colour = newcol

    def updatepos(newx,newy):
        xposition = newx
        yposition = newy #I will have to run body.draw() after this each time when it is animated
    
    #initialises the body object
    def draw(self):
        pygame.draw.rect(self.surface,self.colour,[self.xposition,self.yposition])
        #draws the body as a circle on the given surface with a specific colour



class human:
    def __init__(self,myhealth,myspeed):
        self.health = myhealth
        self.speed = myspeed
#defines the human class for my player and zombies

    def get_health(health):
        return health 

def set_health(newhealth):
    health = newhealth
#this health can be adjusted for the zombies

class player(human):
    def __init__(mylives):
        lives = mylives

    def get_lives(lives):
        return lives

    def set_lives(newlives):
        lives = newlives
    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
   
    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        for wall in map:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom


class map(object):
    def __init__(self, wx, wy):
        map.append(self)
        self.rect = pygame.Rect(wx, wy, 30, 30)

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

    def moveZombie(human,self):
        dirvect = pygame.math.Vector(player.rect.x - self.rect.x,player.rect.y - self.rect.y)
        dirvect.normalise()
        dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)
#This is used to figure out the zombie's position relative to the player and creates a direction vector for the ai to use to be attracted towards the player's position
class items(body):
    def __init__(self,mybandage,mymedkit):
        self.bandage = mybandage
        self.medkit = mymedkit
#defines how the health items will work and how much health they give to the player

    def get_bandage(bandage):
        return bandage

    def set_bandage(lives):
        if lives < 3:
            return lives + 0.5
        

class weapons(items):
    def __init__(self,myfiresound,myammo):
     self.firesound = myfiresound
     self.ammo = myammo
#this defines the firesound and the ammo the user has

    def shoot(self,Screen_Width):
        
        if ammo > 0:
            for event in pygame.event.get():
              #  if event.type == pygame.KEYDOWN and Gun.image == NOGUN: 
               #     if event.key == pygame.K_SPACE and Gun.image == NOGUN: 
        #Initialize Bullet so it's not null 
                        Bullet.rect.center = self.rect.center 
        if self.direction == 0: 
            Bullet.direction = 0 

        if Bullet != "":
         Bullet.X += 10 
        if Bullet.X > Screen_Width() :
         Bullet = ""

        pygame.mixer.Sound("myfiresound")
        pygame.mixer.music.stop()
        ammo += -1

    #this will play the sound associates with firing and remove 1 bullet from the user's total

