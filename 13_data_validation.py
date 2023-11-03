"""13. **Data Validation**: Write a script to validate user input, ensuring it meets certain criteria, like email address format.
"""
import re

def validate(usr_input):
    x = re.fullmatch("^[\w\.]+@[\w]+\.[\w]+",usr_input)
    if x:
        print(f"{usr_input} is a valid email.")
    else:
        print(f"{usr_input} is not a valid email.")
    
email = input("Enter email: ")
validate(email)