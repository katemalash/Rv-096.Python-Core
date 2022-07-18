'''entered_list = input("Введите список чисел, разделенных пробелом: ").split()
num_list = list(map(int, entered_list))'''
a = int(input("Enter 1 number: "))
b = int(input("Enter 2 number: "))
c = int(input("Enter 3 number: "))
d = int(input("Enter 4 number: "))
e = int(input("Enter 5 number: "))

n = 0
m = 1
i = 0
for i in range(a,b,c,d,e):
    if (a,b,c,d,e) > 0 :
        n += 1
    if (a,b,c,d,e) < 0 :
        m += 1
    if (a,b,c,d,e) == 0 :
        break
        print("Процент положительных чисел: " + str(100 / len(num_list) * n))
        print("Процент отрицательных чисел: " + str(100 / len(num_list) * m))
