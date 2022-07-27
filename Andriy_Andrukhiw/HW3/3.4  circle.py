p = 3.14
r = float(input("Press radius: "))
action = input("Find area or perimeter? (a - p): ") 

a = p * r**2
per = 2*p*r 

#p - число Пі
#a - площа кола
#r - радіус кола
#per - периметр кола

if action == "a":
    print (a)
elif action == "p":
    print (per)
else:
    print("not entered correctly")
