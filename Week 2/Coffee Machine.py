# Drink class represents a type of coffee drink (like latte or espresso)
class Drink:
    def __init__(self, name: str, ingredients: dict, cost: float):
        # Set up the drink's name, what ingredients it needs, and how much it costs
        self.name = name
        self.ingredients = ingredients  # Dictionary: e.g. {'water': 100, 'milk': 50, 'coffee': 18}
        self.cost = cost

# Menu class holds a list of all available drinks
class Menu:
    def __init__(self):
        self.drinks = []  # Will hold multiple Drink objects

    def get_items(self):
        # Returns a string of available drink names to show the user
        return "/".join([drink.name for drink in self.drinks])

    def find_drink(self, drink_name):
        # Search the drinks list and return the matching Drink object
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink
        return None  # Return None if not found

# PaymentProcessor handles taking coins and checking if enough money was inserted
class PaymentProcessor:
    def __init__(self):
        # Each coin's value in dollars
        self.coins = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}

    def collect_coins(self):
        # Ask user to insert coins, and calculate total money inserted
        print("Please insert coins:")
        total = 0
        for coin, value in self.coins.items(): #self.coins is a dictionary and we are calling its items
            count = int(input(f"How many {coin}? "))
            total += count * value
        return round(total, 2)

    def is_transaction_successful(self, inserted_amount, drink_cost):
        # Check if inserted money is enough for the drink
        if inserted_amount < drink_cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif inserted_amount > drink_cost:
            change = round(inserted_amount - drink_cost, 2)
            print(f"Here is ${change} in change.")
        return True

# CoffeeMachine represents the machine that makes drinks and manages resources
class CoffeeMachine:
    def __init__(self):
        # Initialize the resources available in the machine
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
        self.money = 0.0  # Track money earned
        self.is_on = True  # Power state of the machine

    def report(self):
        # Print out the current levels of resources and money
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.money}")

    def is_resource_sufficient(self, drink):
        # Check if we have enough ingredients for the selected drink
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources.get(item, 0):
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink):
        # Deduct ingredients from resources and confirm to user
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        self.money += drink.cost  # Add the cost of the drink to machine's money
        print(f"Here is your {drink.name}. Enjoy!")

    def turn_off(self):
        # Shut down the machine
        self.is_on = False


# ----------- Main Program Execution -------------

# Create menu and add drinks
menu = Menu()
menu.drinks.append(Drink("espresso", {"water": 50, "coffee": 18}, 1.5))
menu.drinks.append(Drink("latte", {"water": 200, "milk": 150, "coffee": 24}, 2.5))
menu.drinks.append(Drink("cappuccino", {"water": 250, "milk": 100, "coffee": 24}, 3.0))

# Create the machine and payment handler
coffee_machine = CoffeeMachine()
payment_processor = PaymentProcessor()

# Main loop
while coffee_machine.is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == "off":
        coffee_machine.turn_off()  # Turn off the machine
    elif choice == "report":
        coffee_machine.report()    # Show current status
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_machine.is_resource_sufficient(drink):
                payment = payment_processor.collect_coins()
                if payment_processor.is_transaction_successful(payment, drink.cost):
                    coffee_machine.make_coffee(drink)
        else:
            print("Sorry, that drink is not on the menu.")