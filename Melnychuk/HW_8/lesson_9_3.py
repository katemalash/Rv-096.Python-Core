def year_check(year):
    if 1 <= year <= 3000: return True
    else: return False
    
def is_year_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else: return False  
      
def month_check(month):
    if 1 <= month <= 12: return True
    else: return False

def day_check(year, month, day):
    if month <= 7 and month % 2 == 1:
       max_day = 31
    elif month <= 7 and month % 2 == 0 and month != 2:
       max_day = 30
    elif month >= 8 and month % 2 == 1:
       max_day = 30
    elif month >= 8 and month % 2 == 0:
       max_day = 31
    elif month == 2:
        if is_year_leap(year):
            max_day = 29
        else: max_day = 28
    #print(max_day)   
    if 1 <= day <= max_day:
        return True
    else: return False
 
   
def date_check(year, month, day):
#    print(year_check(year))
#    print(month_check(month))
#    print(day_check(year, month, day))
   
   if not year_check(year):
       return False
   elif not month_check(month):
       return False
   elif not day_check(year, month, day):
       return False
   else: return True
    
       
        
print(date_check(1808, 2, 29))
 