positive_qty=0
negative_qty=0 
count=0
digit=1
while not digit == 0:
    digit=int(input("Enter integer number "))
    if digit < 0:
        negative_qty+=1
    elif digit > 0:
        positive_qty+=1
    count+=1
print(f"Share of negative digits is {negative_qty*100/(count-1)}% ")
print(f"Share of positive digits is {positive_qty*100/(count-1)}% ")   
