import random

def menuChoice():
    print("Option 1: Display rules")
    print("Option 2: Start new game")
    print("Option 3: Quit")
    choice = int(input("What would you like to do? "))
    while (choice < 1 or choice > 3):
        print("That is not a valid choice.")
        choice = int(input("Please enter a number between 1 and 3: "))
    return choice

def displayRules():
    print("The rules of the game are as follows: \n \
    Players take turns to throw two dice. \n \
    If the throw is a `double`, i.e. two 2s, two 3s, etc., \n \
    the player's score reverts to zero and their turn ends. \n \
    (etc.)")

def playerTurn(player, score):
    print("Your turn,", player)
    anotherGo = "Y"
    scoreThisTurn = 0
    while (anotherGo == "Y" or anotherGo == "y"):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print("You rolled,", die1, "and", die2)
        if (die1 == die2):
            scoreThisTurn = 0
            cumulativeScore = 0
            anyKey = input("Bad luck! Press any key to continue: ")
            anotherGo = "N"
        else:
            scoreThisTurn = scoreThisTurn + die1 + die2
            cumulativeScore = score + scoreThisTurn
            print("Your score this turn is", scoreThisTurn)
            print(player, "Your cumulative score is", cumulativeScore)
            if (cumulativeScore >= 50):
                anotherGo = "N"
            else:
                anotherGo = input("Another go? (Answer 'Y' or 'N')")
    return cumulativeScore

def playGame():
    score1 = 0
    score2 = 0
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    while (score1 < 50 and score2 < 50):
        score1 = playerTurn(player1, score1)
        if (score1 >= 50):
            print("You win!")
        else:
            score2 = playerTurn(player2, score2)
            if (score2 >= 50):
                print("You win!")
