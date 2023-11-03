"""12. **Anagram Finder**: Create a program that checks if two words are anagrams of each other.
"""
def anagram_finder(word1,word2):
    if len(word1) == len(word2):
        temp = list(word1)
        temp2 = list(word2)
        for i in temp:
            if i in temp2:
                temp2.remove(i)
        if temp2 == []:
            print(f"{word1} is an anagram of {word2}.")
        else:
            print(f"{word1} is not an anagram of {word2}.")
    else:
        print(f"{word1} and {word2} are not of the same lenght.")
    
print("**Anagram Finder**")
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
anagram_finder(word1,word2)