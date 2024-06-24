x = int(input("Enter a Number: "))
y = int(input("Enter a Number: "))
z = int(input("Enter a Number: "))

if (x % 2 > 0) and (x >= y or y % 2 == 0) and (x >= z or z % 2 == 0):
    print("The greatest odd number is ", x)
elif (y % 2 > 0) and (y >= x or x % 2 == 0) and (y >= z or z % 2 == 0):
    print("The greatest odd number is ", y)
elif (z % 2 > 0) and (z >= x or x % 2 == 0) and (z >= y or y % 2 == 0):
    print("The greatest odd number is ", z)
else:
    print("There is no odd number given.")
