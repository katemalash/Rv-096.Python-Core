'''Aleksieiev Valentyn
26/07/2022 HomeWork#8, Task#2
The user makes a deposit of n dollars for year at 10% per annum (each year the amount of his deposit increases by 10%.
This money is added to the deposit amount, and next year there will also be interest on it).
Create a bank function that takes the arguments n and years and returns the amount that will be in the user's account.
'''
from cheker import variable_check


def bank_function(dep, years=1, per=10):
    '''function can calculate amount for
deposit = int > 0
years = int > 0 (1 year as default)
percents = float > 0 < 100 (10% as default)'''
    if dep<0 or years < 0 or 0>per>100:
        print(f"Can't calc this deposit = {dep}, year = {years}, % = {per}")
        return None
    sum_ = 0
    for i in range(years):
        dep += round(dep*per/100, 2)
        print(f'{i+1} year {per}% per annum: deposit = {dep:.2f}')
    return dep
    
    
while True:
    
    deposit, year = variable_check(int, 2, 'Input deposit(#1) & years(#2) to calc value')
    print(f'{deposit} for {year} and 10% per annum = {bank_function(deposit, year):.2f}')
    print('==========================================')    
    print(f'Calc for 12.5% per annum = {bank_function(deposit, year, 12.5):.2f}')

    print('============CALCULATION FINISH============\n')
    if input('Press enter to calculate new deposit or "0" to exit: ') == '0': break
    
print('Thanks for testing my function bank_function! Have a nice day:)')