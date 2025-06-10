from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

os.system("clear")

display = Menu()
coffee = CoffeeMaker()
account = MoneyMachine()
is_on = True


while is_on:
    print("Welcome to Starbucks!!")
    print(f"We have the following items: {display.get_items()}")
    choice = input("Please enter your selected drink: ").lower()
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        account.report()
    else:
        drink = display.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and account.make_payment(drink.cost):
            coffee.make_coffee(drink)


