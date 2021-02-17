#imports
import math, heapq
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
		self.barriers = []

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
				if (j, i) not in self.barriers:
					if i == y or j == x:
						neighbors.insert(0, (j, i))
					else:
						neighbors.append((j, i))
		return neighbors

	def setbarriers(self, barriers):
		self.barriers = barriers

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
			if not mindist:			#No path
				return None
			x, y = mindist
			self.spt[y][x] = True
			if bricks:
				clock = pygame.time.Clock()
				bricks[x*self.height+y].fillcolor(yellow)
				pygame.display.update()
				clock.tick(50)
			neighbors = self.getneighbors(x, y)
			for neighbor in neighbors:
				dx, dy = neighbor
				if self.spt[dy][dx] == False and self.dist[dy][dx]>1+self.dist[y][x]:
					self.dist[dy][dx] = 1+self.dist[y][x]

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

	def h_score(self, node, end):
		return max(abs(node[0]-end[0]), abs(node[1]-end[1]))

	def a_star(self, endpoints, bricks):
		xstart,ystart = endpoints[0]
		xend,yend = endpoints[1]

		open_list = []
		heapq.heappush(open_list, (0, (xstart, ystart)))

		cameFrom = dict()

		gscore = self.dist.copy()
		gscore[ystart][xstart] = 0

		fscore = self.dist.copy()
		fscore[ystart][xstart] = self.h_score((xstart, ystart), (xend, yend))

		while open_list:
			current_f, current = heapq.heappop(open_list)
			if current == (xend, yend):
				shortestpath = [current]
				while current in cameFrom:
					current = cameFrom[current]
					shortestpath.append(current)
				return shortestpath
			x, y = current
			neighbors = self.getneighbors(x, y)
			for neighbor_x,neighbor_y in neighbors:
				temp_g = gscore[y][x] +1
				if temp_g < gscore[neighbor_y][neighbor_x]:
					cameFrom[(neighbor_x, neighbor_y)] = current
					gscore[neighbor_y][neighbor_x] = temp_g
					f = fscore[neighbor_y][neighbor_x] = temp_g + self.h_score((neighbor_x, neighbor_y), (xend, yend))
					if (f, (neighbor_x, neighbor_y)) not in open_list:
						heapq.heappush(open_list, (f, (neighbor_x, neighbor_y)))

		return False



#tests
if __name__ == "__main__":
	test = gameboard(5, 5)
	barriers = [(1,2),(1,3),(1,4)]
	test.setbarriers(barriers)
	#test.printboard()
	#(x,y) = test.mindistv()
	#print(x, y)
	#shortestpath = test.dijkstra((2,3),(0,0))
	shortestpath = test.a_star([(2,3),(0,0)], None)
	#test.printboard()
	#test.printspt()
	print(shortestpath)