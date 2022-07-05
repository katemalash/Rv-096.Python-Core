money_amount = int(input("Enter amount of money: "))

def count_amount(money_amount):
    money = [200, 100, 10, 1]
    money_count = {}

    for uah in money:
        if money_amount >= uah:
            money_count[uah] = money_amount // uah
            money_amount %= uah

    print("Exchange amount of money is:")
    for key, val in money_count.items():
        print(f"{key} : {val}")

print(count_amount(money_amount))
