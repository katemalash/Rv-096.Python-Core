year = int(input("Enter year to check: "))

if year %4 == 0:
    if year <= 100:
        print("1st century.")
    elif year %100 == 0:
        print(year // 100,"century")
    else:
        print(year // 100 + 1,"century")
else:
    print(year,"This year is not a intercalary year")