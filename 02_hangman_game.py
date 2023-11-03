"""2. **Hangman Game**: Implement a text-based Hangman game where the user can guess words.
ORIGINAL CODE: https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py"""

import os
import random

words = ["python", "terminal", "script", "programming", "automation", "code", "functions", "system", "project"]

def get_word():
    word = random.choice(words)
    return word.upper()

def play(word):
    os.system("clear")
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 4
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion,"\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        os.system("clear")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job",guess,"is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word",guess)
            elif guess != word:
                print(guess,"is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
            
        print(display_hangman(tries))
        print(word_completion,"\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ", maybe next time!")


def display_hangman(tries):
    stages = [  
            """
            --------
            |      |
            |      O
            |     /|\\ 
            |      |
            |     / \\
            -
            """,
            """
            --------
            |      |
            |      O
            |     /|\\
            |      |
            |     / 
            -
            """,
            """
            --------
            |      |
            |      O
            |     /|\\
            |      |
            |      
            -
            """,
            """
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
            """,
            """
            --------
            |      |
            |      
            |    
            |      
            |     
            -
            """]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)
    
if __name__ == "__main__":
    main()