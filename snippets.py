
a = 3
b = 2.7
c = 3 + 5j

#Strings
string_A = "hello"
string_B = "world"
string_C = string_A + string_B
print(string_C)

string_euler = "Die Eulersche Zahl beträgt etwa {}"
print(string_euler.format(b))
print(string_euler)

#Konvertierungen
a = 3
b = 2.7
c = 3 + 5j

x = float(a)
y = int(b)
z = complex(a)

print(x)
print(type(x))

print(y)
print(type(y))

print(z)
print(type(z))


bool_a = True
bool(string_A)  #True
bool("")        #False