from task05 import is_year_leap


def validation_date(day, month, year):
    """This function validation date and return 'True' or 'False'."""

    flag = False
    number_of_month = {1: 31, 2: 29 if is_year_leap(year) else 28, 3: 31, 4: 30, 5: 31, 6: 30,
                       7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if month in number_of_month.keys() and day in range(1, number_of_month[month] + 1) and year >= 1:
        flag = True

    return flag


date = [int(number) for number in (input('Enter date: ')).split('.')]

print(validation_date(date[0], date[1], date[2]))
