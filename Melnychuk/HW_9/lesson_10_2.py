salad = ['shallot', 'cucumber', 'cherry tomatoes', 'green olives', 'jarred sliced pepperoncini']
lasagna = ['meat sauce', 'lasagna noodles', 'mozzarella cheese', 'parmesan cheese', 'bechamel sauce']
vegetable_ragu = ['onion', 'celery sticks', 'carrots', 'garlic', 'tomatoes', 'courgettes','mushrooms']

def adding_lettuce(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("* lettuce\nBelieve me: it's tastier with lettuce.")
        return result
    return wrapper
 
@adding_lettuce
def output_dish_ingredients(dish):
    for item in dish:
        print('*', item)
    return f'So, those are all the ingredients.'
    
print(output_dish_ingredients(lasagna))

