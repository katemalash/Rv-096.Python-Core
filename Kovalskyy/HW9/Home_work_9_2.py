# Suppose you are a cook and you have a lot of lettuce so you’ve decided to add it to all the dishes. 
# Create a few collections that contain the ingredients of dish; 
# create function that outputs the ingredients of each dish. 
# Create decorator that adds lettuce to all the dishes.

menu = {"Big_Mac":{"Bun", "Patty", "Sauce", "Cheese", "Pickle", "Onions"},
        "Cheeseburger":{"Bun", "Patty", "Ketchup", "Cheese", "Pickle", "Onions", "Mustard"},
        "Chicken_Sandwich":{"Bun", "Chicken", "Mayonnaise", "Tomato", "Lettuce"},
        }

def add_lettuce(func):
    def wrapper(*args,**kwargs):
        print('Collection before decorate:')
        func(*args,**kwargs)
        menu = args[0]
        for val in menu.values():
            val.add("Lettuce")
            
        print('Collection after decorate:')
        return func(menu) 
    return wrapper

@add_lettuce
def show_ing(ingr):
    print("The ingrediants of each dish are:")
    [print(f"{key} : {val}") for key, val in ingr.items()]

show_ing(menu)
