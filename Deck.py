import random
class Deck:
	deck = []
	rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	suit = ['C', 'D', 'H', 'S']

	def __init__(self):
		self.reshuffleDeck()

	def reshuffleDeck(self):
		for i in range(4):
			for j in range(13):
				temp = self.suit[i] +'-'+ self.rank[j]
				self.deck.append(temp)
				temp = ''


	def inDeck(self, card):
		isPresent = 0

		if self.deck == []:
			return 2

		for i in self.deck:
			if i == card:
				isPresent = 1
				
		return isPresent


	def getCards(self, size):
		shuffle = True
		i = 0
		hand = []
		while len(hand) < size and i == 0:
			s = random.randint(0,3)
			r = random.randint(0,12)
			card = self.suit[s] +'-'+ self.rank[r]
			if self.inDeck(card) == 1:
				self.deck.remove(card)
				hand.append(card)

			elif self.inDeck(card) == 2:
				if shuffle == True:
					self.reshuffleDeck()
				else:
					i = 1

		return hand


	def takeCard(self, card):
		if self.inDeck(card) == 1:
			self.deck.remove(card)
			return 1
		else:
			return 0

	def printDeck(self):
		print(self.deck)
