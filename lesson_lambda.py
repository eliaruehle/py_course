import math
from functools import reduce
import random

integers = [2, 23, 12, 3, 5, 17, 29]

# Aufgabe 1:
sqrts = list(map(lambda x: math.sqrt(x), integers))
print(sqrts)

# Aufgabe 2
threes = list(map(lambda x: x**3, integers))
print(threes) 

# Aufgabe 3
increment = list(map(lambda x: x + 2*x, integers))
print(increment)

# Aufgabe 4
quers = list(map(lambda x: x - sum([int(digit) for digit in str(x)]), integers))
print(quers)

# Aufgabe 5
reduced = reduce(lambda a, b: a+b, integers)
print(reduced)

my_list = [random.randint(1, 150) for _ in range(10)]
print("list", my_list)
even = list(filter(lambda x: x%2 == 0, my_list))
odd = list(filter(lambda x: x%2 != 0, my_list))

print("even", even)
print("odd", odd)