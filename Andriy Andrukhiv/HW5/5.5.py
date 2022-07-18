from random import randint
p = 5
h = 8
c = 1
suma = 0
numbersBetwhen = 0
multipickation = 1
myList = []
while c:
    x = int(input ('Введіть число від 1 до 10: '))
    myList.append(x)
    if x == p or x == h:
        break
    else:
        ()
    
for item in myList:
    if item < p:
        suma+=item
    elif item > h:
        multipickation*=item
    elif p < item < h or h < item < p:
        numbersBetwhen+=1
    else:
        ()
print ('p='+str(p)+' h='+str(h))
print ('Сума всіх чисел менших за р: '+str(suma)+'.\nДобуток всіх чисел більших за h: '+str(multipickation)+'.\nКількість чисел які знаходились між p і h: '+str(numbersBetwhen)+'.')


