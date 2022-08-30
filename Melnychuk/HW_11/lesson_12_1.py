import calculator


print(calculator.sum(2, 4))
print(calculator.dif(2, 4))
print(calculator.product(2, 4))
print(calculator.fraction(2, 4))

from calculator import fraction, product


print(fraction(7, 21))
print(product(2, 4))

from calculator import *


print(sum(2, 4))
print(dif(2, 4))
print(product(2, 4))
print(fraction(5, 15))