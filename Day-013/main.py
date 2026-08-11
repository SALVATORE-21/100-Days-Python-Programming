"""
Sample debugging example.
This program shows how to find and handle errors using:
- print statements
- try and except blocks
- simple debugging methods
"""


def divide_numbers():
    print("Starting the division program...")

    try:
        first_number = input("Enter the first number: ")
        second_number = input("Enter the second number: ")

        print(f"User entered first number: {first_number}")
        print(f"User entered second number: {second_number}")

        first = int(first_number)
        second = int(second_number)

        print("Both values were converted to integers successfully.")
        print(f"Now dividing {first} by {second}")

        result = first / second
        print(f"Result: {result}")

    except ValueError as error:
        print("Error: Please enter only numeric values.")
        print(f"Details: {error}")

    except ZeroDivisionError as error:
        print("Error: The second number cannot be zero.")
        print(f"Details: {error}")

    except Exception as error:
        print("Unexpected error occurred.")
        print(f"Details: {error}")

    finally:
        print("Program finished running.")


# Debugging methods used in this example:
# 1. Print statements help us see the values at each step.
# 2. Try and except blocks help us catch errors safely.
# 3. Reading the error message helps us understand the problem.
# 4. Testing with valid and invalid inputs helps confirm the fix.

divide_numbers()

