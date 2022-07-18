b = iter(range(1,11,1))
for i in range(10):
    d = int(input(f"Введіть "+str(next(b))+'-e число: '))
    if  d%5==0 :
        print('ДІЛИТЬСЯ на 5')
    else:
        print('НЕ ділиться на 5')