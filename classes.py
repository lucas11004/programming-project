import pygame
import math
import random

class body:
	def __init__(myxpos,myypos,mycol,mysurf):
		xposition = myxpos
		yposition = myypos
		colour = mycol
		surface = mysurf

	def getxpos():
		return xposition

	def getypos():
		return yposition

	def changecolour(newcol):
		colour = newcol

	def updatepos(newx,newy):
		xposition = newx
		yposition = newy #I will have to run body.draw() after this each time when it is animated
#initialises the body object

def draw():
	pygame.draw.rect(surface,colour,[xposition,yposition])
#draws the body as a circle on the given surface with a specific colour

