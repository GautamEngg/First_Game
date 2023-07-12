# Rock Paper Scissors Game
# Basic game in python
import random

# Print any number between 1 to 6
"""
r_number = random.randint(1,6)
print(r_number)
"""

def game_result(sys, player):
    if sys == player:
        return None
    elif sys == 'R':
        if player == 'S':
            return False
        if player == 'P':
            return True 
    elif sys == 'P':
        if player == 'R':
            return False
        if player == 'S':
            return True
    elif sys == 'S':
        if player == 'P':
            return False
        if player == 'R':
            return True

print("Player1/system Turn: Rock(R) Paper(P) or Scissor(S)?")
r_number = random.randint(1,3)

if r_number == 1:
    sys = 'R'
elif r_number == 2:
    sys = 'P'
elif r_number == 3:
    sys = 'S' 

player = input("Player/your Turn: Rock(R) Paper(P) or Scissor(S)?")

a = game_result(sys, player)

print(f"sys choose {sys}")
print(f"You choose {player}")

if a == None:
    print("The Game is Tie")
elif a:
    print("Congratulations.... You Win!!!!")
else:
    print("Sorry.. You lose")
