def menuChoice():
    print("Option 1: Display rules")
    print("Option 2: Start new game")
    print("Option 3: Quit")
    choice = int(input("What would you like to do? "))
    while (choice < 1 or choice > 3):
        print("That is not a valid choice.")
        choice = int(input("Please enter a number between 1 and 3: "))
    return choice
