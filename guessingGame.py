"""
    Abejar, Jayharron Mar
    BSIT - 3
    04549 - IT ELECT PYTHON
    9:00 - 11:30am tth
    
    Activity #1

	Guessing game
	
	A program that would enable the user to set integer limit for a value to be guess.
	The program generate a random value from set limit.
	If user enters a larger, the program displays "too large",
	If user enters a smaller, the program displays "too small",
	If user enters a correct value, the program displays "You got it right!",
	and displays the number of tries the user does.
	
	Example Output:
	
	Input Lower Limit(n):1
	Input Upper Limit(n):32
	--------------------
	
	Enter your guess: 16
	Too Small
	
	Enter your guess: 24
	Too Large
	
	Enter your guess: 20
	You got it right! in 3 tries

	to generate random value use 
	
	from random import randint
	value=randint(lower,upper)
	
"""
from random import randint
from os import system


min_limit = 0
max_limit = 0
guessNumber = 0

def initGame():
    min_limit = int(input("Enter Lower limit: "))
    max_limit = int(input("Enter Upper limit: "))
    n = randint(min_limit, max_limit)
    gameLoop(n)

def gameLoop(guessNumber):
    tries = 0
    while True:
        guess = int(input("Enter your guess: "))
        tries+=1
        if guess == guessNumber:
            print("You guessed it right! %d number of tries" % (tries))
            return
        elif guess < guessNumber:
            print("Too small")
        else:
            print("Too large")
            

def main():
    system("cls")
    initGame()

if __name__ == "__main__":
    main()