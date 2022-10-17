import random

# Game - Rock Paper Scissors 

def gameWin(comp,player):
    # If two values are equal, declare a tie!
    if comp == player:
        return None
   
    # Check for all possibilities when computer chose r
    elif comp == "r":
        if player == "p":
            return True
        elif player == "s":
            return False
    
    # Check for all possibilities when computer chose p
    elif comp == "p":
        if player == "s":
            return True
        elif player == "r":
            return False
    # Check for all possibilities when computer chose s
    elif comp == "s":
        if player == "r":
            return True
        elif player == "p":
            return False



# Prints Welcome Message
print(" Welcome to Rock , Paper or Scissors Game By Manaan Mattoo")
print(" Get Ready , You'll be playing against the Computer !\n")

# Prints comp input has been registered
print("Computer has choosen it's tool !")

# Give random value to comp and assigning a str to those values
randno = random.randint(1,3)
if randno == 1:
    comp = "r"
elif randno == 2:
    comp = "p"
else :
    comp = "s"

# Takes input from user
player = input("Your Turn , Rock(r), Paper(p) or Scissors(s) ?\n")

# starts user defined function
a = gameWin(comp, player)

# Prints the choices choosen by both CPU and the player
print(f"Choices : The Computer choose {comp} and You choose {player}")

# Assinging what to print with None & True/False Bool operators used in user defined func()
if a == None:
    print("It is a Tie !\n")
elif a == True:
    print("You Won!\n")
else:
    print("You Lost!\n")

#End of the Prog

