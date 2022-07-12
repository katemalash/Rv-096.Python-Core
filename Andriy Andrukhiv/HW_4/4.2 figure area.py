lock = 1
while lock:
    figure = (input('Hello, select your figure for definition area: \n Trinagle - t\n Circle - c\n Rectangle - r\n'))

    if figure == "t" or figure == "T":
        ab = float(input("Press first katet: "))
        bc = float(input("Press second katet: "))
        ac = (ab**2+bc**2)**0.5
        print (ac)

    elif figure == 'c' or figure == 'C':
        p = 3.14
        r = float(input("Press radius: "))
        area = p * r**2
        print (area)

    elif figure ==  'r' or figure == 'R':
        height = float(input("press height(m): "))
        width = float(input("press width(m): "))
        area = height*width
        print (area)

    else:
        print ('I can not treat with figure :c ')
    lock = int(input('Continue? 1 - yes , 0 - no:'))

print ('Bye c:')