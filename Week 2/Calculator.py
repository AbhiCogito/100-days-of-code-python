import os 
os.system("clear")
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
    
def work(reuse, output):
    print ("Choose an operator: \n \
           1. Add       = 1 or + or add \n \
           2. Substract = 2 or - or substract \n \
           3. Multiple  = 3 or * or multiply \n \
           4. Divide    = 4 or / or divide \n")
    
    operation = input("Enter your selection: ")
    if reuse.lower() == 'n':
        first_number = float(input("Enter the first number: ").strip())
    else:
        first_number = output
    second_number = float(input("Enter the second number: ").strip())
    result = calculator(first_number, second_number, operation)
    print(f"{first_number} {operation} {second_number} = {result}")
    reuse = input("Do you want to reuse the number for further operations (y or n): ")
    if reuse.lower() == 'y':
        print("The previous result is ", result)
    return reuse, result

print("The Calculator App \n")
reuse = 'n'
result = 0

while reuse_number:
    reuse, result = work(reuse, result)
    if reuse.lower() == 'n':
        reuse_number = False