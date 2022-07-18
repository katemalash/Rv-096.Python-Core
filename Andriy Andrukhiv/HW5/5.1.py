from random import randint

t_r_y = iter(range(10,0,-1))
a = randint(0,100)
for i in range(10):
    b = int(input(f'Залилось '+str(next(t_r_y)) +' спроб!\nВгадай число: '))
    if a == b:
        print (f"Вітаю ти вгадав число, це було число "+str(a)+' !!!' )
        break
    elif a < b:
        print ("менше")
    elif a > b:
        print ("Більше")
    else:
        () 
print('Це було число '+str(a)+' !' )
        
