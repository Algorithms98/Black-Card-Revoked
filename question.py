class Questions:
    
    def __init__(self):
        self.q = ""
        self.a = []
        self.ra = ""
        self.num = 11
        self.quiz = {
            1 : {
                "question" : "After you stop and drop, what should you do next?",
                "answers" : ["shut 'em down, open up shop", "put your hands up", "roll", "hand over your liscense and registration"],
                "answer" : "shut 'em down, open up shop"
                
            },
            2 : {
                "question" : "If Young Metro don't trust you, what might Future do?" ,
                "answers" : ["call the police", "shoot you", "fight you", "beat you"],
                "answer" : "shoot you"
            },
            3 : {
                "question" : "What might momma tell you before going into any store?",
                "answers" : ["don't touch nothing", "don't ask for nothing", "don't look for nothing", "all of the above"],
                "answer" : "all of the above"
            },
            4 : {
                "question" : "Who was Oprah Winfrey's best friend?",
                "answers" : ["gayle king", "tyler perry", "stedman graham", "cicely tyson"],
                "answer" : "gayle king"
            },
            5 : {
                "question" : "In what city did Rosa Parks refuse to give up her seat?",
                "answers" : ["tuskegee, alabama", "montgomery, alabama", "birmingham, alabama", "jackson, mississippi"],
                "answer" : "montgomery, alabama"
            },
            6 : {
                "question" : "According to Kanye, who doesn't have the answers?",
                "answers" : ["taylor swift", "beck", "jay-z", "sway"],
                "answer" : "sway"
            },
            7 : {
                "question" : "In what years did Cash Money Records take over?" ,
                "answers" : ["2001 - 2002", "1999 - 2000", "1997 - 1998", "2004 - 2005"],
                "answer" : "1999 - 2000"
            },
            8 : {
                "question" : "In what city was MLK Jr Killed?",
                "answers" : ["atlanta, ga", "washington dc", "birmingham, al" "memphis, tn"],
                "answer" : "memphis, tn"
            },
            9 : {
                "question" : "Who is Steve Urkel's cool alter ego?",
                "answers" : ["stan", "scotty", "stefan", "shawn"],
                "answer" : "stefan"
            },
            10 : {
                "question" : "What might momma say you need in order to get some McDonald's?",
                "answers" : ["a job", "a clue", "good grades", "mcdonald's money"],
                "answer" : "mcdonald's money"
            }
        }
        
        
    def getQuestions(self):
            
        for question in self.quiz:
            return(self.quiz[question]['question'])
        
    def getAnswers(self, num):
        return self.quiz[num]['answers']

    def getAnswer(self, num):
        return self.quiz[num]['answer']

    def getQuestion(self, num):
        return self.quiz[num]['question']

    def getDeck(self):
        return self.quiz

         
        
    def addQuestions(self): #q - question, a - answers, ra - real answer
        
        print("Before, we start, do you want to add a question? Type in Y/N")
        answer = input().lower()
        if answer == 'y':
            print("Please enter in the question you want to add")
            self.q = input()
            print("Please enter in the possible answers to your added question")
            for i in range(0, 4):
                temp = str(input())
                self.a.append(temp)
            print("Please enter in the real answer to your question")
            self.ra = input()
            self.quiz.update({self.num : {"question": "%s" % (self.q), "answers": ["%s" % (self.a[0]), "%s" % (self.a[1]), "%s" % (self.a[2]), "%s" % (self.a[3])], "answer" : "%s" % (self.ra)}})
            #print(self.quiz)
            self.num += 1
        
        else:
            return -1

#test = Questions()
#test.addQuestions()
#print("Outside")