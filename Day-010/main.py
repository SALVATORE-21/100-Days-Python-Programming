"""
Topics Covered
--------------
- Function with outputs

"""

calc = """

.-----------------------.
|  ●●●●  ●●●●  ●●●●     |   <-- Display
|-----------------------|
| ● 1 ● ● 2 ● ● 3 ●  +  |
| ● 4 ● ● 5 ● ● 6 ●  -  |
| ● 7 ● ● 8 ● ● 9 ●  ×  |
|     ● 0 ●     ● = ● ÷ |
'-----------------------'

"""
print("-----The calculator program-----")
print(calc)

"""
Necessary Function
"""

def add(n1,n2):
    return n1 + n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

def power(n1,n2):
    return n1**n2

def subtract(n1,n2):
    return n1 - n2


"""
Saing the mathematical operations under a dict

"""

operations = {
    "+":add,
    "*":multiply,
    "-":subtract,
    "**":power,
    "/":divide
}

def calculator():
    should_accumilate = True
    a = int(input("What is the first number: "))
    print("-" * 20)

    while should_accumilate:
        print("Choose among the 5 available operations")
        print(" '+' '*' '-' '/' '**' ")
        b = str(input("The choosen operation....: "))

        c = int(input("What is the second number: "))
        print("The final result is: ",(operations[b](n1=a,n2=c)))
        result = operations[b](n1=a,n2=c)

        choice = input(f"Type 'y' to continue calculating with the result `{result}` or type 'n' to exit: ").lower()

        if choice == "y":
            a = result
        else:
            should_accumilate = False
            print("xxxxxxxxxxxxxxxxxxxENDXXXXXXXXXXXXXXXXXXXXXX")


######################################################################
# - Calling the calculator
calculator()


