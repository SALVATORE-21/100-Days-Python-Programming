print("Welcome to Python Pizza devlivery!!")
size = input("Choose the size of the pizza: S,M or L: ")
Total_bill = 0

if size == "S":
    print("You need to pay $15")
    Total_bill += 15
elif size == "M":
    print("You need to pay $20")
    Total_bill += 20
elif size == "L":
    print("You need to pay $25")
    Total_bill += 25
else:
    print("You have provided a wronge input")

pepperoni = input("Do you want pepperoni on your pizza: Y or N: ")
if pepperoni == "Y":
    print("+3$ adds into your bill")
    Total_bill += 3

extra_chesse = input("Do you want extra cheese? Y or N: ")
if extra_chesse == "Y":
    print("For extra cheese you will be added with extra $1")
    Total_bill += 1

print(f"Hence forth the final bill is......${Total_bill}")