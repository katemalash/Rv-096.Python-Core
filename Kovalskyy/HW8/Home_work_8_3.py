# Create a date function that takes 3 arguments - day, month and year.
# Return True if such a date is in our calendar, and False - otherwise. 

def date(year,month,day):
    if year >0:
        if month == 2:
            if day in range(1,29):
                return True
            else:
                return False
        elif month ==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            if day in range(1,32):
                return True
            else:
                return False
        elif month==4 or month==6 or month==9 or month==11:
            if day in range(1,31):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

year = int(input("Input a year: "))
month = int(input("Input a month: "))
day = int(input("Input a day: "))
print(date(year,month,day))
