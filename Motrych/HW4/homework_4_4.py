K = float(input("Enter K-distanse from wall to stage "))
radius = float(input("Enter radius of stage:  "))
square = float(input("Enter hall square:  "))

from math import pi
from math import sqrt

if 2*radius+K >= sqrt(square):
    print ("Can't set  stage here")
else:
    print("Stage can be placed") 