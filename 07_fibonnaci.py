"""7. **Fibonacci Sequence**: Create a function to generate the Fibonacci sequence up to a specified number.
"""
import os
# recursion
def fibbonacci(n):
    if n in {0,1}:
        return n
    return fibbonacci(n-1) + fibbonacci(n-2)

# solution #1
# def fibbonacci(n):
#     sequence = [0, 1]
#     while len(sequence) < n:
#         next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
#         sequence.append(next_value)
#     return sequence

def main():
    while True:
        os.system("clear")
        print("**Fibonacci Sequence**")
        try:
            number = int(input("Enter a positive integer: "))
            if number <= 0:
                raise Exception
        except:
            print("Only positive numbers allowed as input.")
            input("Press enter to continue.")
            continue
        else:
            print(f"First {number} members of the Fibbonacci sequence:")
            
            # solution #1
            # print(fibbonacci(number))
            
            # recursion
            sequence = [fibbonacci(n) for n in range(number)]
            print(sequence)
            
            break

if __name__ == "__main__":
    main()