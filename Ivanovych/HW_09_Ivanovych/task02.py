def salad(func):

    def add_salad(*args, **kwargs):
        func(*args, **kwargs)
        print('salad')

    return add_salad


@salad
def print_recipe(recipe=str):
    try:

        recipe = recipe.split(', ')

    except AttributeError:
        print('This is not recipe')

    for ingredient in recipe:
        print(ingredient)


sandwich = 'potato, tomato, cucumber, bun, sauce, cutlet'
soup = 'potato, cabbage, beet, meat'

print_recipe(soup)
