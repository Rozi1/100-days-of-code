from calc_art import logo
print(logo)

# Addition Function
def add(a, b):
    return a + b

# Subtraction Function
def subtract(a, b):
    return a - b

# Multiplication Function
def multiply(a, b):
    return a * b

# Division Function
def divide(a, b):
    if b!= 0:
        return a / b
    else:
        raise ZeroDivisionError("Cannot divide by zero.")
    
# Power Function 
def power(a, b):
    return a**b
# Calculator Function -- Main Logic
def caclulator():
    first_number = float(input("What's the first Number?: "))
    while True:
        print("+\n-\n*\n/")
        char = input("Pick an Operation: ")
        second_number = float(input("What's the next Number?: "))
        result = 0
    
        if char == '+':
            result = add(first_number, second_number)
            print(f"{first_number} + {second_number} = {result}")
        elif char == '-':
            result = subtract(first_number, second_number)
            print(f"{first_number} - {second_number} = {result}")

        elif char == '*':
            result = multiply(first_number, second_number)
            print(f"{first_number} x {second_number} = {result}")
        elif char == '/':
            result = divide(first_number, second_number)
            print(f"{first_number} / {second_number} = {result}")
        else:
            print("An Invalid Operation Selected!!!")
        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or 'q' to Quit: ").lower()
        if should_continue == 'n':
            caclulator()
        elif should_continue == 'y':
            first_number = result
            continue
        elif should_continue == 'q':
            break

caclulator()