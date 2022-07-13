# First intercalary year is 4
year = int(input("Enter year: "))
century = int(year/100) +1
if year%4 ==0:
    for i in range(4,year+1,4):
        if i == year:
            print(f"Your year {year} is intercalary. It belong to, {century}' century.")
else: print(" Year is NOT intercalary!")
    
   
