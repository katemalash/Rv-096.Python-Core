import random

p = random.randint(0, 100)
h = random.randint(0, 100)
print(p, h)

user_data = []
user_num = None
while user_num not in {p, h}:
    user_num = int(input('Enter the number: '))
    user_data.append(user_num)

sum = 0
for i in user_data:
    if i < p:
        sum += i
print (f'The sum of numbers that are less than p={p} is {sum}.')

mult = 1
filtered = list(filter(lambda score: score > h, user_data))
#print(filtered)
if not filtered:
    mult = 0
else:
    for i in filtered:
        mult = i * mult
print (f'The product of numbers grater than h={h} is {mult}.')

count = 0
for i in user_data:
    if i in range(p+1, h) or i in range(h+1, p):
    #if p < i < h or p > i > h :
        count +=1
print (f'The number of numbers in range of values: {p} and {h}  is {count}.')
