figure = input('Hello, select your figure for definition area: \n Trinagle - t\n Circle - c\n Rectangle - r\n')

if figure == 't' or 'T':
    ab = float(input("Press first katet: "))
    bc = float(input("Press second katet: "))
    ac = (ab**2+bc**2)**0.5
    print (ac)

elif figure == 'c' or 'C':
    p = 3.14
    r = float(input("Press radius: "))
    a = p * r**2
    print (a)

elif figure == 'r' or 'R':
    height = float(input("press height(m): "))
    width = float(input("press width(m): "))
    area = height*width
    print (area)
    

else:
    print ('I can not treat with figure :c ')

print ('Bye c:')