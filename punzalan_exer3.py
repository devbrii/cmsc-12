desired_number = int(input("n = "))
i = 0
starting_number = 2
while i < desired_number:
    for number in range(2, starting_number):
        if starting_number % number == 0:
            desired_number += 1
            break
    else:
        print(starting_number, end=" ")
    starting_number += 1
    i += 1
