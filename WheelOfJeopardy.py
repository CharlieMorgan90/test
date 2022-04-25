import random

points = [50, 50, 75, 75, 100, 100, 150, 150, "double jeopardy", 200]

def spinWheel():
    return random.choice(points)

def randomNum():
    num = random.randrange(0,40,2)
    return num

def getAnswer(data, num):
    return(data[num])

def getQuestion(data, num):
    return(data[num])
    
print("Welcome to Wheel Of Jeopardy!!!!!")
print()
player1 = input("Player1 please enter your name: ")
player2 = input("Player2 please enter your name: ")
print()
print("Rules of the Game:")
print("Players will take turns spinning the wheel to determine", end = ' ')
print("the number of points for the current question.", end = ' ')
print("If the wheel lands on 'double jeopardy' you will", end = ' ')
print("be asked to wager a selected amount of points within", end = ' ')
print("your current score at that time.", end = ' ')
print("The same player who spon the wheel will be asked", end = ' ')
print("to choose the topic for the questions.", end = ' ')
print("The question will then be displayed, and both players", end = ' ')
print("must race to determine who gets to answer the question.", end = ' ')
print(player1, "must enter a 1 when they know the answer and", end = ' ')
print(player2, "must enter a 2 when they know the answer,", end = ' ')
print("and if no one knows the answer enter a 3.", end = ' ')
print("Once a number is entered, the player who entered", end = ' ')
print("their number first will be asked for their answer.", end = ' ')
print("If their answer is incorrect they were loose the", end = ' ')
print("amount of points determined above,", end = ' ')
print("if they're correct they will gain those points.", end = ' ')
print("The game ends when a player reaches 1000 points.")
print()
print("Let the games begin!")
print()

turn = 0
score1 = 0
score2 = 0
usedSportsQs = []
usedMusicQs = []
usedVideoGameQs = []
while score1 < 1000 and score2 < 1000:
    if turn % 2 == 0:
        currentPlayer = player1
    else:
        currentPlayer = player2
    
    button = ' '
    while button != '':
        print(currentPlayer, end = ' ')
        button = input("press enter to spin the wheel")
        if button == "":
            prize = spinWheel()
            print("The wheel landed on", prize)
    if prize == "double jeopardy":
        print(player1, "score:", score1)
        print(player1, "enter your wager: ", end = ' ')
        wager1 = int(input(""))
        while wager1 < 0 or wager1 > score1:
            print("Wager is not within zero and your current score, try again: ")
            wager1 = int(input(""))

        print(player2, "score:", score2)
        print(player2, "enter your wager: ", end = ' ')
        wager2 = int(input(""))
        while wager2 < 0 or wager2 > score2:
            print("Wager is not within zero and your current score, try again: ")
            wager2 = int(input(""))
            
    topic = " "
    while topic != "sports" and topic != "music" and topic != "video games":
        print(currentPlayer, end = ' ')
        topic = input("choose a question topic(Sports, Music, Video Games) ")
        topic = topic.lower()
        print()
        if topic == "sports":
            data = open("SportsQuestions.txt", "r")
            data = data.readlines()
            num = randomNum()
            question = getQuestion(data, num)
            while question in usedSportsQs:
                num = randomNum()
                question = getQuestion(data, num)    
            print(question)
            usedSportsQs.append(question)
            answer = getAnswer(data, num + 1)
            players = '4'
            while players != '1' and players != '2' and players != '3':
                players = input("")
                if players == '1':
                    print(player1, "your guess is:", end = ' ')
                    guess = input("")
                    guess = guess.lower()       
                    if guess == "" or guess == " ":
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score1 = score1 - wager1
                        else:
                            score1 = score1 - prize
                    elif guess in answer:
                        print("Correct!")
                        if prize == "double jeopardy":
                            score1 = score1 + wager1
                        else:
                            score1 = score1 + prize
                    else:
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score1 = score1 - wager1
                        else:
                            score1 = score1 - prize
                elif players == '2':
                    print(player2,"your guess is:", end = ' ')
                    guess = input("")
                    guess = guess.lower()
                    if guess == "" or guess == " ":
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score2 = score2 - wager2
                        else:
                            score2 = score2 - prize
                    elif guess in answer:
                        print("Correct!")
                        if prize == "double jeopardy":
                            score2 = score2 + wager2
                        else:
                            score2 = score2 + prize
                    else:
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score2 = score2 - wager2
                        else:
                            score2 = score2 - prize
                elif players == '3':
                    pass
                else:
                    print("Invalid Input!, try again")
                
          
            turn = turn + 1
            print(player1, ":", score1)
            print(player2, ":", score2)
            print()
        
        
        elif topic == "music":
            data = open("MusicQuestions.txt", "r")
            data = data.readlines()
            num = randomNum()
            question = getQuestion(data, num)
            while question in usedMusicQs:
                num = randomNum()
                question = getQuestion(data, num)    
            print(question)
            usedMusicQs.append(question)
            answer = getAnswer(data, num + 1)
            players = '4'
            while players != '1' and players != '2' and players != '3':
                players = input("")
                if players == '1':
                    print(player1, "your guess is:", end = ' ')
                    guess = input("")
                    guess = guess.lower()
                    if guess == "" or guess == " ":
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score1 = score1 - wager1
                        else:
                            score1 = score1 - prize
                    elif guess in answer:
                        print("Correct!")
                        if prize == "double jeopardy":
                            score1 = score1 + wager1
                        else:
                            score1 = score1 + prize
                    else:
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score1 = score1 - wager1
                        else:
                            score1 = score1 - prize
                elif players == '2':
                    print(player2,"your guess is:", end = ' ')
                    guess = input("")
                    guess = guess.lower()
                    if guess == "" or guess == " ":
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score2 = score2 - wager2
                        else:
                            score2 = score2 - prize
                    elif guess in answer:
                        print("Correct!")
                        if prize == "double jeopardy":
                            score2 = score2 + wager2
                        else:
                            score2 = score2 + prize
                    else:
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score2 = score2 - wager2
                        else:
                            score2 = score2 - prize
                elif players == '3':
                    pass
                else:
                    print("Invalid Input!, try again")
          
            turn = turn + 1
            print(player1, ":", score1)
            print(player2, ":", score2)
            print()

        
        elif topic == "video games":
            data = open("VideoGamesQuestions.txt", "r")
            data = data.readlines()
            num = randomNum()
            question = getQuestion(data, num)
            while question in usedVideoGameQs:
                num = randomNum()
                question = getQuestion(data, num)    
            print(question)
            usedVideoGameQs.append(question)
            answer = getAnswer(data, num + 1)
            players = '4'
            while players != '1' and players != '2' and players != '3':
                players = input("")
                if players == '1':
                    print(player1, "your guess is:", end = ' ')
                    guess = input("")
                    guess = guess.lower()
                    if guess == "" or guess == " ":
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score1 = score1 - wager1
                        else:
                            score1 = score1 - prize
                    elif guess in answer:
                        print("Correct!")
                        if prize == "double jeopardy":
                            score1 = score1 + wager1
                        else:
                            score1 = score1 + prize
                    else:
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score1 = score1 - wager1
                        else:
                            score1 = score1 - prize
                elif players == '2':
                    print(player2,"your guess is:", end = ' ')
                    guess = input("")
                    guess = guess.lower()
                    if guess == "" or guess == " ":
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score2 = score2 - wager2
                        else:
                            score2 = score2 - prize
                    elif guess in answer:
                        print("Correct!")
                        if prize == "double jeopardy":
                            score2 = score2 + wager2
                        else:
                            score2 = score2 + prize
                    else:
                        print("Incorrect!")
                        if prize == "double jeopardy":
                            score2 = score2 - wager2
                        else:
                            score2 = score2 - prize
                elif players == '3':
                    pass
                else:
                    print("Invalid Input!, try again")
          
            turn = turn + 1
            print(player1, ":", score1)
            print(player2, ":", score2)
            print()
        
        else:
            print("That isn't a topic")
            topic = " "

if score1 > score2:
    print(player1, "wins!")
else:
    print(player2, "wins!")








            
