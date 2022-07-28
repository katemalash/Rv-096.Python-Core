'''Aleksieiev Valentyn
28/07/2022 HomeWork#8, Task#1
Suppose you are a cook and you have a lot of lettuce so you’ve decided to add it to all the dishes.
Create a few collections that contain the ingredients of dish;
create function that outputs the ingredients of each dish. Create decorator that adds lettuce to all the dishes.
'''
dict_coll = {'Salat Cezar': ('Green salad', 'Chicken', 'Tomato', 'Parmesan cheese', 'Garlic', 'White bread', 'Butter', 'Salt'),
             'Gamburger': ('Sesame buns', 'Mushrooms', 'Cream cheese', 'Clove of garlic', 'Boiled chicken breast', 'Olive oil'),
             'Sendwitch': ('Bread', 'Ham', 'Cheese', 'Cucumber', 'Tomato', 'Mayonnaise', 'Butter')}

def add_lettuce(func):
    """Декоратор, добавляющий латук к выводу коллекции"""
    def wrapper(collect_, *args):
        print('Collection before decorate:')
        func(collect_, *args)  # print original function for test
        print('=============DECORATING FUNCTIONS STARTS=============')
        collect_ += ('Lettuce', )  # add to the end of tuple 'Lettuce'
        print('Collection after decorate:')
        return func(collect_, *args)  # return function value with modified parameters
    return wrapper

@add_lettuce
def print_collec(collect, col_name):
    print(f'Collection {col_name}:')
    [print(f'{i+1}. {item}', end=' ') for i, item in enumerate(collect)]
    print()

for key, value in dict_coll.items():
    print_collec(value, key)
    input('Press enter to add lettuce next collection')
    print('\n=============NEXT COLLECTION=============\n')

print("The original dictionary has not changed after decorating! Tuples is immutable type:)")
for key in dict_coll:
    print(f'Collection {key}:')
    [print(f'{i + 1}. {item}', end=' ') for i, item in enumerate(dict_coll[key])]
    print('\n====================================================')