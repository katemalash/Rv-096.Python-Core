
p = 15
h = 27

user_numbers = []
numbers_pool = 10
numbers_sum = 0
numbers_product = 1

while numbers_pool > 0:
    print(f"Numbers left to enter: {numbers_pool}")
    number = input("Please, enter your number: ")
    if number.isdigit():
        number = int(number)
        if number < 0:
            print("Your natural number must be positive!")
            continue
        elif number != p and number != h:
            user_numbers.append(number)
            numbers_pool -= 1
            continue
        else:
            user_numbers.append(number)
            break

    else:
        print("Please, enter a natural number!")
        continue

for numbers in user_numbers:
    if numbers < p:
        numbers_sum += numbers
    elif numbers > h:
        numbers_product *= numbers

print(f"Your numbers summary is {numbers_sum}.\nYour numbers product is {numbers_product}")
