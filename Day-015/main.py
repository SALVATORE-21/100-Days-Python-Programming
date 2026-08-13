"""
Coffee machine program that simulates a coffee machine.
The program allows users to select different types of coffee and process payments.
It also keeps track of the inventory and provides options for refilling ingredients.
The program is designed to be user-friendly and interactive, providing a realistic coffee machine experience.

"""
# Importing the menu module to access coffee options and their details
from menu import MENU, resources


def is_resource_sufficient(order_ingredients):
    """Checks if there are enough resources to make the selected coffee."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Processes the coins inserted by the user and returns the total amount."""
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction_successful(money_received, drink_cost):
    """Checks if the transaction is successful based on the money received and the cost of the drink."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is ${change} in change.")
        return True
    else:
        return False

def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources and makes the coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True
profit = 0
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        print("Turning off the coffee machine. Goodbye!")
        is_on = False
    elif user_choice == "report":
        print("Water:", resources["water"], "ml")
        print("Milk:", resources["milk"], "ml")
        print("Coffee:", resources["coffee"], "g")
        print("Money: $", profit)
    #Check if the resouces are sufficient to make the coffee
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            print(f"The cost of {user_choice} is ${drink['cost']}. Please insert coins.")
            # Process payment
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                # Deduct the required ingredients from the resources
                make_coffee(user_choice, drink["ingredients"])
            else:
                print("Sorry, that's not enough money. Money refunded.")





