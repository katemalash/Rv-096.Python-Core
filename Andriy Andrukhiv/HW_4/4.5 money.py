def exchange(money,x,bal ):
    if money // x:
        bal.append(1)
        exchange(money-x,x,bal)
    return f'{sum(bal)} купюри по {x}',money-(sum(bal*x))
 
sum_money = int(input('Введіть вашу суму: '))
if sum_money >= 500:
    result, sum_money = exchange(sum_money,500,[])
    print(result)
if sum_money >=200:
    result,sum_money  = exchange(sum_money ,200,[])
    print(result)
if sum_money >=100:
    result,sum_money  = exchange(sum_money ,100,[])
    print(result)
if sum_money >= 50:
    result,sum_money  = exchange(sum_money ,50,[])
    print(result)
if sum_money >= 20:
    result,sum_money  = exchange(sum_money ,20,[])
    print(result)
if sum_money >= 10:
    result,sum_money  = exchange(sum_money ,10,[])
    print(result)
if sum_money > 5:
    result,sum_money  = exchange(sum_money ,5,[])
    print(result)
if sum_money > 2:
    result,sum_money  = exchange(sum_money ,2,[])
    print(result)
if sum_money >= 1:
    result,sum_money  = exchange(sum_money ,1,[])
    print(result)
