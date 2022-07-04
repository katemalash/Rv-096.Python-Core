'''Aleksieiev Valentyn
30/07/2022 HomeWork#3, Task#7
Please suggest your option of situation where different data types are used for saving the information
(describe situation like in previous task).

Например есть Обычная Средняя Школа
Всего в школе 12 лет обучения, на каждый поток (год) обучения возможно от 1 до 4 классов
В каждом классе от 15 до 30 учеников.
Также каждый класс проходит обязательные предметы, у каждого потока свои предметы от 5 до 10 наименований.
Директор ставит задачу учителю информатики:
1) Создать базу данных на все потоки/классы/учеников таким образом чтобы он мог делать сравнение среднего
балла любого класса по любому предмету с любым другим классом того же потока.

Для решения такой задачи можно использовать несколько вариантов решения.
Например, на каждый поток создать отдельный список из словарей следующего характера:
lst_classes= [{'10-A': {'Ivanov I.N.': {'Math': [5,4,3,5], 'Geography': [4,5,4]...},
                         'Petrov M.N.': {'Math': [5,4,3,5], 'Geography': [4,5,4]...}}
               {'10-B': {'Sidorov N.P.': {'Math': [5,4,3,5], 'Geography': [4,3,4]...}]
                         'Aleksieiev V.V.': {'Math': [5,5,5,5], 'Geography': [4,4,4]...)}}]

Доступ к кажому классу возможен по ключу: lst_classes['10-A']
Доступ к каждому ченику класса: lst_classes['10-A']['Petrov M.N.']
Средний бал каждого ученика по предмету 'Math':
    sum(lst_classes['10-A']['Petrov M.N.']['Math'])/len(lst_classes['10-A']['Petrov M.N.']['Math'])
Средний бал класса по предмету:
avg_ball_class_curse(class_name, curse_name)

Средний бал класса по всем предметам:
avg_ball_class(class_name):

'''

lst_classes= {'10-A': {'Ivanov I.N.': {'Math': [5,5,3,5,5], 'Geography': [4,5,4,2]},
                        'Petrov M.N.': {'Math': [5,4,3,5], 'Geography': [4,5,4]}},
               '10-B': {'Sidorov N.P.': {'Math': [5,4,3,5], 'Geography': [4,3,4]},
                         'Aleksieiev V.V.': {'Math': [5,5,5,5], 'Geography': [4,4,4]},
                        'Yevtushenko K.P.': {'Math': [2,3,2,3], 'Geography': [3,3,4]},}
               }

def avg_ball_class_curse(class_name, curse_name):
    res_avg = []
    for childrens in lst_classes[class_name]:
        res_avg += [sum(lst_classes[class_name][childrens][curse_name]) / len(lst_classes[class_name][childrens][curse_name])]
    return round(sum(res_avg) / len(res_avg), 2)

def avg_ball_class(class_name):
    res_avg = []
    for childrens in lst_classes[class_name]:
        for curses in lst_classes[class_name][childrens]:
            res_avg += [sum(lst_classes[class_name][childrens][curses]) / len(lst_classes[class_name][childrens][curses])]
    return round(sum(res_avg) / len(res_avg), 2)


print('\033[1mAll classes dictionary:')
[print(f'\033[1m{clas_num}\033[0m: {lst_classes[clas_num]}') for clas_num in lst_classes]

print(f'\nAvg ball in 10-A of course Math = {avg_ball_class_curse("10-A", "Math")}')
print(f'Avg ball in 10-B of course Math = {avg_ball_class_curse("10-B", "Math")}')
print(f'Avg ball in 10-B of all curses = {avg_ball_class("10-B")}')
print(f'Avg ball in 10-A of all curses = {avg_ball_class("10-A")}')