def add(x, y):
    return x + y


def subtracting(x, y):
    return x - y


def multiply(x, y):
    return x * y


def square(x, y):
    return x ** y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "На 0 делить нельзя"

print("Hello, it's Calculator!")