ammount = int(input("Enter ammount "))

import math

n200=math.trunc(ammount/200)

a=ammount % 200
n100=math.trunc(a/100)
b=a % 100
n10=math.trunc(b/10)
c=b % 10 

print(f"Ammount can be split by {n200} 200-banknotes,{n100} 100-banknotes, {n10} 10-banknotes,{c} 15161-banknotes")
