"""6. **String Manipulation**: Write a program that reverses a string and checks if it's a palindrome (reads the same forwards and backward).
"""
print("**String Manipulation**")

# User input
word = input("Enter a word: ")

# Convert the word to a list and save it in the opposite order
word_list = list(word)
word_list.reverse()
reverse_word = "".join(word_list)
print(word, reverse_word)

# check if its a palindrome
if word == reverse_word:
    print(word, " is a palindrome.")
else:
    print(word, " is not a palindrome.")