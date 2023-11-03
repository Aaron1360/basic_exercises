"""11. **Palindrome Detector**: Build a program that checks if a given sentence is a palindrome, considering spaces and punctuation.
"""
def check_sentence(palindrome):
    no_spaces = palindrome.replace(" ","")
    temp = list(no_spaces)
    temp.reverse()
    test = "".join(temp)
    
    if no_spaces == test:
        print(f"{palindrome} is a palindrome")
    else:
        print(f"{palindrome} is not a palindrome")

print("**Palindrome Detector**")
sentence = input("Enter a sentence: ")
check_sentence(sentence)