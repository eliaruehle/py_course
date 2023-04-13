# Es gibt in Python fundamentale Kontrollstrukturen:

# 1. for-loop 
for i in range(4):
    print(i)

# 2. while-loop
a:int = 3
b:int = 0
while( b < a ):     # while b<a: auch möglich, Klammern optional
    print(b)
    b = b+1 
    # schöner und kürzer: b+=1

# 3. if-statement
c:int = 3
if c == 3:
    print("Hurra")
elif c == 2:
    print("OHOH")
else:
    print("Verrückt!")

# 4. match statement (seit Python 3.10)
name:str = "Uwe"

match name:
    case "Heiko":
        print("Algortithmen und Datenstrukturen")
    case "Franz":
        print("Formale Systeme")
    case "Uwe":
        print("Softwaretechnologie")
    case _ :
        print("Anwesend")


### Aufgaben: ###

'''
1. Definiert euch zwei Variablen vom Typ 'float' und belegt sie mit beliebigen Werten. 
   Prüft dann ob beide Variablen denselben Wert haben. Wenn ja soll "gleich" ausgegeben werden,
   wenn nein, dann "ungleich.
'''
# write your code here


'''
2. Wir wollen 5 mal hintereinander das Wort "Informatik" ausgeben. Dabei soll jedes mal zusätzlich
   ausgegeben werden, das wie vielte "Informatik" gerade ausgegeben wird. 
   Hinweis: Mit print(arg1, arg2) kann zwei Variablen gleichzeitig ausgeben.
'''
# write your code here


'''
3. In einer Schleife sollen alle Zahlenwerte von 0 bis 9 durchlaufen werden. Ist eine Zahl gerade, 
   so soll "gerade" ausgegeben werden, andernfalls ungerade. 
   Hinweis: In Python bezeichnet % den modulo Operator, z.B. ist 4 % 2 = 0
'''
# write your code here