#imports
import math

#data structure
class board():

	def __init__(self, width, height):
		self.height = height
		self.width = width
		self.numofv = height*width
		self.dist = [[math.inf for column in range(width)]
		for row in range(height)]
		self.spt = [[False for column in range(width)]
		for row in range(height)]

	def getwidthrange(self,x):
		if x == 0:
			return 0, x+2
		elif x == self.width-1:
			return x-1, x+1
		else:
			return x-1, x+2

	def getheightrange(self,y):
		if y == 0:
			return 0, y+2
		elif y == self.height-1:
			return y-1, y+1
		else:
			return y-1, y+2

	def setbarriers(self, barriers):
		for barrier in barriers:
			x, y = barrier
			self.spt[y][x] = math.inf

	def printboard(self):
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
	def mindistv(self):
		mini = math.inf
		minv = None
		for y in range(len(self.dist)):
			for x in range(len(self.dist[y])):
				if self.dist[y][x]<mini and self.spt[y][x] ==False:
					mini = self.dist[y][x]
					minv = (x, y)
		return minv

	def dijkstra(self, startpoint, endpoint):
		xstart,ystart = startpoint
		xend, yend = endpoint

		self.dist[ystart][xstart] = 0

		while not self.spt[yend][xend]:
			(x, y) = self.mindistv()
			self.spt[y][x] = True

			xl, xu = self.getwidthrange(x)
			yl, yu = self.getheightrange(y)

			for i in range(yl, yu):
				for j in range(xl, xu):
					if self.spt[i][j] == False and self.dist[i][j]>1+self.dist[y][x]:
						self.dist[i][j] = 1+self.dist[y][x]

		distance = self.dist[yend][xend]
		shortestpath = [(xend, yend)]
		while distance != 0:
			xl, xu = self.getwidthrange(xend)
			yl, yu = self.getheightrange(yend)

			for i in range(yl, yu):
				for j in range(xl, xu):
					if self.dist[i][j] < distance:
						shortestpath.insert(0, (j,i))
						distance = self.dist[i][j]
						xend = j
						yend = i
						break
				else:
					continue
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