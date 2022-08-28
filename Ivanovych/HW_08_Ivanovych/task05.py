def is_year_leap(year):
    """This function checks if the year is a leap year."""

    result = True if (year % 4 == 0 and year % 100 != 0 and year > 0) \
                     or (year % 4 == 0 and year % 400 == 0 and year > 0) else False
    return result


year_of_user = int(input('Enter year: '))

print(is_year_leap(year_of_user))
