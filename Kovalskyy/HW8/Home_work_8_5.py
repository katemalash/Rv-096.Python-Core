# Create the function is_year_leap, that takes 1 argument - year, 
# and returns True if the year is high, and False otherwise. 

def is_year_leap(year):
    if year %4 ==0:
        return True
    else:
        return False

year = int(input("Input a year: "))
print(is_year_leap(year))
