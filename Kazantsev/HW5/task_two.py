
user_numbers = []
print("Please, enter 10 natural numbers.\n")
numbers_pool = 10

while len(user_numbers) < 11:
    print(f"Numbers left to enter: {numbers_pool}")
    number = input("Enter your natural number, which is bigger than 2: ")
    if number.isdigit():
        number = int(number)
        if number < 0:
            print("Your natural number must be positive!")
            continue
        elif number == 2:
            print("Your natural number should not be equal 2!")
            continue
        else:
            user_numbers.append(number)
            numbers_pool -= 1
    else:
        print("Please, enter a natural number that's bigger than 2!")
        continue

multiples_of_five = 0
for numbers in user_numbers:
    if numbers % 5 == 0:
        multiples_of_five += 1
    else:
        continue

print(f"{multiples_of_five} out of 10 numbers, that you've entered, multiples of five.")
