sum_of_positiv=0
sum_of_negativ=0
count = 0
digit=1
while not digit==0:
    digit = int(input("Enter positiv or negativ digit: "))
    if digit<0:
        sum_of_negativ+=1
    elif digit>0:
        sum_of_positiv+=1
    count+=1
#print(count-1,sum_of_negativ,sum_of_positiv)
print(f"Persent of negativ digits is {sum_of_negativ/(count-1)*100} %.")
print(f"Persent of positiv digits is {sum_of_positiv/(count-1)*100} %.")



