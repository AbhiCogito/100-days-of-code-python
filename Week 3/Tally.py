import os
from datetime import datetime

class FinanceManager:

    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, income):
        self.incomes.append(income)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def income_report(self):
        for income in self.incomes:
            print(income.date, income.income_category, income.amount)

    def expense_report(self):
        for expense in self.expenses:
            print(expense.date, expense.expense_category, expense.expense_amount)

    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income.amount
        return total

    def total_expenses(self):
        total = 0
        for income in self.expenses:
            total += income.expense_amount
        return total

    def total_income_by_category(self):
        income_by_category = {
            "Salary" : 0, 
            "Rent" : 0, 
            "Dividend" : 0
            }    
        
        for income in self.incomes:
            income_by_category[income.income_category] += income.amount
        
        return income_by_category
    
    def total_expense_by_category(self):
        expense_by_category = {
            "Rent" : 0,
            "Utilities" : 0,
            "Food" : 0,
            "Travel" : 0,
            "Insurance" : 0,
            "Splurge" : 0
            }
    
        for expense in self.expenses:
            expense_by_category[expense.expense_category] += expense.expense_amount

        return expense_by_category

    def get_balance(self):
        return self.total_income() - self.total_expenses()
    

class Income:
    
    valid_income_categories = ["Salary", "Rent", "Dividend"]

    def __init__(self, date, income_category, amount):

        if income_category not in Income.valid_income_categories:
            raise ValueError(f"Invalid income category. Select from {Income.valid_income_categories} only.")

        self.date = date
        self.amount = amount
        self.income_category = income_category


class Expense:

    expense_categories = ["Rent", "Utilities", "Food", "Travel", "Insurance", "Splurge"]

    def __init__(self, date, expense_category, expense_amount):
        
        if expense_category not in Expense.expense_categories:
            raise ValueError(f"Invalid expense category. Select from {Expense.expense_categories} only.")
        
        self.date = date
        self.expense_category = expense_category
        self.expense_amount = expense_amount

class Budget:
    def __init__(self, user_budget, financemanager):
        self.budget = user_budget
        self.fm = financemanager

    def check_limit(self):
        total_income = self.fm.total_income()
        threshold = 0.33 * total_income

        actual_expenses = self.fm.total_expense_by_category()

        for category, amount in actual_expenses.items():
            if amount > threshold:
                print(f"{category} expense of {amount} is more than 33% of total income {total_income}.")

    def set_limit(self):
        total_income = self.fm.total_income()
        threshold = 0.33 * total_income

        actual_expenses = self.fm.total_expense_by_category()
        user_limits = {}

        for category, _ in actual_expenses.items():
            user_limits[category] = int(input(f"Enter the limit for {category} where max amount can be {threshold}: "))

        self.budget = user_limits

    def compare_expense_with_budget(self):

        expense_category_wise = self.fm.total_expense_by_category()

        for category, amount in expense_category_wise.items():
            if category in self.budget:
                if amount >= self.budget[category]:
                    print(f"Amount spent in {category} is more than the budgeted limit of {self.budget[category]}")
            else:
                print(f"No budget set for the {category}.")

# Main Loop

fm = FinanceManager()
budget = None
os.system("clear")

while True:
    try:
        choice = int(input(
            "\nWelcome to your Personal Finance Manager. Please select from the following options:\n"
            "1. Add Income\n"
            "2. Add Expense\n"
            "3. Get Income Report\n"
            "4. Get Expense Report\n"
            "5. Show Balance\n"
            "6. Set Budget\n"
            "7. Compare Expenses with Budget\n"
            "8. Exit\n"
            "Enter your choice (1-8): "
        ))

        if choice == 1:
            income_category = input("Please enter the input category - Salary, Rent, Dividend : ")
            amount = int(input("Please enter the amount: "))
            
            current_date = datetime.now()
            formatted_date = current_date.strftime("%B %Y")
            date = formatted_date

            income = Income(date, income_category, amount)
            fm.add_income(income)

        elif choice == 2:
            expense_category = input("Please enter the input category - Rent, Utilities, Food, Travel, Insurance, Splurge : ")
            amount = int(input("Please enter the amount: "))
            
            current_date = datetime.now()
            formatted_date = current_date.strftime("%B %Y")
            date = formatted_date

            expense = Expense(date, expense_category, amount)
            fm.add_expense(expense)

        elif choice == 3:
            fm.income_report()
            print(fm.total_income_by_category())

        elif choice == 4:
            fm.expense_report()
            print(fm.total_expense_by_category())

        elif choice == 5:
            print(fm.get_balance())

        elif choice == 6:
            user_budget = {}
            for category in fm.total_expense_by_category().keys():
                limit = int(input(f"Enter your budget for {category}: "))
                user_budget[category] = limit
            budget = Budget(user_budget, fm)
            print("Budget has been set.")

        elif choice == 7:

            if budget:
                budget.compare_expense_with_budget()
            else:
                print("Please set the budget first (Option 6).")

        elif choice == 8:
            exit()

        if choice < 1 or choice > 8:
            print("Invalid choice. PLease enter a number between 1-8. \n")
            continue

    except ValueError:
        print("Invalid input.")

    






