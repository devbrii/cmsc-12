# Punzalan, Kurt Brian Daine B.
# CMSC 12 - T4L

# function that adds key-value pairs in the dictionary
def add_record(records):
    product_number = input("Enter product number: ")
    if product_number in records:
        print("The product alredy exists.\n")
    else:
        per_product = {}

        records[product_number] = per_product

        brand = input("Input brand: ")
        records[product_number]["Brand: "] = brand

        product_type = input("Type of Product: ")
        records[product_number]["Type of Product: "] = product_type

        weight = input("Weight of Product: ")
        records[product_number]["Weight: "] = weight

        items = input("Number of Items in Stock: ")
        records[product_number]["No. of Items: "] = items

    return records


# function that views all details of a specific product
def view_record(records):
    x = 1
    if len(records) != 0:
        print("Pick a product number from the following.")
        print()
        for k in records:
            print("Product Number ", x, " : ", k)
            x += 1
        print()

        user = input("Choose a product number: ")
        print()
        if user in records.keys():
            print("-------------------------------------")
            print("(", user, ")", records[user]["Brand: "], records[user]["Type of Product: "],
                  records[user]["Weight: "], "(", records[user]["No. of Items: "], ") pcs")

            print("\nProduct Number: \t", end=" ")
            print(user)

            print("Brand: \t\t\t", end=" ")
            print(records[user]["Brand: "])

            print("Type of Product : \t", end=" ")
            print(records[user]["Type of Product: "])

            print("Weight : \t\t", end=" ")
            print(records[user]["Weight: "])

            print("No. of Items : \t\t", end=" ")
            print(records[user]["No. of Items: "], "pcs")
        else:
            print("Wrong input!\n")
    else:
        print("There are no items in the records yet.")


# function that views all records in the dictionary
def view_all(records):
    if len(records) != 0:
        print("All records in the shop: \n")
        for items in records:
            concatenated = records[items]["Brand: "] + " " + records[items]["Type of Product: "] + \
                " " + records[items]["Weight: "] + " " + \
                "(" + records[items]["No. of Items: "] + ") pcs"
            print("(", items, ") : ", concatenated)
    else:
        print("There are no items in the records yet.")


# function that deletes a specific records in the dictionary
def delete_record(records):
    x = 1
    if len(records) != 0:

        print("Pick a product number to delete.")

        for k in records:
            print("Product Number ", x, " : ", k)
            x += 1

        message = input("\nEnter the product number: ")
        if message in records:
            del records[message]
            print("\nThe product was deleted successfully.")
        else:
            print("Wrong input!")

    else:
        print("There are no records at this moment. Try adding a product first.")

    return records


# function that deletes all records
def delete_all(records):
    if len(records) != 0:
        records = {}
        print("All items were succesfully deleted.")
    else:
        print("The records are empty at this moment.")
        print("Try adding new products.")
    return records


# function that saves current file to records.txt
def save_file(records):
    if len(records) == 0:
        print("There are no saved files yet. \nTry adding a product first.")
    else:
        file_handle = open("records.txt", "w")
        for i in records:
            file_handle.write(i + "<#>" + records[i]["Brand: "] + "<#>" + records[i]["Type of Product: "] +
                              "<#>" + records[i]["Weight: "] + "<#>" + records[i]["No. of Items: "] + "\n")
        file_handle.close()
        print("The products were saved in the secondary memory.")
    return records


# function that loads records.txt file
def load_file(records):
    file_handle = open("records.txt", "r")
    records.clear()
    number_of_files = 0
    for line in file_handle:
        data = line[:-1].split("<#>")

        per_item = {}

        product_number = data[0]

        brand = data[1]
        per_item["Brand: "] = brand

        product_type = data[2]
        per_item["Type of Product: "] = product_type

        weight = data[3]
        per_item["Weight: "] = weight

        items = data[4]
        per_item["No. of Items: "] = items

        records[product_number] = per_item
        number_of_files += 1
    file_handle.close()
    print("Successfully loaded your file.")
    print(number_of_files, " product/s were loaded.")
    return records


# function for different options
def menu():
    print("-------------------------------------")
    print("[1] Add a product")
    print("[2] View a product")
    print("[3] View all products")
    print("[4] Delete a product")
    print("[5] Delete all products")
    print("[6] Save to file")
    print("[7] Load from file")
    print("[0] Exit")
    print("-------------------------------------")
    choice = int(input("What do you want to do? "))
    print("-------------------------------------")
    return choice


records = {}


# conditions
while True:
    choice = menu()
    if choice == 1:
        records = add_record(records)
    elif choice == 2:
        view_record(records)
    elif choice == 3:
        view_all(records)
    elif choice == 4:
        records = delete_record(records)
    elif choice == 5:
        records = delete_all(records)
    elif choice == 6:
        records = save_file(records)
    elif choice == 7:
        records = load_file(records)
    elif choice == 0:
        print('\nProgram Terminated')
        break
    else:
        print("Invalid choice. Try again.")
