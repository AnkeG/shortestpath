import pygame
from pygame.locals import *
import sys

screen_width = 500
screen_height = 500
screen_size = (screen_width, screen_width)
brick_width = 50
brick_height = 50
brick_size = (brick_width, brick_height)

colorgray = (152, 152, 152)

class brick(pygame.sprite.Sprite):
	def __init__(self, size, location):
		pygame.sprite.Sprite.__init__(self)
		self.size = size
		self.surf = pygame.Surface(size)
		self.surf.fill(colorgray)
		self.rect = self.surf.get_rect()
		self.rect.topleft = location

	def toggle(self, point):
		if (self.rect.collidepoint(point)):
			if self.surf.get_at((0,0)) == colorgray:
				self.surf.fill((255,0,0))
			else:
				self.surf.fill(colorgray)
			return True
		return False

if __name__ == "__main__":
	pygame.init()

	screen = pygame.display.set_mode(screen_size)
	screen.fill('white')

	bricks = pygame.sprite.Group()

	for x in range(screen_width//brick_width):
		for y in range(screen_height//brick_height):
			b = brick(brick_size, (x*brick_width, y*brick_height))
			screen.blit(b.surf, b.rect)
			bricks.add(b)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				point = pygame.mouse.get_pos()
				for b in bricks:
					if b.toggle(point):
						screen.blit(b.surf, b.rect)
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()