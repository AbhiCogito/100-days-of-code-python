import os 
os.system("clear")

first_number = float(input("Enter the first number: "))
reuse_number = True

def calculator(first_number, second_number, operation):
    if operation in ("+", "1", "add"):
        return first_number + second_number
    elif operation in ("-", "2", "substract"):
        return first_number - second_number
    elif operation in ("*", "3", "multiply"):
        return first_number * second_number
    elif operation in ("/", "4", "divide"):
        return first_number / second_number
    
print("The Calculator App \n")
if reuse_number == False:
    first_number = float(input("Enter the first number: "))
else:
    print ("Choose an operator: \n 1. Add = 1 or + or add \n 2. Substract = 2 or - or substract \n 3. Multiple = 3 or * or multiply \n 4. Divide = 4 or / or divide \n")
    operation = input("Enter your selection: ")
    second_number = float(input("Enter the second number: "))
    result = calculator(first_number, second_number, operation)
    print(f"{first_number} {operation} {second_number} = {result}")