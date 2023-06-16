
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def __str__(self) -> str:
        return self.name

    
    def __del__(self):
        del self.age
        del self.height
        del self.name

    def __eq__(self, other):
        return self.name == other.name


if __name__ == '__main__':
    my_class = Person('John', 25, 180)
    print(my_class.name)
    print(my_class.age)
    print(my_class.height)

    del my_class
    # prin(my_class) -> NameError: name 'my_class' is not defined