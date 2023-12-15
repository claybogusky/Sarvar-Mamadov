
# learn about functions
# learn about random numbers
# learn about input
# string ==> number
# modules

import random

num = random.randint(1, 10)
#guess = None

guess = input("guess a number between 1 and 10: ")
guess = int(guess)
if guess == num:
    print("congratulations! you won!")
else:
    print("nope, sorry. try again!")
