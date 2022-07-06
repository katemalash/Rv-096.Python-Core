money = int(input("Enter the amount of your money: "))

if money%200 == 0:
    print("200 : ", money//200, "Times ")
elif money//200 > 1:
    print("200 : ", money//200, "Times ")
else:
    print("Time")
if money%100 == 0:
    print("100 : ", money//100, "Times" if money//100 > 1 else "Time")
if money%10 == 0:
    print("10 : ", money//10, "Times" if money//10 > 1 else "Time")
if money%1 == 0:
    print("1 : ", money//1, "Times" if money//1 > 1 else "Time")
