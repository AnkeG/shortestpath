#imports
import sys
import pygame
from pygame.locals import *
import board
import spf

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

def mouseactions(mousefunction, endpoints, barriers):
	extraendpoint = None
	point = pygame.mouse.get_pos()
	for b in bricks:
		if (b.rect.collidepoint(point)):
			if mousefunction == 'endpoints':
				if b.togglered():
					endpoints.insert(0,b.location)
					extraendpoint = endpoints.pop()		#limit number of endpoints
					if extraendpoint:
						x,y = extraendpoint
						extrab = bricks[x*numofrows+y]
						extrab.surf.fill(gray)
						screen.blit(extrab.surf, extrab.rect)
						extraendpoint = None
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

def keyactions(endpoints, barriers):
	if event.key == pygame.K_SPACE:		#find shortest path
		gameboard = spf.board(numofcolumns, numofrows)
		gameboard.setbarriers(barriers)
		sp = gameboard.dijkstra(endpoints[0],endpoints[1])
		for b in bricks:
			if b.location in sp:
				b.surf.fill(green)
				screen.blit(b.surf, b.rect)
	if event.key == pygame.K_e:		#set start/end points
		return 'endpoints'
	if event.key == pygame.K_b:		#set barriers
		return 'barriers'
	if event.key == pygame.K_ESCAPE:    #reset
		endpoints = [None, None]
		barriers = []
		for b in bricks:
			b.surf.fill(gray)
			screen.blit(b.surf, b.rect)
		return 'endpoints'
#main
if __name__ == "__main__":

	mousefunction = 'endpoints'
	endpoints = [None, None]
	barriers = []

	pygame.init()

	screen = pygame.display.set_mode(screen_size)
	bricks = []

	for x in range(numofcolumns):
		for y in range(numofrows):
			b = board.brick(brick_size, (x, y), brick_side)
			screen.blit(b.surf, b.rect)
			bricks.append(b)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouseactions(mousefunction, endpoints, barriers)
			if event.type  == pygame.KEYDOWN:
				mousefunction = keyactions(endpoints, barriers)
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()