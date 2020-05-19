
from random import *
import numpy as np


def game():
    player = int(input("Select the number from the list:"))
    if (player is numbers):
        print("you win")
    else:
        print("you loss")
        print("Number:",numbers)

def random():
    global numbers
    random_nums = list()
    for i in range(5):
        numbers = randrange(1, 50)
        random_nums.append(int(numbers))
    global a
    a=set(random_nums)
    print(type(a))
    print("pick one from the list:",a)
    #print("list:",random_nums)
while True:
    play_nextgame = input("\n**Want to play New Game YES or NO \n type (y or n)**:")
    while(play_nextgame.lower() != 'y'  and play_nextgame.lower() != 'n'):
        play_nextgame = input("please select (y/n) :")
    if (play_nextgame.lower() == 'y'):
        print("$$$ Lets Play $$$")
        print("1$ to play :) ")
        amount = int(input("Insert amount:"))
        if amount > 1:
            print("collect the change:", amount - 1, "$")
        random()  # random numbers function
        if amount == 1:
            print(" start ")
            game()
        else:
            print(" start ")
            game()
    elif (play_nextgame.lower() == 'n'):
        print("Thank You")
        break
    else:
        pass
    ###git








