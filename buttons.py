import pygame
import time

#button class
class button():
	def __inint__(self,bx,by,image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (bx,by)
		
	def draw(self, surface):
		#draw button on screen
		surface.blit(self.image, (self.rect.bx, self.rect.by))