from data import tenPlayerHoleWinOdds, eightPlayerHoleWinOdds, sixPlayerHoleWinOdds, fourPlayerHoleWinOdds, threePlayerHoleWinOdds, twoPlayerHoleWinOdds, cardRanks
from collections import Counter
class calculator:

	def __init__(self):
		self.currOuts = 0
		pass

	def outs(self, holeCards, commCards, pointOfPlay):
		totalCards = []
		self.currOuts = 0

		if pointOfPlay == 'Flop':
			commCardsToCount = 2
		elif pointOfPlay == 'Turn':
			commCardsToCount = 3

		for card in holeCards:
			currCard = holeCards.get(card)
			totalCards.append(currCard)

		currCountIndex = 0

		for card in commCards:
			currCard = commCards.get(card)
			if currCountIndex <= commCardsToCount:
				totalCards.append(currCard)
				currCountIndex = currCountIndex + 1
			else:
				break

		if self.checkOpenStraightDraw(totalCards) and self.checkFlushDraw(totalCards):
			self.currOuts = 15
		elif self.checkInsideStraightDraw(totalCards) and self.checkFlushDraw(totalCards):
			self.currOuts = 12
		elif self.checkInsideStraightDraw(totalCards) and self.checkTwoOverCardsToOverPair(totalCards):
			self.currOuts = 10
		elif self.checkFlushDraw(totalCards):
			self.currOuts = 9
		elif self.checkOpenStraightDraw(totalCards):
			self.currOuts = 8
		elif self.checkInsideStraightDraw(totalCards):
			self.currOuts = 4
		elif self.checkSetToFullHouseOrFourOfAKind(totalCards):
			self.currOuts = 7
		elif self.checkPocketPairToSet(totalCards):
			self.currOuts = 2
		elif self.checkTwoOverCardsToOverPair(totalCards):
			self.currOuts = 6
		elif self.checkOneOverCardToOverPair(totalCards):
			self.currOuts = 3
		elif self.checkNoPairToPair(totalCards):
			self.currOuts = 6
		elif self.checkTwoPairToFullHouse(totalCards):
			self.currOuts = 4
		elif self.checkOnePairToTwoPairOrSet(totalCards):
			self.currOuts = 5

		return self.currOuts

	def handOdds(self, playerNum, pointOfPlay):
		currHandOdds = 0
		cardsLeftInDeck = 52

		if playerNum == '10 Players':
			cardsLeftInDeck = cardsLeftInDeck - 20
		elif playerNum == '9 Players':
			cardsLeftInDeck = cardsLeftInDeck - 18
		elif playerNum == '8 Players':
			cardsLeftInDeck = cardsLeftInDeck - 16
		elif playerNum == '7 Players':
			cardsLeftInDeck = cardsLeftInDeck - 14
		elif playerNum == '6 Players':
			cardsLeftInDeck = cardsLeftInDeck - 12
		elif playerNum == '5 Players':
			cardsLeftInDeck = cardsLeftInDeck - 10
		elif playerNum == '4 Players':
			cardsLeftInDeck = cardsLeftInDeck - 8
		elif playerNum == '3 Players':
			cardsLeftInDeck = cardsLeftInDeck - 6
		elif playerNum == '2 Players':
			cardsLeftInDeck = cardsLeftInDeck - 4

		if pointOfPlay == 'Flop':
			cardsLeftInDeck = cardsLeftInDeck - 3
			currHandOdds = self.flopToRiverOdds(cardsLeftInDeck)
		elif pointOfPlay == 'Turn':
			cardsLeftInDeck = cardsLeftInDeck - 4
			currHandOdds = self.turnToRiverOdds(cardsLeftInDeck)

		return currHandOdds

	def potOdds(self, currBet, potSize):
		call = currBet
		currPotOdds = (call / (potSize + currBet))
		currPotOdds = round(currPotOdds, 4)


		return currPotOdds

	def callOrFold(self, currPotOdds, currHandOdds):
		if (currPotOdds <= currHandOdds):
			return True
		else:
			return False

	def initialHandOdds(self, playerNum, holeCardVal):
		if playerNum == '10 Players' or playerNum == '9 Players':
			iHandOdds = tenPlayerHoleWinOdds.get(holeCardVal)
		elif playerNum == '8 Players' or playerNum == '7 Players':
			iHandOdds = eightPlayerHoleWinOdds.get(holeCardVal)
		elif playerNum == '6 Players' or playerNum == '5 Players':
			iHandOdds = sixPlayerHoleWinOdds.get(holeCardVal)
		elif playerNum == '4 Players':
			iHandOdds = fourPlayerHoleWinOdds.get(holeCardVal)
		elif playerNum == '3 Players':
			iHandOdds = threePlayerHoleWinOdds.get(holeCardVal)
		elif playerNum == '2 Players':
			iHandOdds = twoPlayerHoleWinOdds.get(holeCardVal)

		return iHandOdds

	def initialHandAction(self, playerNum, iHandOdds):
		if playerNum == '10 Players':
			if iHandOdds >= .1153:
				return 'Call'
			else:
				return 'Fold'
		elif playerNum == '8 Players':
			if iHandOdds > .1439:
				return 'Call'
			else:
				return 'Fold'
		elif playerNum == '6 Players':
			if iHandOdds >= .181:
				return 'Call'
			else:
				return 'Fold'
		elif playerNum == '4 Players':
			if iHandOdds >= .2674:
				return 'Call'
			else:
				return 'Fold'
		elif playerNum == '3 Players':
			if iHandOdds >= .3533:
				return 'Call'
			else:
				return 'Fold'
		elif playerNum == '2 Players':
			if iHandOdds >= .4796:
				return 'Call'
			else:
				return 'Fold'

	def checkOpenStraightDraw(self, totalCards):
		cardRankVals = []
		sortedCardRankVals = []
		consecutiveCards = []

		for card in totalCards:
			cardVal = card[:-1]
			cardRank = cardRanks.get(cardVal)
			cardRankVals.append(cardRank)

		sortedCardRankVals = sorted(cardRankVals)

		lenOfCards = len(cardRankVals)

		for x in range(lenOfCards - 1):
			if (sortedCardRankVals[x] + 1) == sortedCardRankVals[(x + 1)]:
				if sortedCardRankVals[x] not in consecutiveCards:
					consecutiveCards.append(sortedCardRankVals[x])
				if sortedCardRankVals[(x + 1)] not in consecutiveCards:
					consecutiveCards.append(sortedCardRankVals[(x + 1)])

		if len(consecutiveCards) < 4:
			return False
		elif consecutiveCards[0] == 1 or consecutiveCards[-1] == 13:
			return False
		elif len(consecutiveCards) == 4:
			if (consecutiveCards[0] + 1) != consecutiveCards[1]:
				return False
			elif (consecutiveCards[1] + 1) != consecutiveCards[2]:
				return False
			elif (consecutiveCards[2] + 1) != consecutiveCards[3]:
				return False
			else:
				return True

	def checkInsideStraightDraw(self, totalCards):
		cardRankVals = []
		sortedCardRankVals = []
		consecutiveCards = []
		index = 0

		for card in totalCards:
			cardVal = card[:-1]
			cardRank = cardRanks.get(cardVal)
			cardRankVals.append(cardRank)

		sortedCardRankVals = sorted(cardRankVals)

		lenOfCards = len(cardRankVals)

		for x in range(lenOfCards - 1):
			if (sortedCardRankVals[x] + 1) == sortedCardRankVals[(x + 1)]:
				if sortedCardRankVals[x] not in consecutiveCards:
					consecutiveCards.append(sortedCardRankVals[x])
				if sortedCardRankVals[(x + 1)] not in consecutiveCards:
					consecutiveCards.append(sortedCardRankVals[(x + 1)])

		if len(consecutiveCards) < 3:
			return False
		elif len(consecutiveCards) == 4:
			if (consecutiveCards[1] + 2) == consecutiveCards[2]:
				return True
			if consecutiveCards[0] == 1 or consecutiveCards[-1] == 13:
				if (consecutiveCards[0] + 1) != consecutiveCards[1]:
					return False
				elif (consecutiveCards[1] + 1) != consecutiveCards[2]:
					return False
				elif (consecutiveCards[2] + 1) != consecutiveCards[3]:
					return False
				else:
					return True
			else:
				return False
		elif len(consecutiveCards) == 3:
			index = sortedCardRankVals.index(consecutiveCards[0])
			if index == 0:
				pass
			elif sortedCardRankVals[index] == (sortedCardRankVals[index - 1] + 2):
				return True
			index = sortedCardRankVals.index(consecutiveCards[-1])
			if index == (len(sortedCardRankVals) - 1):
				pass
			elif sortedCardRankVals[index] == (sortedCardRankVals[index + 1] - 2):
				return True
			else:
				return False


	def checkFlushDraw(self, totalCards):
		cardSuitVals = []

		for card in totalCards:
			cardSuit = card[-1]
			cardSuitVals.append(cardSuit)

		suitDict = Counter(cardSuitVals)

		for val in suitDict:
			if suitDict.get(val) == 4:
				return True

		return False

	def checkTwoOverCardsToOverPair(self, totalCards):
		cardVals = []
		cardRankVals = []
		commCardRanks = []
		handCardRank1 = 0
		handCardRank2 = 0
		isHandCardOneOver = True
		isHandCardTwoOver = True

		for card in totalCards:
			cardVal = card[:-1]
			cardVals.append(cardVal)

		for val in cardVals:
			cardRankVal = cardRanks.get(val)
			cardRankVals.append(cardRankVal)

		commCardRanks = cardRankVals[-2:]

		handCardRank1 = cardRankVals[0]
		handCardRank2 = cardRankVals[1]

		for rank in commCardRanks:
			if handCardRank1 <= rank:
				isHandCardOneOver = False
				break

		for rank in commCardRanks:
			if handCardRank2 <= rank:
				isHandCardTwoOver = False
				break

		if not isHandCardOneOver or not isHandCardTwoOver:
			return False
		if isHandCardOneOver and isHandCardTwoOver:
			return True


	def checkSetToFullHouseOrFourOfAKind(self, totalCards):
		cardVals = []

		for card in totalCards:
			cardVal = card[:-1]
			cardVals.append(cardVal)

		cardDict = Counter(cardVals)

		for val in cardDict:
			if cardDict.get(val) == 3:
				return True

		return False

	def checkNoPairToPair(self, totalCards):
		cardVals = []

		for card in totalCards:
			cardVal = card[:-1]
			cardVals.append(cardVal)

		cardDict = Counter(cardVals)

		for val in cardDict:
			if cardDict.get(val) != 1:
				return False

		return True

	def checkOnePairToTwoPairOrSet(self, totalCards):
		cardVals = []

		for card in totalCards:
			cardVal = card[:-1]
			cardVals.append(cardVal)

		cardDict = Counter(cardVals)

		if cardVals[0] == cardVals[1]:
			return False

		for val in cardDict:
			if cardDict.get(val) == 2:
				return True

		return False

	def checkTwoPairToFullHouse(self, totalCards):
		cardVals = []
		numOfPairs = 0

		for card in totalCards:
			cardVal = card[:-1]
			cardVals.append(cardVal)

		cardDict = Counter(cardVals)

		for val in cardDict:
			if cardDict.get(val) == 2:
				numOfPairs = numOfPairs + 1

		if numOfPairs == 2:
			return True

		return False

	def checkOneOverCardToOverPair(self, totalCards):
		cardVals = []
		cardRankVals = []
		commCardRanks = []
		handCardRank = 0
		isHandCardOneOver = True
		isHandCardTwoOver = True

		for card in totalCards:
			cardVal = card[:-1]
			cardVals.append(cardVal)

		for val in cardVals:
			cardRankVal = cardRanks.get(val)
			cardRankVals.append(cardRankVal)

		commCardRanks = cardRankVals[-2:]

		handCardRank = cardRankVals[0]

		for rank in commCardRanks:
			if handCardRank < rank:
				isHandCardOneOver = False
				break

		handCardRank = cardRankVals[1]

		for rank in commCardRanks:
			if handCardRank < rank:
				isHandCardTwoOver = False
				break

		if isHandCardOneOver and isHandCardTwoOver:
			return False
		elif not isHandCardOneOver and not isHandCardTwoOver:
			return False
		elif isHandCardOneOver or isHandCardTwoOver:
			return True

	def checkPocketPairToSet(self, totalCards):
		cardVals = []

		for card in totalCards:
			cardVal = card[:-1]
			cardVals.append(cardVal)

		if cardVals[0] == cardVals[1]:
			return True

		return False

	def flopToRiverOdds(self, cardsLeftInDeck):
		flopToRiverOdds = 0

		flopToTurnCardsLeftAfterOuts = float(cardsLeftInDeck - self.currOuts)
		flopToRiverCardsLeftInDeck = float(cardsLeftInDeck - 1)
		flopToRiverCardsLeftAfterOuts = float(flopToRiverCardsLeftInDeck - self.currOuts)
		cardsLeftInDeck = float(cardsLeftInDeck)

		flopToRiverCalc = (flopToTurnCardsLeftAfterOuts/cardsLeftInDeck) * (flopToRiverCardsLeftAfterOuts/flopToRiverCardsLeftInDeck)

		flopToRiverOdds = round((1 - flopToRiverCalc), 4)

		return flopToRiverOdds

	def turnToRiverOdds(self, cardsLeftInDeck):
		turnToRiverOdds = 0

		cardsLeftAfterOuts = cardsLeftInDeck - self.currOuts

		turnToRiverCalc = (float(cardsLeftAfterOuts)/float(cardsLeftInDeck))

		turnToRiverOdds = round((1 - turnToRiverCalc), 4)

		return turnToRiverOdds
