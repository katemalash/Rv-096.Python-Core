# Create the function is_year_leap, that takes 1 argument - year, and returns 
# True if the year is high, and False otherwise. 


def cheking_leap(year):

    if year% 4 == 0 :
        leap="Yes"
    else :
        leap="No"
    return(leap) 

print(cheking_leap(1980))