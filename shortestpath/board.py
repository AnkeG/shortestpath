import pygame
from pygame.locals import *
import sys
import spf

screen_width = 1000
screen_height = 800
screen_size = (screen_width, screen_height)
brick_side = 25
brick_size = (brick_side, brick_side)
numofrows = screen_height//brick_side
numofcolumns = screen_width//brick_side

gray = (152, 152, 152)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

class brick(pygame.sprite.Sprite):
	def __init__(self, size, location):
		pygame.sprite.Sprite.__init__(self)
		self.surf = pygame.Surface(size)
		self.surf.fill(gray)
		self.rect = self.surf.get_rect()
		self.location = location
		x, y = location
		self.rect.topleft = (x*brick_side, y*brick_side)

	def togglered(self):
		if self.surf.get_at((0,0)) == gray:
			self.surf.fill(red)
			return True
		else:
			self.surf.fill(gray)
			return False

	def togglewhite(self):
		if self.surf.get_at((0,0)) == gray:
			self.surf.fill(white)
			return True
		else:
			self.surf.fill(gray)
			return False

if __name__ == "__main__":
	endpoints = [None, None]
	barriers = []
	mousefunction = 'barriers'

	pygame.init()

	screen = pygame.display.set_mode(screen_size)
	screen.fill('white')

	bricks = pygame.sprite.Group()

	for x in range(numofcolumns):
		for y in range(numofrows):
			b = brick(brick_size, (x, y))
			screen.blit(b.surf, b.rect)
			bricks.add(b)

	# barriers = [(6,2), (6,3), (6,4), (6,5)]
	# for b in bricks:
	# 	if b.location in barriers:
	# 		b.surf.fill(white)
	# 		screen.blit(b.surf, b.rect)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				point = pygame.mouse.get_pos()
				for b in bricks:
					if (b.rect.collidepoint(point)):
						if mousefunction == 'endpoints':
							if b.togglered():
								endpoints.insert(0,b.location)
								endpoints.pop()
							else:
								bindex = endpoints.index(b.location)
								endpoints.pop(bindex)
								endpoints.append(None)
						elif mousefunction == 'barriers':
							if b.togglewhite():
								barriers.append(b.location)
							else:
								bindex = barriers.index(b.location)
								barriers.pop(bindex)
						screen.blit(b.surf, b.rect)
			if event.type  == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:		#find shortest path
					gameboard = spf.board(numofcolumns, numofrows)
					gameboard.setbarriers(barriers)
					sp = gameboard.dijkstra(endpoints[0],endpoints[1])
					for b in bricks:
						if b.location in sp:
							b.surf.fill(green)
							screen.blit(b.surf, b.rect)
					#print(endpoints)
					#gameboard.printboard()
				if event.key == pygame.K_e:
					mousefunction = 'endpoints'
					#print(mousefunction)
				if event.key == pygame.K_b:
					mousefunction = 'barriers'
					#print(mousefunction)
				if event.key == pygame.K_ESCAPE:    #reset
					endpoints = [None, None]
					barriers = []
					for b in bricks:
						b.surf.fill(gray)
						screen.blit(b.surf, b.rect)
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()