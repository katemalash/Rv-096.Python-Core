#The amount of money is known. Exchange it with 200, 100, 10 banknotes and 1 UAH coin, if possible
amount_of_money = int(input("Please, input the amount of money: "))
bancnotes_200=int(amount_of_money/200)
amount_of_money= amount_of_money-bancnotes_200*200
bancnotes_100=int(amount_of_money/100)
amount_of_money= amount_of_money-bancnotes_100*100
bancnotes_10=int(amount_of_money/10)
amount_of_money= amount_of_money-bancnotes_10*10
bancnotes_1=int(amount_of_money/1)
print ("200 uah:", bancnotes_200, "bancnotes, 100 uah:", bancnotes_100, \
    "bancnotes, 10 uah:", bancnotes_10, "bancnotes, 1 uah:", bancnotes_1, "coins")
