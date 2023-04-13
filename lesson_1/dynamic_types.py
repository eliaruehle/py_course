# Wertzuweisung von a und b
# Interpreter schließt auf deren Typ
a = 3
b = 3.4

# Ausgabe der Typen von a und b
print(type(a))
print(type(b))

# a wird zu Text
a = "Hello"
print(type(a))

# Typ einer Variable festlegen
c = str("3.1415926")
d = 3.1415926
print(type(c))
print(type(d))

def add(x: int, y: int) -> int:
    return x+y

print(add(2.3, 1.2))
