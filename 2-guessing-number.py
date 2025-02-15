from random import randint
from art import guessNumLogo
print(guessNumLogo)
print("Welcome to the Number Guessing game!")
print("I'm thinking of a number 1 to 100")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

answer = randint(1, 100)

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

turns = set_difficulty()

def check_answer(guess, answer, turns):
    if (answer < guess):
        print("Too high")
        return turns - 1
    elif(answer > guess):
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


print(answer)
def guess(answer, turns):
    guess = 0
    while(answer != guess):
        guess = int(input('Make a guess:'))
        print(f"You have {turns} attemps remaining to the guss number")
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
guess(answer, turns)
