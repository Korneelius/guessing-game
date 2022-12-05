"""SCRIPT"""

# BOILERPLATE
import random

# this generates a random number between 1 and 10
number = random.randint(1, 10)

TRIES = 0
# GAME LOOP
while TRIES < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    
    TRIES = TRIES + 1

# implement your logic below
    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low")
    elif guess == number:
        print("You got it!")
        break
    elif TRIES == 3:
        print("You lose!")
        break
if TRIES == 3:
    print("That was your last try!")