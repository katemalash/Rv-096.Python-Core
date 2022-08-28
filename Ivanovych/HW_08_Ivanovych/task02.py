def deposit(money, years, percent):
     """This function calculates compound interest"""

     while years != 0:
        money += round(money * (percent / 100), 2)
        years -= 1

        return round(money, 2)


money = int(input('Enter makes a deposit : '))
years = int(input('Enter years : '))
percent = int(input('Enter percent : '))
income = deposit(money, years, percent)

print(f'\nResult: {income}')
