
def date(day,month,year):
    if 1<=day<=31 and 1<=month<=12:
        if month ==4 or month==6 or month==9 or month==11:
            day<=30
            return True
        elif month==2:
            day<=29
            return True
         #(f"{day}.{month}.{year})
    else: return False
print(date(30,2,2020))