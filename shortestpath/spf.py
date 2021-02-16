#imports
import math
import board
import pygame
#static
yellow = (255,255,0)
#data structure
class gameboard():

	def __init__(self, width, height):
		self.height = height
		self.width = width
		self.numofv = height*width
		self.dist = [[math.inf for column in range(width)]
		for row in range(height)]
		self.spt = [[False for column in range(width)]
		for row in range(height)]

	def getwidthrange(self,x):		#detect edges
		if x == 0:
			return 0, x+2
		elif x == self.width-1:
			return x-1, x+1
		else:
			return x-1, x+2

	def getheightrange(self,y):		#detect edges
		if y == 0:
			return 0, y+2
		elif y == self.height-1:
			return y-1, y+1
		else:
			return y-1, y+2

	def getneighbors(self, x, y):		#used for checking up/down/left/right first
		xl, xu = self.getwidthrange(x)
		yl, yu = self.getheightrange(y)
		neighbors = []
		for i in range(yl, yu):
			for j in range(xl, xu):
				if i == y or j == x:
					neighbors.insert(0, (j, i))
				else:
					neighbors.append((j, i))
		return neighbors

	def setbarriers(self, barriers):
		for barrier in barriers:
			x, y = barrier
			self.spt[y][x] = math.inf

	def printboard(self):			#debug tool
		for row in self.dist:
			row_str = str()
			for v in row:
				row_str += str(v)+'\t'
			print(row_str)

	def printspt(self):    
		for row in self.spt:
			row_str = str()
			for v in row:
				row_str += str(v)+'\t'
			print(row_str)

#path-finding
	def mindistv(self):				#find vertice with minimum distance
		mini = math.inf
		minv = None
		for y in range(len(self.dist)):
			for x in range(len(self.dist[y])):
				if self.dist[y][x]<mini and self.spt[y][x] ==False:
					mini = self.dist[y][x]
					minv = (x, y)
		return minv

	def dijkstra(self, endpoints, bricks):
		xstart,ystart = endpoints[0]
		xend, yend = endpoints[1]

		self.dist[ystart][xstart] = 0

		while not self.spt[yend][xend]:
			mindist = self.mindistv()
			if not mindist:
				return None
			x, y = mindist
			self.spt[y][x] = True
			if bricks:
				clock = pygame.time.Clock()
				bricks[x*self.height+y].fillcolor(yellow)
				pygame.display.update()
				clock.tick(50)

			xl, xu = self.getwidthrange(x) 
			yl, yu = self.getheightrange(y)

			for i in range(yl, yu):
				for j in range(xl, xu):
					if self.spt[i][j] == False and self.dist[i][j]>1+self.dist[y][x]:
						self.dist[i][j] = 1+self.dist[y][x]

		#record the shortest path
		distance = self.dist[yend][xend]
		shortestpath = [(xend, yend)]
		while distance != 0:
			neighbors = self.getneighbors(xend, yend)
			for neighbor in neighbors:
				dx, dy = neighbor
				if self.dist[dy][dx] < distance:
					shortestpath.insert(0, (dx,dy))
					distance = self.dist[dy][dx]
					xend = dx
					yend = dy
					break
		return shortestpath

#tests
if __name__ == "__main__":
	test = board(5, 5)
	barriers = [(1,2),(1,3),(1,4)]
	test.setbarriers(barriers)
	#test.printboard()
	#(x,y) = test.mindistv()
	#print(x, y)
	shortestpath = test.dijkstra((2,3),(0,0))
	test.printboard()
	#test.printspt()
	print(shortestpath)