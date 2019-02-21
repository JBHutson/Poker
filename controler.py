import os
from calc import calculator

class calcControler:

	def __init__(self):
		self.pCalc = calculator()
		self.playerNum = ''
		self.formatedHandVal = ''
		self.pointInPlay = ''

	global holeCards, commCards

	# dicts that hold the value of the hole and
	# community cards
	holeCards = {
		'Hole 1': '',
		'Hole 2': ''
		}

	commCards = {
		'Flop 1': '',
		'Flop 2': '',
		'Flop 3': '',
		'Turn': '',
		'River': ''
		}

	# Function that gets the path to the pic of the card
	# passed to it, also checks if the card value is
	# a real card
	def setCardPicPath(self, cardVal):
		cardPicPathEnd = cardVal + '.jpg'
		cardPicPath = os.path.join('C:/', 'Users', 'James-PC', 'Documents', 'Poker', 'JPEG', cardPicPathEnd )
		if os.path.isfile(cardPicPath):
			return cardPicPath
		else:
			raise Exception('Not a card')

	# Function used to set hole card value in internal
	# data structure
	def setHoleCard(self, holeCardNum, cardVal):
		if holeCardNum == 'Hole 1':
			holeCards['Hole 1'] = cardVal
		elif holeCardNum == 'Hole 2':
			holeCards['Hole 2'] = cardVal

	# Function used to set community card value in internal
	# data structure
	def setCommCard(self, commCardNum, cardVal):
		if commCardNum == 'Flop 1':
			commCards['Flop 1'] = cardVal
		elif commCardNum == 'Flop 2':
			commCards['Flop 2'] = cardVal
		elif commCardNum == 'Flop 3':
			commCards['Flop 3'] = cardVal
		elif commCardNum == 'Turn':
			commCards['Turn'] = cardVal
		elif commCardNum == 'River':
			commCards['River'] = cardVal

	# Function that creates a hole hand value in the required
	# format to be able to retrive the initial hand odds from
	# internal data structures
	def setHoleHandVal(self):
		self.formatedHandVal = ''

		try:
			holeOneVal = holeCards.get('Hole 1')
			holeTwoVal = holeCards.get('Hole 2')

			self.formatedHandVal = holeOneVal[:-1]
			self.formatedHandVal = self.formatedHandVal + holeTwoVal[:-1]

			if holeOneVal[:-1] == holeTwoVal[:-1]:
				self.formatedHandVal = self.formatedHandVal + '_P'
			elif holeOneVal[-1:] == holeTwoVal[-1:]:
				self.formatedHandVal = self.formatedHandVal + '_S'
			else:
				self.formatedHandVal = self.formatedHandVal + '_U'
		except:
			raise Exception('Must input both hole cards')

	# Function that sets the number of players for calculations
	def setPlayerNum(self, players):
		self.playerNum = players

	# Function that gets the initial hole card odds from calculator
	def getHoleCardOdds(self):
		iHandOdd = self.pCalc.initialHandOdds(self.playerNum, self.formatedHandVal)
		return iHandOdd

	# Function that gets the initial action that should be taken based
	# on hole cards recieved
	def getHoleCardAction(self):
		iHandOdd = self.getHoleCardOdds()
		iHandAction = self.pCalc.initialHandAction(self.playerNum, iHandOdd)

		return iHandAction

	# Function that receives pot odds determined by the calc
	def getPotOdds(self, costToCall, potSize):
		potOdds = self.pCalc.potOdds(costToCall, potSize)

		return potOdds

	def getCurrentOuts(self):
		currOuts = self.pCalc.outs(holeCards, commCards, self.pointInPlay)

		return currOuts

	def checkIsInt(self, pot, bet):
		try:
			val = int(pot)
			val2 = int(bet)
		except ValueError:
			raise Exception('Must input both pot and bet values')

	def setPointInPlay(self):
		commCardsNum = 0

		for card in commCards:
			if commCards[card] != '':
				commCardsNum = commCardsNum + 1

		if commCardsNum == 3 and self.pointInPlay == '':
			self.pointInPlay = 'Flop'
		elif commCardsNum == 4:
			self.pointInPlay = 'Turn'
		else:
			raise Exception('Must Input the correct Number of Comm cards')

	def getHandOdds(self):
		currOdds = self.pCalc.handOdds(self.playerNum, self.pointInPlay)

		return currOdds

	def getAction(self, currPotOdds, currHandOdds):
		action = ''

		if self.pCalc.callOrFold(currPotOdds, currHandOdds):
			action = 'Call'
		else:
			action = 'Fold'

		return action

	def resetPointInPlay(self):
		self.pointInPlay = ''
