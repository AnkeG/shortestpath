import pygame
from pygame.locals import *

gray = (152, 152, 152)

class brick(pygame.sprite.Sprite):
	def __init__(self, location, brick_side, screen):
		pygame.sprite.Sprite.__init__(self)
		self.surf = pygame.Surface((brick_side,brick_side))
		self.rect = self.surf.get_rect()
		self.location = location
		x, y = location
		self.rect.topleft = (x*brick_side, y*brick_side)
		self.screen = screen

	def togglecolor(self, color):
		if self.surf.get_at((0,0)) != color:
			self.surf.fill(color)
			self.screen.blit(self.surf, self.rect)
			return True
		else:
			self.surf.fill(gray)
			self.screen.blit(self.surf, self.rect)
			return False
		

	def fillcolor(self, color):
		self.surf.fill(color)
		self.screen.blit(self.surf, self.rect)