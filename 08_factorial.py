"""8. **Factorial Calculator**: Write a function to calculate the factorial of a given number.
"""
import os

# recursion
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print("**Factorial Calculator**")

while True:
    os.system("clear")
    try:
        number = int(input("Enter a positive integer: "))
        if number <= 0:
            raise Exception
    except:
        print("Only positive numbers allowed as input.")
        input("Press enter to continue.")
    else:
        # solution 1
        # print(f"Factorial({number}) = {math.factorial(number)}")
        
        # recursion
        print(factorial(number))
        break
    
# solution 1
# import os
# import math

# print("**Factorial Calculator**")

# while True:
#     os.system("clear")
#     try:
#         number = int(input("Enter a positive integer: "))
#         if number <= 0:
#             raise Exception
#     except:
#         print("Only positive numbers allowed as input.")
#         input("Press enter to continue.")
#     else:
#         print(f"Factorial({number}) = {math.factorial(number)}")
#         break