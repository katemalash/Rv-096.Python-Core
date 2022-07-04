'''Aleksieiev Valentyn
30/07/2022 HomeWork#3, Task#6
1. Suppose that you are a philatelist. You have three collections of marks. The first one contains marks dedicated to cats,
the second one holds cars and the third one has elephants. You can exchange by your collections with another philatelists,
but only entire collections (for example, change cars on bicycles), but not the single marks. 
Also you want to have short description of each collection.
Please suggest the most appropriate way of saving information about collections, marks they consist of and their descriptions.
2. Suppose you have equal marks in collection  with cats and you want to hold information only about unique ones.
How would you save this information?

1) We should to create a dictionary from the required categories = ('bikes', 'cars', 'cats', 'elephants', 'dogs')
Dictionary key - it's a category name
Dictionary values - dictionary of the next character:
'Items' = set of the unique collections
'Info' - description of the collection

Advantage of this storage method: linear speed of access and query processing to any category by key,
also a fast and convenient property of sets - adding new elements with clipping of repetitions when
we trying to add an already existing element to the set.
'''

from cheker import variable_check

col_marks1 = {'Bikes': {'Items': {'Yamaha MT-06', 'Suzuki vStrom'},
                        'Info': 'Unique collection of motorcycles from the 2020 series'},
              'Cars': {'Items': {'Audi Q7', 'BMW X5', 'Audi TT', 'Lexus R450h'},
                       'Info': 'Unique Collection of cars from the 2021 series'},
             'Cats': {'Items': {'Persian', 'Siamese', 'Scottish'},
                      'Info': 'Unique collection of popular cat breeds in illustrations'},
             'Elephants': {'Items': {'White', 'Indian', 'Mamont'},
                           'Info': 'Unique collection of elephants in nature'}}

col_marks2 = {'Bikes': {'Items': {'Yamaha MT-06', 'Kawasaki Er6N', 'BMW S1000-RS'},
                        'Info': 'Unique collection of motorcycles from the 2020 series'},
             'Cats': {'Items': {'Persian', 'Scottish'},
                      'Info': 'Unique collection of popular cat breeds in illustrations'},
             'Elephants': {'Items': {'White'},
                           'Info': 'Unique collection of elephants in nature'},
             'Dogs': {'Items': {'Labrador, Buldog, Spaniel, Pudel'},
                           'Info': 'Unique collection of dogs'}}

def change_all_category(collect1, collect2, cat_name1, cat_name2):
    if collect1.get(cat_name1) and collect2.get(cat_name2):
        coll_1 = collect1.pop(cat_name1)
        coll_2 = collect2.pop(cat_name2)
    else:
        print('No such category in collections try again :)')
        return False

    if collect1.get(cat_name2):
        collect1[cat_name2]['Items'] |= coll_2['Items']
    else:
        collect1[cat_name2] = coll_2
    if collect2.get(cat_name1):
        collect2[cat_name1]['Items'] |= coll_1['Items']
    else:
        collect2[cat_name1] = coll_1
    return True

def print_dic(colect, name):
    print(f'\033[1m{name}:\033[0m',*[f'\033[32m{item}\033[0m {colect[item]}' for item in colect], sep='\n')


print_dic(col_marks1, name='col_marks1')
print_dic(col_marks2, name='col_marks2')

flag = True

while flag:
    name1, name2 = variable_check(str, 2, 'Input category to change or 2 times Enter to exit')
    if not name1 or not name2:
        break
    if name1.title() in col_marks1 and name2.title() in col_marks2:
        print(f'\nAll category \033[1m{name1} from col_marks1 add to col_marks2 {name1}\033[0m and category\
\033[1m {name2}\033[0m from 2 sent in full to 1 collection\n')

        change_all_category(col_marks1, col_marks2, name1.title(), name2.title())
        print_dic(col_marks1, name='col_marks1')
        print_dic(col_marks2, name='col_marks2')
    else:
        print('enter the correct categories names')
    

