# Coffee Machine

A Python command-line simulation of a coffee vending machine that serves drinks, tracks ingredient resources, and processes coin payments.

## How to Play

1. Run the program with Python:
   ```bash
   python main.py
   ```
2. When prompted, type the name of a drink (`latte`, `espresso`, or `cappuccino`).
3. Insert coins (quarters, dimes, nickles, pennies) when asked to pay for the drink.
4. Type `report` to see the current water, milk, and coffee resources along with total profit.
5. Type `off` to turn the machine off and exit the program.

## Objective

Simulate a real coffee machine: manage limited ingredient resources, accept coin payments, give correct change, and keep track of profit.

## Project Files

- `main.py` – Runs the main program loop, handles user input, and coordinates the menu, coffee maker, and money machine.
- `menu.py` – Defines `MenuItem` and `Menu` classes that store the available drinks, their ingredients, and cost.
- `coffee_maker.py` – Defines the `CoffeeMaker` class, which tracks resources, checks if there are enough ingredients, and makes coffee.
- `money_machine.py` – Defines the `MoneyMachine` class, which processes coins, validates payment, and gives change.

## Requirements

- Python 3.x

## Example Flow

```text
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
What would you like? (latte/espresso/cappuccino/): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```

## Notes

This project is a beginner-friendly exercise in object-oriented Python that demonstrates:

- classes and objects
- separating concerns across multiple files/modules
- dictionaries for tracking resources and ingredients
- conditional logic and loops
- input handling
