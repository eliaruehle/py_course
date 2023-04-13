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
e = str(1.2)
print(type(c))
print(type(d))
print(type(e))

# Typisierung, aber Achtung!
f:int = 1
g:float = 2.3
print(type(f))
print(type(g))

h:int = 2.3
print(type(h))