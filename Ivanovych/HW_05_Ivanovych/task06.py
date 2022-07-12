entered_list = input("Введите список чисел, разделенных пробелом: ").split()
num_list = list(map(int, entered_list))

n = 0
m = 0
for i in range(num_list):
    if num_list > 0 :
        n += 1
    if num_list < 0 :
        m += 1
    if num_list == 0 :
        break
        print("Процент положиьельных чисел: " + str(100 / len(num_list) * n))
        print("Процент положиьельных чисел: " + str(100 / len(num_list) * m))
