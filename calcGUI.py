

import functools
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from controler import calcControler
from data import cardVals, playerNumChoices, cardChoices, suits, suitVals


class App(QWidget):
    """ App class that represents the GUI of the
    Poker Calculator
    """

    def __init__(self):
        """ Initialization function that defines
        variables and constants used in GUI and
        calls the first set up function

        Variables:
        suitButtons (list): list that will contain suit button values
        cardValDict (dict): dictinary that will contain the values and
                            button references for card values
        holeCards (list): list that will contain the values of hole cards
        communityCards (list): list that will contain the values of community
                               cards
        firstClick (bool): boolean that lets the program know if the first card
                           value has been picked
        holeCardsCalced (bool): boolean value that tells the program that the
                                statistics for the initial hole cards have been
                                calculated
        flopCalced (bool): boolean value that tells the program that the statistics
                           for the flop have been calculated
        turnCalced (bool): boolean value that tells the program that the statistics
                           for the turn have been calculated
        riverCalced (bool): boolean value that tells the program that the statistics
                            for the river have been calculated
        cardVal (str): string that will contain the value of the current picked card

        Constants:
        title (str): string with the title of the GUI
        left (int): int with the y-value for the GUI
        top (int): int with the x-value for the GUI
        width (int): int with the width of the GUI
        height (int): int with the height of the GUI
        """
        
        super().__init__()
        self.cControler = calcControler()
        self.suitButtons = []
        self.cardValDict = {}
        self.holeCards = []
        self.communityCards = []
        self.firstClick = True
        self.holeCardsCalced = False
        self.flopCalced = False
        self.turnCalced = False
        self.riverCalced = False
        self.cardVal = ''
        self.title = 'Poker Calculator'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        """ Create the initial GUI setup """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createCardsLayout()
        self.createHandLayout()
        self.createCommunityCardsLayout()
        self.createBetAndPotLayout()
        self.createButtonConnects()

        windowLayout = QGridLayout()
        windowLayout.addWidget(self.horizontalGroupBox, 0, 0)
        windowLayout.addWidget(self.handBox, 0, 1)
        windowLayout.addWidget(self.betAndPotBox, 1, 0)
        windowLayout.addWidget(self.communityBox, 1, 1)
        self.setLayout(windowLayout)

        self.show()

    def createCardsLayout(self):
        """ Create the layout of buttons used to choose
        the value of cards
        """
        self.horizontalGroupBox = QGroupBox("Cards")
        cardPickerLayout = QGridLayout()

        cardValButtons = []

        for val in cardVals:
            button = QPushButton(val)
            cardValButtons.append(button)

        for suit in suits:
            button = QPushButton(suit)
            self.suitButtons.append(button)

        self.cardValDict = dict(zip(cardVals, cardValButtons))

        a = 0
        b = 0

        for x in self.cardValDict:
            if b == 4:
                cardPickerLayout.addWidget(self.cardValDict[x], a, b)
                a = a + 1
                b = 0
            else:
                cardPickerLayout.addWidget(self.cardValDict[x], a, b)
                b = b + 1

        b = 0
        a = a + 1

        for x in self.suitButtons:
            cardPickerLayout.addWidget(x, a, b)
            b = b + 1

        self.horizontalGroupBox.setLayout(cardPickerLayout)

    def createHandLayout(self):
        """ Create the layout that shows the hole cards and
        displays stats
        """    
        self.handBox = QGroupBox("Hand")
        handLayout = QHBoxLayout()
        oddsLayout = QVBoxLayout()

        cardPath = self.cControler.setCardPicPath('blue_back')

        global betOdds, potOdds, outs, actionLabel

        for card in range(2):
            card = QLabel()
            self.setCardPic(card, cardPath)
            handLayout.addWidget(card)
            self.holeCards.append(card)

        betOdds = QLabel('Hand Odds')
        potOdds = QLabel('Pot Odds')
        outs = QLabel('Outs')
        actionLabel = QLabel('Fold or Call')

        oddsLayout.addWidget(betOdds)
        oddsLayout.addWidget(potOdds)
        oddsLayout.addWidget(outs)
        oddsLayout.addWidget(actionLabel)
        handLayout.addLayout(oddsLayout, stretch=1)

        self.handBox.setLayout(handLayout)

    def createCommunityCardsLayout(self):
        """ Create the layout that shows the community
        cards
        """
        self.communityBox = QGroupBox("Community Cards")
        commLayout = QHBoxLayout()

        cardPath = self.cControler.setCardPicPath('blue_back')

        for card in range(5):
            card = QLabel()
            self.setCardPic(card, cardPath)
            commLayout.addWidget(card)
            self.communityCards.append(card)

        self.communityBox.setLayout(commLayout)

    def createBetAndPotLayout(self):
        """ Create the layout that allows for inputs such as
        number of players, cards being chosen and pot value
        """
        self.betAndPotBox = QGroupBox("Bet and Pot")
        betPotLayout = QVBoxLayout()
        calcClearLayout = QHBoxLayout()

        global cardChoice, playerNum, betEdit, potEdit, calcButton, clearButton

        cardChoice = QComboBox()
        cardChoice.addItems(cardChoices)

        playerNum = QComboBox()
        playerNum.addItems(playerNumChoices)

        betEdit = QLineEdit()
        betEdit.setPlaceholderText('Bet')

        potEdit = QLineEdit()
        potEdit.setPlaceholderText('Pot')

        calcButton = QPushButton('Calculate')
        clearButton = QPushButton('Clear')

        betPotLayout.addWidget(cardChoice)
        betPotLayout.addWidget(playerNum)
        betPotLayout.addWidget(betEdit)
        betPotLayout.addWidget(potEdit)

        calcClearLayout.addWidget(calcButton)
        calcClearLayout.addWidget(clearButton)

        betPotLayout.addLayout(calcClearLayout)

        self.betAndPotBox.setLayout(betPotLayout)

    def makeButton(self, text):
        """ Function to make and return button

        Params:
        text (str): value that will be displayed on button

        Returns:
        button (button object): button object with the corresponding text
        """
        button = QPushButton(text)
        return button

    def setCardVal(self, val):
        """ Function that takes the value selected and sets
        the card pic and card val in data structure

        Params:
        val (str): value that represents the selected card
        """
        if self.firstClick:
            self.cardVal = val
            self.firstClick = False
        elif not self.firstClick:
            self.cardVal = self.cardVal + val
            try:
                cardPath = self.cControler.setCardPicPath(self.cardVal)
                pickedCard = cardChoice.currentText()
                self.findCardToChange(pickedCard, cardPath, self.cardVal)
                self.cardVal = ''
                self.firstClick = True
            except Exception as error:
                self.firstClick = True
                self.cardVal = ''
                self.buildErrorPopup(str(error))

    def buildErrorPopup(self, errorName):
        """  Function that creates a GUI popup stating
        an error has occured

        Params:
        errorName (str): value that states the type of error
        """
        errPopup = QErrorMessage()
        errPopup.showMessage(str(errorName))
        errPopup.exec()

    def createButtonConnects(self):
        """ Function to set the event connections for the
        click of buttons
        """
        for x in self.cardValDict:
            self.cardValDict.get(x).clicked.connect(functools.partial(self.setCardVal, x))

        y = 0
        for x in self.suitButtons:
            x.clicked.connect(functools.partial(self.setCardVal, suitVals[y]))
            y = y + 1

        calcButton.clicked.connect(functools.partial(self.calculateClicked))
        clearButton.clicked.connect(functools.partial(self.reset))

    def calculateClicked(self):
        """ Function called when the calculate button is clicked"""
        player = playerNum.currentText()
        betSize = betEdit.text()
        potSize = potEdit.text()

        if self.holeCardsCalced is False:
            try:
                self.cControler.setHoleHandVal()
                self.cControler.setPlayerNum(player)
                betOdds.setText('Initial Hand Odds: ' + str(self.cControler.getHoleCardOdds()))
                action = self.cControler.getHoleCardAction()
                actionLabel.setText('Initial Action: ' + action)
                self.holeCardsCalced = True
            except Exception as error:
                self.buildErrorPopup(str(error))
        elif self.holeCardsCalced is True and self.flopCalced is True:
            try:
                self.cControler.checkIsInt(potSize, betSize)
                self.cControler.setPointInPlay()
                currOuts = self.cControler.getCurrentOuts()
                handOddsVal = self.cControler.getHandOdds()
                betOdds.setText('Hand Odds: ' + str(handOddsVal))
                potOddsVal = self.cControler.getPotOdds(int(betSize), int(potSize))
                potOdds.setText('Pot Odds: ' + str(potOddsVal))
                action = self.cControler.getAction(potOddsVal, handOddsVal)
                actionLabel.setText('Action: ' + action)
                outs.setText('Outs: ' + str(currOuts))
                self.turnCalced = True
            except Exception as error:
                self.buildErrorPopup(str(error))
        elif self.holeCardsCalced is True:
            try:
                self.cControler.checkIsInt(potSize, betSize)
                self.cControler.setPointInPlay()
                currOuts = self.cControler.getCurrentOuts()
                handOddsVal = self.cControler.getHandOdds()
                betOdds.setText('Hand Odds: ' + str(handOddsVal))
                potOddsVal = self.cControler.getPotOdds(int(betSize), int(potSize))
                potOdds.setText('Pot Odds: ' + str(potOddsVal))
                action = self.cControler.getAction(potOddsVal, handOddsVal)
                actionLabel.setText('Action: ' + action)
                outs.setText('Outs: ' + str(currOuts))
                self.flopCalced = True
            except Exception as error:
                self.buildErrorPopup(str(error))

    def reset(self):
        """ Function that is called when the reset button is clicked"""
        betEdit.clear()
        potEdit.clear()

        actionLabel.setText('Fold or Call')
        betOdds.setText('Hand Odds')
        potOdds.setText('Pot Odds')
        outs.setText('Outs')
        cardChoice.setCurrentIndex(0)

        self.holeCardsCalced = False
        self.flopCalced = False
        self.turnCalced = False
        self.cControler.resetPointInPlay()

        cardPath = self.cControler.setCardPicPath('blue_back')

        self.setHand1(cardPath, '')
        self.setHand2(cardPath, '')
        self.setComm1(cardPath, '')
        self.setComm2(cardPath, '')
        self.setComm3(cardPath, '')
        self.setComm4(cardPath, '')
        self.setComm5(cardPath, '')

    def findCardToChange(self, pickedCard, cardPath, cardVal):
        """ Function that picks the card that needs to be changed

        Params:
        pickedCard (str): value that has the card in hand to be changed
        cardPath (str): string that is the file path to the image of the card
        cardVal (str): states the value and suit of the card
        """
        if pickedCard == 'Hole 1':
            self.setHand1(cardPath, cardVal)
        elif pickedCard == 'Hole 2':
            self.setHand2(cardPath, cardVal)
        elif pickedCard == 'Flop 1':
            self.setComm1(cardPath, cardVal)
        elif pickedCard == 'Flop 2':
            self.setComm2(cardPath, cardVal)
        elif pickedCard == 'Flop 3':
            self.setComm3(cardPath, cardVal)
        elif pickedCard == 'Turn':
            self.setComm4(cardPath, cardVal)
        elif pickedCard == 'River':
            self.setComm5(cardPath, cardVal)

    def setCardPic(self, pickedCard, imagePath):
        """ Function that creates the rquired card pic
        for the GUI

        Params:
        pickedCard (str): the suit and value of the card
        imagePath (str): the file path to the card image
        """
        newMap = QPixmap(imagePath)
        pickedCard.setPixmap(newMap.scaled(144, 200, Qt.KeepAspectRatio))

    def setHand1(self, imagePath, cardVal):
        """ Function that sets the value and picture of the
        first hand card

        Params:
        imagePath (str): the file path to the card image
        cardVal (str): the suit and value of the card
        """
        self.cControler.setHoleCard('Hole 1', cardVal)
        self.setCardPic(self.holeCards[0], imagePath)

    def setHand2(self, imagePath, cardVal):
        """ Function that sets the value and picture of the
        second hand card

        Params:
        imagePath (str): the file path to the card image
        cardVal (str): the suit and value of the card
        """
        self.cControler.setHoleCard('Hole 2', cardVal)
        self.setCardPic(self.holeCards[1], imagePath)

    def setComm1(self, imagePath, cardVal):
        """ Function that sets the value and picture of the
        first community card

        Params:
        imagePath (str): the file path to the card image
        cardVal (str): the suit and value of the card
        """
        self.cControler.setCommCard('Flop 1', cardVal)
        self.setCardPic(self.communityCards[0], imagePath)

    def setComm2(self, imagePath, cardVal):
        """ Function that sets the value and picture of the
        second community card

        Params:
        imagePath (str): the file path to the card image
        cardVal (str): the suit and value of the card
        """
        self.cControler.setCommCard('Flop 2', cardVal)
        self.setCardPic(self.communityCards[1], imagePath)

    def setComm3(self, imagePath, cardVal):
        """ Function that sets the value and picture of the
        third community card

        Params:
        imagePath (str): the file path to the card image
        cardVal (str): the suit and value of the card
        """
        self.cControler.setCommCard('Flop 3', cardVal)
        self.setCardPic(self.communityCards[2], imagePath)

    def setComm4(self, imagePath, cardVal):
        """ Function that sets the value and picture of the
        fourth community card

        Params:
        imagePath (str): the file path to the card image
        cardVal (str): the suit and value of the card
        """
        self.cControler.setCommCard('Turn', cardVal)
        self.setCardPic(self.communityCards[3], imagePath)

    def setComm5(self, imagePath, cardVal):
        """ Function that sets the value and picture of the
        fifth community card

        Params:
        imagePath (str): the file path to the card image
        cardVal (str): the suit and value of the card
        """
        self.cControler.setCommCard('River', cardVal)
        self.setCardPic(self.communityCards[4], imagePath)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
