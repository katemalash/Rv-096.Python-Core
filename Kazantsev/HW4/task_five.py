
amount_of_money = int(input("What amount of money do you have?\n"))
two_hundred_banknotes = 0
one_hundred_banknotes = 0
tens_banknotes = 0
ones_banknotes = 0


if amount_of_money // 200 >= 1:
    two_hundred_banknotes = amount_of_money // 200
    amount_of_money = amount_of_money - amount_of_money//200 * 200
    print(amount_of_money)
if amount_of_money // 100 >= 1:
    one_hundred_banknotes = amount_of_money // 100
    amount_of_money = amount_of_money - amount_of_money // 100 * 100
    print(amount_of_money)
if amount_of_money // 10 >= 1:
    tens_banknotes = amount_of_money // 10
    amount_of_money = amount_of_money - amount_of_money // 10 * 10
    print(amount_of_money)
if amount_of_money // 1 >= 1:
    ones_banknotes = amount_of_money // 1
    amount_of_money = amount_of_money - amount_of_money // 1 * 1
    print(amount_of_money)

print(f'Now you have {two_hundred_banknotes} of two hundred hryvnia banknotes, {one_hundred_banknotes} of one hundred \
hryvnia banknotes, {tens_banknotes} of ten hryvnia banknotes and {ones_banknotes} of one hryvnia banknotes.')

