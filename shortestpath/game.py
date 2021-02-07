#imports
import sys
import pygame
from pygame.locals import *
import board
import spf

#globals
mousefunction = 'endpoints'
endpoints = [None, None]
barriers = []

#static
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

def mouseactions():
	global mousefunction, endpoints, barriers
	extraendpoint = None
	point = pygame.mouse.get_pos()
	for b in bricks:
		# if extraendpoint and b.location == extraendpoint:
		# 	b.togglered()
		# 	extraendpoint = None
		if (b.rect.collidepoint(point)):
			if mousefunction == 'endpoints':
				if b.togglered():
					endpoints.insert(0,b.location)
					extraendpoint = endpoints.pop()
					if extraendpoint:
						for bx in bricks:
							if bx.location == extraendpoint:
								bx.surf.fill(gray)
								screen.blit(bx.surf, bx.rect)
								extraendpoint = None
								break
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

def keyactions():
	global mousefunction, endpoints, barriers
	if event.key == pygame.K_SPACE:		#find shortest path
		gameboard = spf.board(numofcolumns, numofrows)
		gameboard.setbarriers(barriers)
		sp = gameboard.dijkstra(endpoints[0],endpoints[1])
		for b in bricks:
			if b.location in sp:
				b.surf.fill(green)
				screen.blit(b.surf, b.rect)
	if event.key == pygame.K_e:
		mousefunction = 'endpoints'
	if event.key == pygame.K_b:
		mousefunction = 'barriers'
	if event.key == pygame.K_ESCAPE:    #reset
		endpoints = [None, None]
		barriers = []
		for b in bricks:
			b.surf.fill(gray)
			screen.blit(b.surf, b.rect)
#main
if __name__ == "__main__":

	pygame.init()

	screen = pygame.display.set_mode(screen_size)
	bricks = pygame.sprite.Group()

	for x in range(numofcolumns):
		for y in range(numofrows):
			b = board.brick(brick_size, (x, y), brick_side)
			screen.blit(b.surf, b.rect)
			bricks.add(b)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouseactions()
			if event.type  == pygame.KEYDOWN:
				keyactions()
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()