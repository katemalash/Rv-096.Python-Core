"""digitals = list(map(int,input("Enter 10 natural digitals by space: ").split()))
print(digitals)
sum=0
for i in range(digitals[0],[10],1):
    if [i]%5==0:
        print [i]
        sum=sum+[i]
print(sum)
"""
first_try = 0
last_try = 10
sum =0
while first_try<last_try:
    attempt = int(input(f"Enter digital. You have {last_try-first_try} attempts: "))
    if attempt<=2:
        continue
    if attempt>2 and attempt%5==0:
        sum+=1
    #print(sum)
    first_try+=1
else:
    print(f"We find special digits a {sum} times.")