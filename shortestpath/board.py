import pygame
from pygame.locals import *

gray = (152, 152, 152)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

class brick(pygame.sprite.Sprite):
	def __init__(self, size, location, brick_side):
		pygame.sprite.Sprite.__init__(self)
		self.surf = pygame.Surface(size)
		self.surf.fill(gray)
		self.rect = self.surf.get_rect()
		self.location = location
		x, y = location
		self.rect.topleft = (x*brick_side, y*brick_side)

	def togglered(self):
		if self.surf.get_at((0,0)) != red:
			self.surf.fill(red)
			return True
		else:
			self.surf.fill(gray)
			return False

	def togglewhite(self):
		if self.surf.get_at((0,0)) != white:
			self.surf.fill(white)
			return True
		else:
			self.surf.fill(gray)
			return False