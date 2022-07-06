
year = int (input ("Пожалуйста, введите год: "))
if year % 4 == 0 and year % 100 != 0:
         print ("Високосный год")
elif year % 400 == 0:
         print ("Високосный год")
else:
         print ("Не високосный год")
if (year % 100 > 0):
   century = year // 100 + 1
else:
   century = year // 100;
print("Этот год относится к", century, "-му столетию")
