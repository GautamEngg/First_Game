# Snake Water Gun Game

import random

# Print any number between 1 to 6
"""
r_number = random.randint(1,6)
print(r_number)
"""

def game_result(sys, player):
    if sys == player:
        return None
    elif sys == 'S':
        if player == 'W':
            return False
        if player == 'G':
            return True 
    elif sys == 'W':
        if player == 'G':
            return False
        if player == 'S':
            return True
    elif sys == 'G':
        if player == 'S':
            return False
        if player == 'W':
            return True

print("Player1/system Turn: Snake(S) Water(W) or Gun(G)?")
r_number = random.randint(1,3)

if r_number == 1:
    sys = 'S'
elif r_number == 2:
    sys = 'W'
elif r_number == 3:
    sys = 'G' 

player = input("Player/your Turn: Snake(S) Water(W) or Gun(G)?")

a = game_result(sys, player)

print(f"sys choose {sys}")
print(f"You choose {player}")

if a == None:
    print("The Game is Tie")
elif a:
    print("Congratulations.... You Win!!!!")
else:
    print("Sorry.. You lose")
