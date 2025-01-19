import random
#game dice = 6
#two dice = 6
#total = 12
#12 - you won the game
#8 --- you can play - choice
# you lost the game
while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    if total == 12:
        print("You won the game")
        break
    elif total == 8:
        print("You can play - choice")
    else:    
        print("Dice values are: ", total)
        print("You lost the game")
        break