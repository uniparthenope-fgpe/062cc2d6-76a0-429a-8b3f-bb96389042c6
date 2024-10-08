def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'Error! Division by zero.'
    return a / b

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
operation = input('Choose operation (+, -, *, /): ')

if operation == '+':
    print(add(num1, num2))
elif operation == '-':
    print(subtract(num1, num2))
elif operation == '*':
    print(multiply(num1, num2))
elif operation == '/':
    print(divide(num1, num2))
else:
    print('Invalid operation')