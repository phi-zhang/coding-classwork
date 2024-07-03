# Name: Phi Zhang
# This program converts a given integer from base 10 to base 2, 8, or 16.
# Written for COMPSCI 130.

def display_intro():
    print("**********************************************")
    print("**        A Number Converter Program        **")
    print("** Decimal --> Binary, Octal or Hexadecimal **")
    print("**********************************************")

def display_menu():
    print("1. Convert to binary value")
    print("2. Convert to octal value")
    print("3. Convert to hexadecimal value")
    print("4. Quit the program")

def get_selection(start, end):
    selection = input("Please make a selection: ")
    while not selection.isnumeric() or not start <= int(selection) <= end:
        selection = input("Invalid selection. Try again: ")
    return int(selection)

def get_number():
    number = input("Please enter a positive integer: ")
    while not number.isnumeric() or not int(number) > 0:
        number = input("Invalid entry. Try again: ")
    return int(number)

def convert_number(number, base):
    if number == 0:
        return ""
    else:
        remainder = (["a", "b", "c", "d", "e", "f"][number % base - 10]
                     if number % base >= 10
                     else number % base)
        return convert_number(number // base, base) + str(remainder)

def main():
    display_intro()
    display_menu()
    print()
    selection = get_selection(1, 4)
    while selection != 4:
        number = get_number()
        converted_number = convert_number(number, [2, 8, 16][selection - 1])
        base = ["binary", "octal", "hexadecimal"][selection - 1]
        print(f"{number} is {converted_number} in {base}")
        print()
        display_menu()
        print()
        selection = get_selection(1, 4)