# sum  of two lists by their elements

from random import randint


list_len=int(input("Enter lenth of lists "))
list1=[randint(1,100)]
for i in range(list_len-1):
    list1.append(randint(1,100))

list2=[int(input("Enter first number "))]
for j in range(list_len-1):
    list2.append(int(input("Enter next number ")))

list3=[x+y for x,y in zip(list1,list2)]    

print(f"Random   list is {list1}")
print(f"Customer list is {list2}")
print(f"Total    list is {list3}")
