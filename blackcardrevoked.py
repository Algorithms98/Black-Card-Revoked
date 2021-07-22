from question import *

class BlackCardRevoked:

	def __init__(self):

		self.players = []
		self.points = {} 	#key = player_name, value = player_points
		self.answer = " "
		self.quiz = Questions()



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
			namecount += 1

	#adds or deducts points after each question or round
	def scorePoints(self):
		return 0

	#who is replying now and next
	def repliesFirst(self):
		return 0

	#checks to see which player has the most points at the end of the game
	def checkWinner(self):
		return 0

	#This function will check the user’s input to see if it is a correct answer
	def isCorrect(self):
		return True

	#takes user input
	def playGame(self):
		print("Welcome to BlackCardRevoked")
		self.takeInput()






