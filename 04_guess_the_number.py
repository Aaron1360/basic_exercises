"""4. **Guess the Number**: Develop a number guessing game where the computer generates a random number, and the user needs to guess it."""
import os
import random

def get_num():
    number = random.choice(range(0,10))
    return number

def play(number):
    os.system("clear")
    hidden_num = "_"
    guessed = False
    tries = 3
    print("**Guess the Number**")
    print("Range: 0-6: ",hidden_num)
    while not guessed and tries > 0:
        try:
            guess = int(input("Please guess a number: "))
        except Exception as error:
            print(error,"\n")
            continue
        
        if guess < 0 or guess > 6:
            print("Number out of range. Try again.\n")
        elif guess != number:
            print(guess," is not the number. Try again\n")
            tries -= 1
        else:
            print(guess," is correct, you win!\n")
            guessed = True

def main():
    number = get_num()
    play(number)
    while input("Play Again? (Y/N) ").upper() == "Y":
        number = get_num()
        play(number)
    
if __name__ == "__main__":
    main()
        