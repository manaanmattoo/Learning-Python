# Game - Rock Paper Scissors 
import random

def gameWin(comp,player):
    if comp == player:
        return None
    elif comp == "r":
        if player == "p":
            return True
        elif player == "s":
            return False
    elif comp == "p":
        if player == "s":
            return True
        elif player == "r":
            return False
    elif comp == "s":
        if player == "r":
            return True
        elif player == "p":
            return False


print(" Welcome to Rock , Paper or Scissors Game By Manaan Mattoo")
print(" Get Ready , You'll be playing against the Computer !\n")

print("Computer has choosen it's tool !")
randno = random.randint(1,3)
if randno == 1:
    comp = "r"
elif randno == 2:
    comp = "p"
else :
    comp = "s"

player = input("Your Turn , Rock(r), Paper(p) or Scissors(s) ?\n")

a = gameWin(comp, player)

print(f"Choices : The Computer choose {comp} and You choose {player}")

if a == None:
    print("It is a Tie !\n")
elif a == True:
    print("You Won!\n")
else:
    print("You Lost!\n")

