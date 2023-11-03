"""1. **Calculator Program**: Create a command-line calculator that can perform basic arithmetic operations."""
import os
import time

DELAY = 2

def clean_error():
    print("Try again.")
    time.sleep(DELAY)
    os.system("clear")
    
# Operations

def add(numbers):
    result = sum(numbers)
    return result

def subtract(numbers):
    result = numbers[0] - sum(numbers[1:])
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    if 0 in numbers[1:]:
        return "Error: Division by zero."
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

# Menu and main loop

menu = """
**Calculator Program**
Options:
Enter 'add' for addition.
Enter 'sub' for subtraction.
Enter 'mul' for multiplication.
Enter 'div' for division.
Enter 'quit' to end the program.
"""

while True:
    os.system("clear")
    print(menu)
    user_input = input(": ")
    
    if user_input == "quit":
        break
    
    elif user_input in ("add","sub","mul","div"):
        try:
            num_list = [float(x) for x in input("Enter numbers separated by space:").split()]
        except Exception as error:
            print("***Error***")
            clean_error()
            continue
        
        if not num_list:
            print("Please enter at least one number.")
            clean_error()
            continue
        
        match user_input:
            case "add":
                print("Result: ",add(num_list))
            
            case "sub":
                print("Result: ",subtract(num_list))

            case "mul":
                print("Result: ",multiply(num_list))
            
            case "div":
                print("Result: ",divide(num_list))
        
        input("Press Enter to continue...")
        
    else:
        print("Invalid input.")
        clean_error()