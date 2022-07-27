'''Aleksieiev Valentyn
26/07/2022 HomeWork#8, Task#3
Create a date function that takes 3 arguments - day, month and year.
Return True if such a date is in our calendar, and False - otherwise
'''

import time


def calendar_validator(date):   
    try:
      valid_date = time.strptime(date, '%d/%m/%Y')
    except ValueError:
      return False
    return True
    
while True:   
    date = input('Date in this format (dd/mm/yyyy): ')
    print(calendar_validator(date))
    print('============CALCULATION FINISH============')
    if input('Press enter to calculate new arithmetic operation or "0" to exit: ') == '0': break
    
print('Thanks for testing my function calendar_validator! Have a nice day:)')