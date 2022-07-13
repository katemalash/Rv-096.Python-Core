
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for numbers in numbers_tuple:
    for number in range(1, 11):
        print(numbers, 'x', number, '=', numbers * number)
    print("")
