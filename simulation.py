from blackJack import Game
from matplotlib import pyplot as plt
import numpy as np 


class Bucket:
	def __init__(self, startingPoint, endingPoint):
		self.startingPoint = startingPoint
		self.endingPoint = endingPoint
		self.values = []

	def isInBucket(self, value):
		if value > self.startingPoint and value < self.endingPoint:
			return 1
		else:
			return 0

	def addToBucket(self, value):
		self.values.append(value)


class Plot:
	def __init__(self, data):
		self.data = data
		self.bucketList = []
		self.createBucket()
		self.dumpData()

	def createBucket(self):
		start = -40
		end = -20
		for i in range(20):
			Object = Bucket(start, end)	
			self.bucketList.append(Object)
			start = end + 1
			end = (start-1)+20

	def dumpData(self):
		for i in self.data:
			self.findBucket(i)

	def findBucket(self, value):
		for bucket in self.bucketList:
			if bucket.isInBucket(value) == 1:
				bucket.addToBucket(value)

	def showGraph(self):
		for i in self.bucketList:
			print(len(i.values), i.startingPoint, i.endingPoint)
			file = open("Result.txt", "a")
			file.write('\n[' + str(i.startingPoint) + ', ' + str(i.endingPoint) + '] -> ' + str(len(i.values)))


def start():
	game = Game()
	result = game.run()
	return result


def plot(data):
	x_axis = []
	for i in range(len(data)):
		x_axis.append(i)

	plt.scatter(x_axis, data)
	plt.show()

def writeData(data):
	file = open('Simulation_result.txt','a')
	for i in data:
		file.write(str(i))

def runSimulation(numberOfGames):
	sum = 200
	for i in range(numberOfGames):
		if sum <= 0:
			break
		game = Game()
		result = game.run()
		sum = sum + result

	return sum, i+1
	print('Final: ',sum)
	print('Number of times ran: ', i+1)


def simulation(numberOfTimes):
	result = []
	for i in range(numberOfTimes):
		print(i)
		finalAmount, numberOfTimesRan = runSimulation(100)
		result.append(finalAmount)

	pl = Plot(result)
	pl.showGraph()
	writeData(result)
	print(result)


if __name__ == "__main__":
	simulation(1000)