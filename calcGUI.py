import sys
import functools
from data import cardVals, playerNumChoices, cardChoices, suits, suitVals
from controler import calcControler
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class App(QWidget):

	def __init__(self):
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

	# Initilize the GUI
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.createCardsLayout()
		self.createHandLayout()
		self.createCommunityCardsLayout()
		self.createBetAndPotLayout()
		self.createButtonConnects()

		windowLayout = QGridLayout()
		windowLayout.addWidget(self.horizontalGroupBox, 0, 0)
		windowLayout.addWidget(self.handBox,0,1)
		windowLayout.addWidget(self.betAndPotBox,1,0)
		windowLayout.addWidget(self.communityBox,1,1)
		self.setLayout(windowLayout)

		self.show()

	# Create the layout for the buttons used to choose
	# the value of cards
	def createCardsLayout(self):
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
				cardPickerLayout.addWidget(self.cardValDict[x],a,b)
				a = a + 1
				b = 0
			else:
				cardPickerLayout.addWidget(self.cardValDict[x],a,b)
				b = b + 1

		b = 0
		a = a + 1

		for x in self.suitButtons:
			cardPickerLayout.addWidget(x,a,b)
			b = b + 1

		self.horizontalGroupBox.setLayout(cardPickerLayout)

	# Create the layout that shows the hole cards and
	# displays stats
	def createHandLayout(self):
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
		handLayout.addLayout(oddsLayout, stretch = 1)

		self.handBox.setLayout(handLayout)

	# Creates the layout that shows the community
	# cards
	def createCommunityCardsLayout(self):
		self.communityBox = QGroupBox("Community Cards")
		commLayout = QHBoxLayout()

		cardPath = self.cControler.setCardPicPath('blue_back')

		for card in range(5):
			card = QLabel()
			self.setCardPic(card, cardPath)
			commLayout.addWidget(card)
			self.communityCards.append(card)

		self.communityBox.setLayout(commLayout)

	# Create the layout that allows for inputs such as
	# number of players, cards being chosen and pot value
	def createBetAndPotLayout(self):
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

	# Function to make and return button
	def makeButton(self, text):
		button = QPushButton(text)
		return button

	# Function that takes the value selected and sets
	# the card pic and card val in data structure
	def setCardVal(self, val):
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

	# Function that creates an error pop up
	# for caught exceptions
	def buildErrorPopup(self, errorName):
		errPopup = QErrorMessage()
		errPopup.showMessage(str(errorName))
		errPopup.exec()

	# Function to set the event connections for the
	# click of buttons
	def createButtonConnects(self):
		for x in self.cardValDict:
			self.cardValDict.get(x).clicked.connect(functools.partial(self.setCardVal, x))

		y = 0
		for x in self.suitButtons:
			x.clicked.connect(functools.partial(self.setCardVal, suitVals[y]))
			y = y + 1

		calcButton.clicked.connect(functools.partial(self.calculateClicked))
		clearButton.clicked.connect(functools.partial(self.reset))

	# Function the is called when the calculate button is clicked
	def calculateClicked(self):
		player = playerNum.currentText()
		betSize = betEdit.text()
		potSize = potEdit.text()

		if self.holeCardsCalced == False:
			try:
				self.cControler.setHoleHandVal()
				self.cControler.setPlayerNum(player)
				betOdds.setText('Initial Hand Odds: ' + str(self.cControler.getHoleCardOdds()))
				action = self.cControler.getHoleCardAction()
				actionLabel.setText('Initial Action: ' + action)
				self.holeCardsCalced = True
			except Exception as error:
				self.buildErrorPopup(str(error))
		elif self.holeCardsCalced == True and self.flopCalced == True:
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
		elif self.holeCardsCalced == True:
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

	# Function that is called when the reset button is clicked
	def reset(self):
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

	# Function that takes picks the card that needs to be changed
	def findCardToChange(self, pickedCard, cardPath, cardVal):
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

	# Function that creates the required card pic
	# for the GUI
	def setCardPic(self, pickedCard, imagePath):
		newMap = QPixmap(imagePath)
		pickedCard.setPixmap(newMap.scaled(144,200,Qt.KeepAspectRatio))

	# Functions that set the value and picture of the
	# hole and community cards
	def setHand1(self, imagePath, cardVal):
		self.cControler.setHoleCard('Hole 1', cardVal)
		self.setCardPic(self.holeCards[0], imagePath)

	def setHand2(self, imagePath, cardVal):
		self.cControler.setHoleCard('Hole 2', cardVal)
		self.setCardPic(self.holeCards[1], imagePath)

	def setComm1(self, imagePath, cardVal):
		self.cControler.setCommCard('Flop 1', cardVal)
		self.setCardPic(self.communityCards[0], imagePath)

	def setComm2(self, imagePath, cardVal):
		self.cControler.setCommCard('Flop 2', cardVal)
		self.setCardPic(self.communityCards[1], imagePath)

	def setComm3(self, imagePath, cardVal):
		self.cControler.setCommCard('Flop 3', cardVal)
		self.setCardPic(self.communityCards[2], imagePath)

	def setComm4(self, imagePath, cardVal):
		self.cControler.setCommCard('Turn', cardVal)
		self.setCardPic(self.communityCards[3], imagePath)

	def setComm5(self, imagePath, cardVal):
		self.cControler.setCommCard('River', cardVal)
		self.setCardPic(self.communityCards[4], imagePath)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec())
