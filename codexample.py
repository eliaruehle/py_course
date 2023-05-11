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
    print(summation(1,2,3,4,5))
    print(summation(1,2,3))
    print(summation(1))

    print(names(name="Uwe", number=81258537, home="Dresden"))

if __name__ == "__main__":
    main()

