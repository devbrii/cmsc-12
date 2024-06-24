# Punzalan, Kurt Brian Daine B.
# CMSC 12 - T4L

# function for user input
def xy_input():
    x = int(input("x: "))
    y = int(input("y: "))
    return x, y


# function for addition
def addition(x, y):
    return x + y


# function for subtraction
def subtraction(x, y):
    return x - y


# function for multiplication
def multiplication(x, y):
    product = 0
    # multiplication using repeated addition
    for i in range(0, y):
        product = addition(product, x)
    return product


# function for division
def division(x, y):
    quotient = 0
    # division using repeated subtraction
    while x != 0:
        x = (subtraction(x, y))
        quotient += 1
        # calculates the quotient with remainder (if there's any)
        if x < 0:
            quotient -= 1
            while x <= 0:
                x += y
            remainder = x
            return str(quotient) + " remainder " + str(remainder)
    return quotient


# function for exponentiation
def exponentiation(x, y):
    result = 1
    # exponentiation using repeated mmultiplication
    for i in range(0, y):
        result = multiplication(result, x)
    return result


# function for menu
def menu():
    print()
    print("Addition                 [1]")
    print("Subtraction              [2]")
    print("Multiplication           [3]")
    print("Division                 [4]")
    print("Exponentiation           [5]")
    print("Terminate the program    [0]")
    print()
    print("-----------------------------")
    user_input = int(input("Desired number: "))
    return user_input


# conditions
while True:
    user_input = menu()
    if user_input == 1:
        print("-----------------------------")
        print("You've chosen addition.")
        print("-----------------------------")
        x, y = xy_input()
        print("x + y = ", addition(x, y))
    elif user_input == 2:
        print("-----------------------------")
        print("You've chosen subtraction.")
        print("-----------------------------")
        x, y = xy_input()
        print("x - y = ", subtraction(x, y))
    elif user_input == 3:
        print("-----------------------------")
        print("You've chosen multiplication.")
        print("-----------------------------")
        x, y = xy_input()
        print("x * y = ", multiplication(x, y))
    elif user_input == 4:
        print("-----------------------------")
        print("You've chosen division.")
        print("-----------------------------")
        x, y = xy_input()
        print("x / y = ", division(x, y))
    elif user_input == 5:
        print("-----------------------------")
        print("You've chosen exponentiation.")
        print("-----------------------------")
        x, y = xy_input()
        print("x ** y = ", exponentiation(x, y))
    elif user_input == 0:
        print("-----------------------------")
        print("Program terminated")
        print("-----------------------------")
        break
    else:
        print("-----------------------------")
        print("You've entered a wrong number!")
        print("Try again!")
    print("-----------------------------")
