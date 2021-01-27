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
