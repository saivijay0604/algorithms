
from random import *
import numpy as np
import time


def game():
    player = int(input("Pick one number from the list:"))
    if (player is numbers):
        print(" WIN ")
    else:
        print("Winning Number:",numbers)
        print("Try Again")

def random_Num_Selection():
    global numbers
    random_nums = list()
    for i in range(5):
        numbers = randrange(1, 50)
        random_nums.append(int(numbers))
    a_set=set(random_nums)
    time.sleep(0.50)
    print("\n\tStart the Game\t")
    time.sleep(0.80)
    print(" NUMBERS : ",a_set)
while True:
    play_nextgame = input("\n**Want to play New Game '$' only** \n  CLICK (Y/N):")
    if(play_nextgame.lower() != 'y'  and play_nextgame.lower() != 'n'):
        play_nextgame = input("Please CLICK (Y/N) :")
    if (play_nextgame.lower() == ('y' or 'Y')):
        print("\n \t$$$ Lets Play $$$\t")
        print("\t\t1$ to play\t\t")
        amount = int(input("\tInsert amount:"))
        if amount > 1:
            print("Collect the change:", amount - 1,"$")
        random_Num_Selection()  # random numbers function
        if amount == 1:
            game()
        else:
            game()
    elif (play_nextgame.lower() == ('n' or 'N')):
        print("\tThank You\t")
        break
    else:
        pass









