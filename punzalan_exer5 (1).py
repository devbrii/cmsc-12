# Punzalan, Kurt Brian Daine B.
# CMSC 12 - T4L

# function that converts words into pig latin
def isPigLatin(word):
    vowel = "aeiou"
    new_word = []
    word.split()
    # splits the user input into different words
    for element in word.split():
        # converts words that starts with vowels into pig latin
        if element[0] in vowel:
            new = element[:] + "ay"
            new_word.append(new)
        # converts words that starts with consonants into pig latin
        else:
            while element[0] not in vowel:
                element = element[1:] + element[0]
            element += "ay"
            new_word.append(element)
    return new_word


def menu():
    print("-------------------------")
    print("[1] Pig Latin")
    print("[0] Terminate the Program")
    print()
    choice = int(input("Choice: "))
    print("-------------------------")
    return choice


while True:
    choice = menu()
    if choice == 1:
        word = input("Type word/s: ")
        print("-------------------------")
        print("Result: ", isPigLatin(word))
    elif choice == 0:
        print("Program Terminated")
        break
    else:
        print("Invalid choice!")
