def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    return a ** b

print("Calculator Module Loaded")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
user_input = input("Enter operation (+, -, * , / , **) or 'exit' to quit: ")
if user_input == 'exit':
    print("Exiting the calculator.")
elif user_input == '+':
    print("Result:", add(number1, number2))
elif user_input == '-':
    print("Result:", subtract(number1, number2))            
elif user_input == '*':
    print("Result:", multiply(number1, number2))
elif user_input == '/':
    print("Result:", divide(number1, number2))
elif user_input == '**':
    print("Result:", power(number1, number2))

else:
    print("Invalid operation Selected.")