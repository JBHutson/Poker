

import os

from calc import calculator


class calcControler:
        """ Controler class that connects the GUI to the
        to the actual Calculator
        """
        def __init__(self):
                """initial function that sets values to class
                variables
                """
                self.pCalc = calculator()
                self.playerNum = ''
                self.formatedHandVal = ''
                self.pointInPlay = ''
                self.holeCards = {
                        'Hole 1': '',
                        'Hole 2': ''
                        }
                self.commCards = {
                        'Flop 1': '',
                        'Flop 2': '',
                        'Flop 3': '',
                        'Turn': '',
                        'River': ''
                        }

        def setCardPicPath(self, cardVal):
                """ Creates the path to the card immage.

                Params:
                cardVal -- string with the card value
                """
                cardPicPathEnd = cardVal + '.jpg'
                currDirectory = os.getcwd()
                cardPicPath = os.path.join(currDirectory, 'JPEG', cardPicPathEnd)
                if os.path.isfile(cardPicPath):
                        return cardPicPath
                else:
                        raise Exception('Not a card')

        def setHoleCard(self, holeCardNum, cardVal):
                """ Sets the selcted hole card to the given value.

                Params:
                holeCardNum -- string dictating the chosen card
                cardVal -- string containing the value of the card
                """
                if holeCardNum == 'Hole 1':
                        holeCards['Hole 1'] = cardVal
                elif holeCardNum == 'Hole 2':
                        holeCards['Hole 2'] = cardVal

        def setCommCard(self, commCardNum, cardVal):
                """ Sets the selcted community card to the given value.

                Params:
                commCardNum -- string dictating the chosen card
                cardVal -- string containing the value of the card
                """
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

        def setHoleHandVal(self):
                """ Creates a hole hand value in the required format"""
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

        def setPlayerNum(self, players):
                """ Set the number of players

                Params:
                players -- string with the number of players
                """
                self.playerNum = players

        def getHoleCardOdds(self):
                """ Get the initial hole card odds."""
                iHandOdd = self.pCalc.initialHandOdds(self.playerNum, self.formatedHandVal)
                return iHandOdd

        def getHoleCardAction(self):
                """ Get the initial hole card action."""
                iHandOdd = self.getHoleCardOdds()
                iHandAction = self.pCalc.initialHandAction(self.playerNum, iHandOdd)

                return iHandAction

        def getPotOdds(self, costToCall, potSize):
                """ Get the pot odds.

                Params:
                costToCall -- int containing the how much is needed to call
                potSize -- int containing the size of the pot
                """
                potOdds = self.pCalc.potOdds(costToCall, potSize)

                return potOdds

        def getCurrentOuts(self):
                """ Get the current number of outs """
                currOuts = self.pCalc.outs(holeCards, commCards, self.pointInPlay)

                return currOuts

        def checkIsInt(self, pot, bet):
                """ Check to see if the values passed for pot and bet are ints

                Params:
                pot -- int containing the size of the pot
                bet -- int containing the size of the bet
                """
                try:
                        val = int(pot)
                        val2 = int(bet)
                except ValueError:
                        raise Exception('Must input both pot and bet values')

        def setPointInPlay(self):
                """ Set the point of play in a particular hand """
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
                """ Get the current hand odds after initial hole odds """
                currOdds = self.pCalc.handOdds(self.playerNum, self.pointInPlay)

                return currOdds

        def getAction(self, currPotOdds, currHandOdds):
                """ Get the action to take after the initial hole action.

                Params:
                currPotOdds -- int containing the current pot odds
                currHandOdds -- int containing the current hand odds
                """
                action = ''

                if self.pCalc.callOrFold(currPotOdds, currHandOdds):
                        action = 'Call'
                else:
                        action = 'Fold'

                return action

        def resetPointInPlay(self):
                """ Resets the point in play """
                self.pointInPlay = ''
