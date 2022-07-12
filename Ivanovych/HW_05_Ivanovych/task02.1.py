entered_list = input("Введите список чисел, разделенных пробелом: ").split()
num_list = list(map(int, entered_list))
#print("Список чисел: ", num_list)
i = 0
for i in (num_list):
    if i % 5 == 0 :
        print("Numbers are multiples of 5:")
        print(i)
