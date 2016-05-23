import random

secretNumber = random.randint(1, 20)

print("Guess a number between 1 and 20...")

# the game starts now
for guessTaken in range(1, 76):
    print("Take a guess:")
    num = int(input())

    if num < secretNumber:
        print("Guess higher...")
    elif num > secretNumber:
        print("Guess lower...")
    else:
        break # for correct guess

if num == secretNumber:
    print("Great job! you have guessed in " + str(guessTaken) + " guesses")
else:
    print("Nope!! My number is "+ str(secretNumber))