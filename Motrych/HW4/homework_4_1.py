year = int(input("Enter year "))

import math

if year % 100 == 0 :
    century = math.trunc(year/100)
else:    
    century = math.trunc(year/100)+1
if year % 4 == 0 :
    leap="Yes"
else :
    leap="No"   
print(f"Current year: {year} , Century: {century}, Leap: {leap}")