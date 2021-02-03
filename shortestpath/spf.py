#imports
import math

#data structure
class board():

	def __init__(self, height, width):
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

	def printboard(self):
		for row in self.dist:
			row_str = str()
			for v in row:
				row_str += str(v)+' '
			print(row_str)

	def printspt(self):
		for row in self.spt:
			row_str = str()
			for v in row:
				row_str += str(v)+' '
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
		coordx,coordy = startpoint
		self.dist[coordy-1][coordx-1] = 0

		xend, yend = endpoint
		xend, yend = xend-1, yend-1

		while not self.spt[yend][xend]:
			(x, y) = self.mindistv()
			self.spt[y][x] = True

			xl, xu = self.getwidthrange(x)
			yl, yu = self.getheightrange(y)

			for i in range(yl, yu):
				for j in range(xl, xu):
					if self.spt[i][j] == False and self.dist[i][j]>1+self.dist[y][x]:
						self.dist[i][j] = 1+self.dist[y][x]

#main for tests
if __name__ == "__main__":
	test = board(5, 5)
	#test.printboard()
	#(x,y) = test.mindistv()
	#print(x, y)
	test.dijkstra((3,5),(5,4))
	test.printboard()
	test.printspt()
