#imports
import sys
import pygame
from pygame.locals import *
import board
import spf
import panel

#static
screen_width = 500
screen_height = 400
screen_size = (screen_width, screen_height)
brick_side = 25
numofrows = screen_height//brick_side
numofcolumns = screen_width//brick_side
gray = (152, 152, 152)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

def mouseactions(bricks, setting):
	extraendpoint = None
	point = pygame.mouse.get_pos()
	for b in bricks:
		if (b.rect.collidepoint(point)):
			if setting.mousefunction == 'endpoints':
				if b.togglecolor(red):
					setting.endpoints.insert(0,b.location)
					extraendpoint = setting.endpoints.pop()		#limit number of endpoints
					if extraendpoint:
						x,y = extraendpoint
						extrab = bricks[x*numofrows+y]
						extrab.fillcolor(gray)
						extraendpoint = None
				else:
					bindex = setting.endpoints.index(b.location)
					setting.endpoints.pop(bindex)
					setting.endpoints.append(None)
			elif setting.mousefunction == 'barriers':
				if b.togglecolor(white):
					setting.barriers.append(b.location)
				else:
					bindex = setting.barriers.index(b.location)
					setting.barriers.pop(bindex)

def keyactions(bricks, setting):
	if event.key == pygame.K_SPACE:		#find shortest path
		if setting.endpoints[0] and setting.endpoints[1]:
			gameboard = spf.gameboard(numofcolumns, numofrows)
			gameboard.setbarriers(setting.barriers)
			if setting.algorithm == 'dijkstra':
				if setting.animation:
					sp = gameboard.dijkstra(setting.endpoints, bricks)
				else:
					sp = gameboard.dijkstra(setting.endpoints, None)
			if setting.algorithm == 'a_star':
				if setting.animation:
					sp = gameboard.a_star(setting.endpoints, bricks)
				else:
					sp = gameboard.a_star(setting.endpoints, None)
			if sp:
				for b in bricks:
					if b.location in sp:
						b.fillcolor(green)
			setting.mousefunction = None

	if event.key == pygame.K_ESCAPE:    #reset
		setting.mousefunction = 'endpoints'
		setting.endpoints = [None, None]
		setting.barriers = []
		for b in bricks:
			b.fillcolor(gray)

	# if event.key == pygame.K_e:		#set start/end points
	# 	setting.mousefunction = 'endpoints'
	# if event.key == pygame.K_b:		#set barriers
	# 	setting.mousefunction = 'barriers'
	# if event.key == pygame.K_s:
	# 	setting.algorithm = 'a_star'
	# if event.key == pygame.K_d:
	# 	setting.algorithm = 'dijkstra'
	# if event.key == pygame.K_a:
	# 	setting.animation = not setting.animation

	return setting
#main
if __name__ == "__main__":
	class setting:
		def __init__(self):
			self.mousefunction = 'endpoints'
			self.animation = False
			self.endpoints = [None, None]
			self.barriers = []
			self.algorithm = 'dijkstra'

	pygame.init()
	screen = pygame.display.set_mode(screen_size)

	setting = setting()
	bricks = []

	controlpanel = panel.controlpanel()

	for x in range(numofcolumns):
		for y in range(numofrows):
			b = board.brick((x, y), brick_side, screen)
			b.fillcolor(gray)
			bricks.append(b)

	while True:
		for event in pygame.event.get():
			setting = controlpanel.getsetting(setting)
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouseactions(bricks, setting)
			if event.type  == pygame.KEYDOWN:
				setting = keyactions(bricks, setting)
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		controlpanel.update()
		pygame.display.update()