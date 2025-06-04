import os

class Drink:
    def __init__(self, name: str, ingredients: dict, cost: float):
        self.name = name
        self.ingredients = ingredients
        self.cost = cost

class Menu:
    def __init__(self):
        self.drinks = []

    def get_items(self):
        return " / ".join([drink.name for drink in self.drinks])
    
    def find_drink(self, drink_name):
        for x in self.drinks:
            if x.name == drink_name:
                return Drink
        return None
    
class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water" : 500,
            "milk"  : 300,
            "coffee": 150
        }
        self.money = 0.0
        self.is_on = True

    def report(self):
        print(f"Water : {self.resources['water']}")
        print(f"Milk : {self.resources['milk']}")
        print(f"Coffee : {self.resource['coffee']}")
        print(f"Total money : {self.money}")

    def sufficient_resources(self,drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources.get(item,0):
                print(f"Insufficient quantity of {item}.")
                return False
        return True
    
    def make_coffee(self, drink):
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        self.money += drink.cost    
        print(f"Enjoy your {drink.name}.")

    def turn_off(self):
        self.is_on = False

class Accountant:
    def __init__(self):
        self.coins = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}

    def collect_coints(self):
        print("Please enter your coins: ")
        for x,y in self.coins:
            count = int(input(f"Enter the number of {y}: "))


menu = Menu()
menu.drinks.append(Drink("americano", {"water" : 50, "coffee" : 18, "milk" : 0}, 1.5))
menu.drinks.append(Drink("espresso", {"water": 30, "coffee": 25}, 1.5))
menu.drinks.append(Drink("latte", {"water": 200, "milk": 150, "coffee": 24}, 2.5))
menu.drinks.append(Drink("cappuccino", {"water": 250, "milk": 100, "coffee": 24}, 3.0))

coffee_machine = CoffeeMachine()
payments = accountant()