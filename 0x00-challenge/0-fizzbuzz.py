#!/usr/bin/python3

# This script implements the FizzBuzz problem.
# For numbers from 1 to n, it prints:
# - "Fizz" if the number is divisible by 3
# - "Buzz" if the number is divisible by 5
# - "FizzBuzz" if the number is divisible by both 3 and 5
# - The number itself if it is not divisible by 3 or 5.

def fizzbuzz(n):
    """
    Prints the FizzBuzz sequence from 1 to n.
    Args:
        n (int): The upper limit of the FizzBuzz sequence.
    """
    for i in range(1, n + 1):
        # Check if the number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        # Check if the number is divisible by 3
        elif i % 3 == 0:
            print("Fizz", end=" ")
        # Check if the number is divisible by 5
        elif i % 5 == 0:
            print("Buzz", end=" ")
        # If none of the above, print the number itself
        else:
            print(i, end=" ")

# Entry point of the script
if __name__ == "__main__":
    # Run the fizzbuzz function with the upper limit 50
    fizzbuzz(50)
