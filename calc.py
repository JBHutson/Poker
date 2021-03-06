

from collections import Counter

from data import *


class calculator:
    """ Calculator class that contains all of the functions
    related to calculating outs and odds.
    """
    def __init__(self):
        self.currOuts = 0
        pass

    def outs(self, holeCards, commCards, pointOfPlay):
            """ Calculate the number of outs.

            Params:
            holeCards (list): list of hole cards
            commCards (list): list of community cards
            pointOfPlay (str): string indicating the point in play

            Returns:
            currOuts (int): the number of outs
            """
            totalCards = []
            self.currOuts = 0
            currCountIndex = 0

            if pointOfPlay == 'Flop':
                commCardsToCount = 2
            elif pointOfPlay == 'Turn':
                commCardsToCount = 3

            for card in holeCards:
                currCard = holeCards.get(card)
                totalCards.append(currCard)

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
        """ Calculate the hand odds given number of players
            and point of play.

        Params:
        playerNum (str): string with number of player
        pointOfPlay (str): string showing point in play

        Returns:
        currHandOdds (int): odds stat for current hand
        """
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
        """ Calculate the pot odds.

        Params:
        currBet (int): Int containing how much you have to bet
        potSize (int): Int containing the current pot size

        Returns:
        currPotOdds (int): current pot odds stat
        """
        call = currBet
        currPotOdds = (call / (potSize + currBet))
        currPotOdds = round(currPotOdds, 4)

        return currPotOdds

    def callOrFold(self, currPotOdds, currHandOdds):
        """ Decide whether to call or fold.

        Params:
        currPotOdds (int): int containing the current pot odds
        currHandOdds (int):  int containing the current hand odds

        Returns:
        returns true if the player should call, false if they should fold
        """
        if (currPotOdds <= currHandOdds):
            return True
        else:
            return False

    def initialHandOdds(self, playerNum, holeCardVal):
        """ Find the initial hand odds of pocket cards.

        Params:
        playerNum (str): string containing the number of players
        holeCardVal (str): string containing the value of hole cards

        Returns:
        iHandOdds (int): the initial hand odds
        """
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
        """ Decide whether to call or fold pocket cards.

        Params:
        playerNum (str): string containing the number of players
        iHandOdds (int): int containing initial hand card odds

        Returns:
        returns initial hand action
        """
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
        """ Check if there is an open straight draw.

        Params:
        totalCards (list): list containing all of the cards in play

        Returns:
        Bool: true if there is a draw, false if not
        """
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
        """ Check for an inside straight draw.

        Params:
        totalCards (list): list containing all of the cards in play

        Returns:
        Bool: true if there is a draw, false if not
        """
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
        """ Check for a flush draw.

        Params:
        totalCards (list): list containing all of the cards in play

        Returns:
        Bool: true if there is a draw, false if not
        """
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
        """ Check for an over pair draw.

        Params:
        totalCards (list): list containing all of the cards in play

        Returns:
        Bool: true if there is a draw, false if not
        """
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
        """ Check for a full house or four of a kind draw.

        Params:
        totalCards (list): list containing all of the cards in play

        Returns:
        Bool: true if there is a draw, false if not
        """
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
        """ Check for a pair draw.

        Params:
        totalCards (list): list containing all of the cards in play

        Returns:
        Bool: true if there is a draw, false if not
        """
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
        """ Check for two pair or set draw

        Params:
        totalCards (list): list containing all of the cards in play

        Returns:
        Bool: true if there is a draw, false if not
        """
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
        """ Check for a full house draw.

        Params:
        totalCards (list): list containing all of the cards in play

        Returns:
        Bool: true if there is a draw, false if not
        """
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
        """ Check for an over pair draw.

        Params:
        totalCards (list): list containing all of the cards in play

        Returns:
        Bool: true if there is a draw, false if not
        """
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
        """ Check for a set draw with a pocket pair.

        Params:
        totalCards (list): list containing all of the cards in play

        Returns:
        Bool: true if there is a draw, false if not
        """
        cardVals = []

        for card in totalCards:
            cardVal = card[:-1]
            cardVals.append(cardVal)

        if cardVals[0] == cardVals[1]:
            return True

        return False

    def flopToRiverOdds(self, cardsLeftInDeck):
        """ Calculate the odds of a winning hand flop to river.

        Params:
        cardsLeftInDeck (int): int with the number of cards left in the deck

        Returns:
        flopToRiverOdds (float): odds of getting a winning hand flop to river
        """
        flopToRiverOdds = 0

        flopToTurnCardsLeftAfterOuts = float(cardsLeftInDeck - self.currOuts)
        flopToRiverCardsLeftInDeck = float(cardsLeftInDeck - 1)
        flopToRiverCardsLeftAfterOuts = float(flopToRiverCardsLeftInDeck - self.currOuts)
        cardsLeftInDeck = float(cardsLeftInDeck)
        flopToRiverCalc = (flopToTurnCardsLeftAfterOuts/cardsLeftInDeck) * (flopToRiverCardsLeftAfterOuts/flopToRiverCardsLeftInDeck)
        flopToRiverOdds = round((1 - flopToRiverCalc), 4)

        return flopToRiverOdds

    def turnToRiverOdds(self, cardsLeftInDeck):
        """ Calculate the odds of a winning hand turn to river.

         Params:
        cardsLeftInDeck (int): int with the number of cards left in the deck

        Returns:
        turnToRiverOdds (float): odds of getting a winning hand turn to river
        """
        turnToRiverOdds = 0
        cardsLeftAfterOuts = cardsLeftInDeck - self.currOuts
        turnToRiverCalc = (float(cardsLeftAfterOuts)/float(cardsLeftInDeck))
        turnToRiverOdds = round((1 - turnToRiverCalc), 4)

        return turnToRiverOdds
