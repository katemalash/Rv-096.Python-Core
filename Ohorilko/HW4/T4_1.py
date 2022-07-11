#The YEAR is known. Determine whether this year is intercalary and to what century this year belongs
# у високосному менше днів а потім визначаєм століття
#  
year = int(input("Please, input the year: "))
if year % 4 == 0 and year % 100 != 0:
    print("The inputed year is (or was or will be) a leap year")
elif year % 400 == 0:
    print("The inputed year is (or was or will be) a leap year")
else:
    print('''The inputed year isn't (or wasn't or won't be) a leap year''')

if year %100 == 0:
            century=year //100 
else:
            century=year //100 + 1
print("It is (or was or will be) ", century, " century")