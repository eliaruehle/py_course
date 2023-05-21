import functools
import random
from typing import Any, List
import math

#### Sortierung ####

def sort_by_length(s : str) -> int:
    return len(s)

def sort_by_last_letter(s : str) -> str:
    return s[-1]

def sort_by_middle_letter(s : str) -> str:
    # note: // is rounded division (round downwards)
    return s[(len(s)-1) // 2]

def sort_by_hash(s : str) -> int:
    # attention: output differs on every machine and every call, since hash() uses random seeds
    return hash(s)

def sort_by_second_tuple(t : tuple) -> int:
    return t[1]

### Lambda Funktionen

def all_lambda():
    int_list = [22,51,6,21,17,43]

    # square root:
    sq_roots = list(map(lambda x: math.sqrt(x), int_list))
    print(sq_roots)

    # 3rd power:
    powers = list(map(lambda x: x**3, int_list))
    print(powers)

    # double increment
    increments = list(map(lambda x: x + (2*x), int_list))
    print(increments)

    # subtract sum
    sub_sums = list(map(lambda x: x - sum(int(digit) for digit in str(x)), int_list))
    print(sub_sums)

### Functools Funktionen 

def reduce_for_sum(numbers : List) -> float:
    return functools.reduce(lambda a,b: a+b, numbers)


def filter_values() -> List:
    values = [random.randint(1,50) for _ in range(10)]
    print(values)
    # for odd: lambda x: x%2 != 0
    return list(filter(lambda x: x%2 == 0, values))


if __name__ == "__main__":
    # define first list 
    my_list = ["Apfel", "Birne", "Melone", "Kiwi", "Salat", "Ananas", "Mango", "Papaya"]
    # define second list
    my_list2 = [(1,2), (2,4), (6,3), (1,7), (7,1), (8,2)]
    # call sort key functions as neccessary
    my_list.sort(key=sort_by_hash)
    my_list2.sort(key=sort_by_second_tuple)
    # print lists after sorting
    print(my_list)
    print(my_list2)

    # calculates all the lambda expressions
    all_lambda()

    numbers = [1.3, 3, 5.77, 12, 14.7]
    print(reduce_for_sum(numbers))

    # call the filter function
    print(filter_values())