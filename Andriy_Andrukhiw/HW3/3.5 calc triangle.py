import math

#aс - це гіпотенуза , оскільки частіше за все трикутник має три кути , які позначаються а, b , с то я вирішив використати такий же приклад , де аb - довший катет bc - коротший катет і ас - гіпотенуза!
ab = float(input("Press first katet: "))
bc = float(input("Press second katet: "))
ac = math.sqrt(ab**2+bc**2)
print (ac)