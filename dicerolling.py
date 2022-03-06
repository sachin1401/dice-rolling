# here we use random for creating random number
import random

while True:
    print(random.randint(1,6))
    roll=input("you want to roll dice again? [yes/no]:")
    if roll.lower()=='yes':
        continue
    else:
        break