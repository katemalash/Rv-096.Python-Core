amount_of_money = int(input('How much money do you have?  '))
if amount_of_money < 0:
    print('Enter the number grater than 0.')
else:
    num_200 = amount_of_money // 200
    left_banknotes_200 = amount_of_money % 200

    num_100 = left_banknotes_200 // 100
    left_banknotes_100 = left_banknotes_200 % 100

    num_10 = left_banknotes_100 // 10
    left_banknotes_10 = left_banknotes_100 % 10

    print(f'You can use:\n{num_200} - 200 banknotes,\n{num_100} - 100 banknotes,\n{num_10} - 10 banknotes,\n{left_banknotes_10} - 1 uah coins.')
    
