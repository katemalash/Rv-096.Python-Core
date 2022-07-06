

def swap_numbers():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    first_number, second_number = second_number, first_number
    return print(f"Now, first number is {first_number}, 5second number is {second_number}")


swap_numbers()
