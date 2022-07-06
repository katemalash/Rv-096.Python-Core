'''Aleksieiev Valentyn
04/07/2022 HomeWork#4, Task#5
The amount of money is known. Exchange it with 200, 100, 10 banknotes and 1 UAH coin, if possible
'''
from cheker import variable_check

dict_money = {200: 0, 100: 0, 10: 0, 1: 0}


def calc_money(money, m_dic):
   for key in m_dic:
        m_dic[key], money = (divmod(money, key))

money = variable_check(int, 1, 'Input money to calculates banknotes in')
if money < 0:
    print('Money can have only positive value in this task! The program convert your number in positiv number.')
    
calc_money(abs(money), dict_money)
print('Answer for this task:')

for key in dict_money:
    if dict_money[key] > 0:
        print(f'{key} banknotes needs: {dict_money[key]}')