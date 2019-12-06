import miscellaneous as misc
from Deck import Deck
from DecisionMaker import DecisionMaker

class Hand:
	
	def __init__(self, hand, bet = 10):
		count = 0
		self.hand = hand
		self.bet = bet
		count = count + 1
		self.id = count


class Game:

	def __init__(self, player = [], dealer = [], playerDeck = [], dealerDeck = []):

		self.deck = Deck()
		self.initializeHands(player, dealer)
		self.decision = DecisionMaker()
		self.log = open('Log.txt', 'a')
		# self.playerDeck = self.getRanks(self.playerDeck)
		# self.dealerDeck = self.getRanks(self.dealerDeck)


	def initializeHands(self, player, dealer):
		if player == [] and dealer == []:
			self.player = self.cards(2)
			self.dealer = self.cards(2)

		else:
			if self.checkCardtype(player[0]) != 'Rank':
				self.player = self.getRanks(player)
				self.dealer = self.getRanks(dealer)

		playerHand_1 = Hand(self.player)
		self.dealerHand = Hand(self.dealer)
		self.playerHand = []
		self.playerHand.append(playerHand_1)


	def run(self):
		self.startGame(self.playerHand[0].hand)
		return self.findResult()


	def cards(self, numberOfCards):
		cards = []
		for i in range(numberOfCards):
			cards.append(self.getCard())

		return cards

	def startGame(self, playerHand):
		self.log.write('\n\n\nRun ' + str(playerHand) + str(self.dealerHand.hand))
		print('\n\n\nRun ', str(playerHand), str(self.dealerHand.hand))
		self.userTurn(playerHand)
		self.dealerTurn()
		

	def checkCardtype(self, hand):
		flag = 0
		listSplit = list(hand)
		for i in listSplit:
			if i == '-':
				flag = 1

		if flag == 0:
			return 'Rank'
		else:
			return 'Card'


	def getRanks(self, hand):
		rankList = []
		for i in hand:
			tempList = i.split('-')
			rank = tempList[1]
			rankList.append(rank)
		return rankList


	def isBlackJack(self, sumOfCards):
		if sumOfCards == 21:
			return True
		else:
			return False


	def getCard(self, option = ''):
		if option == 'player':
			result = self.playerDeck[0]
			self.playerDeck.remove(result)

		elif option == 'dealer':
			result = self.dealerDeck[0]
			self.dealerDeck.remove(result)

		if option == '':
			result = self.deck.getCards(1)
			result = self.getRanks(result)
		print('Get Card ',result[0])
		return result[0]


	def getDecision(self, playerHand):
		result = self.decision.findOutcome(playerHand, self.dealerHand.hand)
		if result == 'S':
			return 'Stand'
		elif result == 'H':
			return 'Hit'
		elif result == 'P':
			return 'Split'
		elif result == 'D':
			return 'Double'
		elif result == 'Bust':
			return 'Bust'
		elif result == 'BJ':
			return 'BJ'


	def userTurn(self, playerHand):
		decision = self.getDecision(playerHand)
		if decision == 'Stand':
			print('Stand----')
			return
		elif decision == 'Split':
			self.split(playerHand)

		elif decision == 'Hit':
			self.hit(playerHand)

		elif decision == 'Double':
			self.double(playerHand)

		elif decision == 'Bust' or decision == 'BJ':
			return


	def dealerTurn(self):
		while misc.sumOfList(self.dealerHand.hand) < 17:
			self.log.write('\nDealer Turn' + str(self.dealerHand.hand) + str(misc.sumOfList(self.dealerHand.hand)))
			print('Dealer Turn',self.dealerHand.hand, misc.sumOfList(self.dealerHand.hand))
			card = self.getCard()
			#card = self.getRanks([card])
			self.dealerHand.hand.append(card[0])


	def hit(self, playerHand):
		self.log.write('\nHIT')
		print('HIT')
		card = self.getCard()
		#card = self.getRanks([card])
		print('HH: ',card)
		playerHand.append(card)
		self.userTurn(playerHand)


	def split(self, playerHand):
		self.log.write('\nSPLIT')
		print('SPLIT')
		hand1, hand2 = self.splitHand(playerHand)
		self.playerHand.remove(self.removeHand(playerHand))
		handObj1 = Hand(hand1)
		handObj2 = Hand(hand2)
		self.playerHand.append(handObj1)
		self.playerHand.append(handObj2)
		self.startGame(hand1)
		self.startGame(hand2)

		for i in self.playerHand:
			print('here')
			print(i.hand)

	def doubleBet(self, playerHand):
		for handObject in self.playerHand:
			if playerHand == handObject.hand:
				handObject.bet = 20


	def double(self, playerHand):
		#print('DOUBLE')
		card = self.getCard()
		#card = self.getRanks([card])
		playerHand.append(card[0])
		self.doubleBet(playerHand)
		self.log.write('\nDOUBLE' + str(playerHand))
		print('DOUBLE', playerHand)
		return		


	def splitHand(self, playerHand):
		hand1 = [playerHand[0]]
		hand2 = [playerHand[1]]
		hand1.append(self.getCard())
		hand2.append(self.getCard())
		self.log.write('\nSP' + str(hand1) + str(hand2))
		print('SP', hand1, hand2)

		return hand1, hand2

	def removeHand(self, playerHand):
		for i in self.playerHand:
			if i.hand == playerHand:
				objectToBeRemoved = i
		return objectToBeRemoved


	def getMoney(self, gameResult, bet):
		money = {'Won':'10', 'Lost':'-10', 'Draw':'0', 'BlackJack':'15'}
		self.money = int(money.get(gameResult)) * bet/10
		return self.money


	def findResult(self):
		totalMoney = 0
		for handObject in self.playerHand:
			hand = handObject.hand
			self.log.write('\nRESULT: ' + str(self.dealerHand.hand) + str(handObject.id))
			print('Res',hand, self.dealerHand.hand, handObject.id)
			player = misc.sumOfList(hand)
			dealer = misc.sumOfList(self.dealerHand.hand)

			biggerHand = misc.compare(player, dealer)
			bj_player = self.isBlackJack(player)
			bj_dealer = self.isBlackJack(dealer)

			if player > 21:
				result = 'Lost'

			elif dealer > 21:
				result = 'Won'

			elif bj_dealer == True:
				if bj_player == True:
					result = 'Draw'
				else:
					result = 'Lost'

			elif bj_player == True:
				if bj_dealer == True:
					result = 'Draw'
				else:
					result = 'BlackJack'

			elif biggerHand == 1:
				result = 'Won'
			elif biggerHand == 2:
				result = 'Lost'
			elif biggerHand == 0:
				result = 'Draw'

			print(result+'\n\n\n')
			money = self.getMoney(result, handObject.bet)
			totalMoney = int(totalMoney) + money
		return totalMoney


	def calculateResult(self):
		result = self.findResult()
		return result