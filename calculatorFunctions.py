def numberInp():
    first_number = input("\nFirst number: ")
    second_number = input("Second number: ")
    try:
        int(first_number)
    except ValueError:
        try:
            float(first_number)
        except ValueError:
            print("Input 1 must be an integer.")
    try:
        int(second_number)
    except ValueError:
        try:
            float(second_number)
        except ValueError:
            print("Input 2 must be an integer.")
    return first_number, second_number


def multiply():
    first_number, second_number = numberInp()
    try:
        answer = int(first_number) * int(second_number)
        print(f"\n{answer} is the product.")
    except ValueError:
        print("Inputs must all be integers.")


def subtract():
    first_number, second_number = numberInp()
    try:
        answer = int(first_number) - int(second_number)
        print(f"{answer} is the difference.")
    except ValueError:
        print("Inputs must all be integers.")


def add():
    first_number, second_number = numberInp()
    try:
        answer = int(first_number) + int(second_number)
        print(f"{answer} is the sum.")
    except ValueError:
        print("Inputs must all be integers.")


def divide():
    first_number, second_number = numberInp()
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0.")
    else:
        print(f"{answer} is the quotient.")
