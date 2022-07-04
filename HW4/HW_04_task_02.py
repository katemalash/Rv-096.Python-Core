'''Aleksieiev Valentyn
04/07/2022 HomeWork#4, Task#2
Depending on the user's choice, calculate the square of ​​either a rectangle, or a triangle, or a circle.
If a rectangle or triangle is selected, the lengths of the sides should be invited; is circle, its radius.
'''
from cheker import variable_check

area_rect = lambda a, b: a * b
area_circle = lambda r: r * r * 3.14
def area_triangl(a, b, c):
    p = (a + b + c)/2
    return round((p * (p - a) * (p - b) * (p - c))**0.5, 2)

rules = ('rectangle', 'circle', 'triangle')
for num, item in enumerate(rules):
    print(f'{num + 1}. To calculate square of {item} input {num + 1}')

choice_ = variable_check(int, 1, 'Input your choice in')

if choice_ == 1:
    a, b = variable_check(int, 2, 'Input 2 sides of rectangle in')
    print('The square of your rectangle:', area_rect(a, b))
elif choice_ == 2:
    r = variable_check(int, 1, 'Input the radius of the circle in')
    print('The square of your rectangle:', area_circle(r))
elif choice_ == 3:
    a, b, c = variable_check(int, 3, 'Input 3 sides of triangle in')
    print('The square of your rectangle:', area_triangl(a, b, c))
else:
    print('You input somthing wrong! :(')
    

    