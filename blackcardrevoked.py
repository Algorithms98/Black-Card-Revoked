from question import *
from random import randint


class BlackCardRevoked:

    def __init__(self):

        self.players = []
        self.points = {}  # key = player_name, value = player_points
        self.answer = {}  # key = player_name , value = answer
        self.cards = Questions()
        self.questionNum = 0  # question number being asked
        self.currentCard = 0
        self.cardsUsed = []
        self.goingFirst = -1  # who's turn it is to play first

    # this function initializes the game, lays out the rules for the game as well as serving as the main loop of the game.

    def takeInput(self):
        print("Instructions")
        print("- To begin you will enter the total number of players and then each player's name.")
        print("- Before starting you will have the option of adding your own question or not to the game.")
        print("- Each player will take turns being the first to answer each question.")
        print("- To answer a question you type out one of the four possible answers given on your turn.")
        print("- Once each player has gone first at least once, the players can choose to end or continue the game.")
        print("- The player(s) with the most points at the end wins.\n")

        print("How many people are playing today?")
        numPlayers = input()
        isValid = numPlayers.isnumeric()

        while isValid == False:
            print("Invalid input. Try again.")
            numPlayers = input()
            if numPlayers.isnumeric():
                isValid = True
                break
        print("\nPlease enter your names")

        namecount = 0
        while namecount < int(numPlayers):
            name = input()
            self.players.append(name)
            self.points[name] = 0
            self.answer[name] = ""
            namecount += 1

    # who is replying now and next

    def repliesFirst(self):
        self.goingFirst += 1
        return self.goingFirst

    # return players with the most points at the end of the game
    def checkWinner(self):
        highScore = max(self.points.values())
        winners = [[w, p] for w, p in self.points.items() if p == highScore]
        return winners

    # This function will check the user’s input to see if it is a correct answer
    def isCorrect(self, answer):

        correct = False
        if answer == self.cards.getAnswer(self.currentCard):
            correct = True
        else:
            correct = False
        return correct

    # adds or deducts points after each question or round
    def scorePoints(self):

        for i in range(len(self.players)):
            if self.isCorrect(self.answer[self.players[i]]) == True:
                # award a point for correct answer
                self.points[self.players[i]] += 1
            else:
                # give zero points for each wrong answer
                self.points[self.players[i]] += 0

    # takes user input
    def blackCard(self):
        self.questionNum += 1
        self.currentCard = randint(1, len(self.cards.quiz))
        while self.currentCard in self.cardsUsed:
            self.currentCard = randint(1, len(self.cards.quiz))
        self.cardsUsed.append(self.currentCard)
        self.repliesFirst()

        # Resets to question 1 after using all the cards
        if self.questionNum == len(self.cards.getDeck()):
            self.questionNum = 1
            self.currentCard = randint(1, len(self.cards.quiz))
            self.cardsUsed = [self.currentCard]

        print(f"\nGet ready for question number, {self.questionNum}")
        print("================================\n")
        print(self.cards.getQuestion(self.currentCard))
        print("\nPossible Answers\n")
        print(self.cards.getAnswers(self.currentCard))

        print(f"\nPlayer, {self.players[self.goingFirst]} answers first")
        self.answer[self.players[self.goingFirst]] = input()
        for i in range(self.goingFirst+1, len(self.players)):
            print(f"\nPlayer, {self.players[i]} enter your answer here")
            self.answer[self.players[i]] = input()

        if self.goingFirst != 0:
            for i in range(0, self.goingFirst):
                print(f"\nPlayer, {self.players[i]} enter your answer here")
                self.answer[self.players[i]] = input()

    def printWinners(self, winnersArray):
        print("\nWINNER(S):")
        for winner in winnersArray:
            print(f"{winner[0]} - {winner[1]} point(s)")

    def playGame(self):
        print("Welcome to Black Card Revoked\n")
        self.takeInput()

        play = True
        self.cards.addQuestions()

        while play:
            
            self.blackCard()
            self.scorePoints()

            # option to continue playing after all players have gone first
            if self.goingFirst == len(self.players)-1:
                print("\nAll playeres have gone first at least once\n")
                print("Do you want to continue playing Y/N ?")
                decision = input()

                if decision.upper() != 'Y':
                    champs = self.checkWinner()
                    self.printWinners(champs)
                    play = False
                    break

                else:
                    champs = self.checkWinner()
                    self.printWinners(champs)
                    play = True
                    self.goingFirst = -1  # Reset to the first player
