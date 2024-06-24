# Punzalan, Kurt Brian Daine B.
# CMSC 12 - T4-L


# function for user input
def input_xy():
    x = int(input("x: "))
    y = int(input("y: "))
    return x, y


# function for recursive multiplication
def recursive_multiplication(y):
    if y == 0:
        return 0
    return x + recursive_multiplication(y - 1)


# function for recursive division
def recursive_division(x):
    if x == 0:
        return 0
    return 1 + (recursive_division(x - y))


# menu function
def menu():
    print("-----------------------------")
    print("[1] Multiplication")
    print("[2] Division")
    print("[0] Terminate the program\n")
    choice = int(input("Desired number: "))
    print("-----------------------------")
    return choice


# condition
while True:
    choice = menu()
    if choice == 1:
        x, y = input_xy()
        print("x * y = ", recursive_multiplication(y))
    elif choice == 2:
        x, y = input_xy()
        print("x / y = ", recursive_division(x))
    elif choice == 0:
        print("Program Terminated")
        break
    else:
        print("Wrong input. Try again.")
