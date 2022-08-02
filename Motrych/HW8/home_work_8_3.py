# Create a date function that takes 3 arguments - day, month and year.
# Return True if such a date is in our calendar, and False - otherwise. 

def check_true_day(dd,mm,yy):
    

    if yy <= 0 or yy >= 3000:
        return False
    
    if mm <= 0 or mm >= 12:
        return False
    
    if mm == 2:
        if yy%4 == 0:   
           if dd <= 29:
               return True
           else: 
               return False      
        else:   
               if dd <= 28:
                   return True
               else:
                   return False      
    if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or  mm == 10 or  mm == 12:
        if dd <= 31:
            return True
        else:       
            return False                     
    if dd <= 30:
        return True
    else:       
        return False

    if mm == 2 or mm == 4 or mm == 6 or mm == 9 or mm == 11 :
        if dd <= 30:
            return True
        else:       
            return False

print(check_true_day(7,4,1970))


