from question import *

class BlackCardRevoked:

	def __init__(self):

		self.players = []
		self.points = {} 	#key = player_name, value = player_points
		self.answer = {}	#key = player_name , value = answer
		self.cards = Questions()
		self.questionNum = 1 #question number being asked



	#this function initializes the game, lays out the rules for the game as well as serving as the main loop of the game.
	def takeInput(self):
		print("Welcome to BlackCardRevoked")
		print("How many people are playing today?")
		numPlayers = input()
		isValid == numPlayers.isnumeric()

		while isValid == False:
			print("Invalid input. Try again.")
			numPlayers = input()
			if numPlayers.isnumeric():
				isValid = True
				break
		print("Please enter your names")

		namecount = 0
		while namecount < numPlayers:
			name = input()
			self.players.append(name)
			self.points[name] = 0
			self.answer[name] = ""
			namecount += 1

	#adds or deducts points after each question or round
	def scorePoints(self):

		for i in range(len(self.players)):
			if isCorrect( answer[self.players[i]] ) == True:
				self.points[self.players[i]] += 1 #award a point for correct answer
			else:
				self.points[self.players[i]] += 0 #give zero points for each wrong answer 
		

	#who is replying now and next
	def repliesFirst(self):
		return 0

	#checks to see which player has the most points at the end of the game
	def checkWinner(self):
		return 0

	#This function will check the user’s input to see if it is a correct answer
	def isCorrect(self, answer):

		correct = False
		if answer == self.card.getAnswer(questionNum):
			correct = True
		else:
			correct = False
		return correct

	#takes user input
	def playGame(self):
		print("Welcome to Black Card Revoked")
		self.takeInput()






