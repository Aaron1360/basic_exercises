"""9. **Prime Number Checker**: Implement a function to check if a number is prime.
"""
import os

print("**Prime Number Checker**")

is_prime = True

while True:
    os.system("clear")
    try:
        number = int(input("Enter a positive integer: "))
        if number <= 0:
            raise Exception
    except:
        print("Only positive integers allowed as input.")
    else:
        for i in range(2,number):
            mod = number%i
            if mod == 0:
                is_prime = False
                break
                
        print(f"{number} is prime") if is_prime else print(f"{number} is not prime.") 
        break
    