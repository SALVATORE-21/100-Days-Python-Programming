from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#Method report() is called to print the current resources and money available in the coffee machine.
coffee_maker.report()
money_machine.report()

is_on = True
while is_on:
    options = menu.get_items() #This line of code calls the get_items() method of the menu object, which is an instance of the Menu class. The method returns a string containing the names of all available menu items, separated by slashes ("/"). This string is stored in the variable options.
    choice = input(f"What would you like? ({options}): ") #This line prompts the user to input their choice of drink from the available options. The input is stored in the variable choice.
    if choice == "off": #This line checks if the user's input is "off". If it is, the program will set is_on to False, which will exit the while loop and turn off the coffee machine.
        is_on = False
    elif choice == "report": #This line checks if the user's input is "report". If it is, the program will call the report() methods of both coffee_maker and money_machine to print the current resources and money available in the coffee machine.
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice) #This line calls the find_drink() method of the menu object, passing in the user's choice as an argument. The method searches for a MenuItem with a matching name and returns it if found. The returned MenuItem object is stored in the variable drink.
        print(drink) #This line prints the drink object to the console. If a valid drink was found, it will display the MenuItem object; otherwise, it will print None.a
        if drink: #This line checks if a valid drink was found (i.e., drink is not None).
            if coffee_maker.is_resource_sufficient(drink): #This line calls the is_resource_sufficient() method of coffee_maker, passing in the drink object. It checks if there are enough resources to make the selected drink. If there are sufficient resources, it returns True; otherwise, it returns False.
                if money_machine.make_payment(drink.cost): #If there are sufficient resources, this line calls the make_payment() method of money_machine, passing in the cost of the selected drink. It processes the payment and returns True if successful; otherwise, it returns False.
                    coffee_maker.make_coffee(drink) #If payment was successful, this line calls the make_coffee() method of coffee_maker, passing in the drink object. It deducts the required resources and prepares the selected drink.