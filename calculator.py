def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

equation = input('Enter an operation (+, -, *, /): ')
x = float(input('Enter the first number here: '))
y = float(input('Enter the second number here: '))
if equation == '+':
    ans = add(x, y)
    print(ans)
elif equation == '-':
    ans = subtract(x, y)
    print(ans)
elif equation == '*':
    ans = multiply(x, y)
    print(ans)
elif equation == '/':
    ans = divide(x, y)
    print(ans)
else:
    print('Choose a valid operator.')
    exit()
