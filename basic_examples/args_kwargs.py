import functools
"""
The difference between *args and **kwargs:
"""

def summation(*args) -> int:
    sum:int = 0

    print(f"Type for args is: {type(args)}")

    for arg in args:
        sum += arg 
        print(f"Type for arg is: {type(arg)}")

    return sum

def names(**kwargs) -> None:
    
    print(f"Type for kwargs is: {type(kwargs)}")

    for key, value in kwargs.items():
        print(f"Key has type {type(key)}, value has type {type(value)}")
        print(f"My {key} is {value}")

if __name__ == "__main__":
    my_list = ["Apfel", "Banane", "Kiwi", "Wassermelone", "mango"]

    list1 = [2,3,4,5]
    list2 = [0.5, 0.5]
    value = functools.reduce(lambda a,b: a+b == 1, list2)
    print(value)   
