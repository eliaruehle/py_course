# In Python gibt es einige fundamentale Datenstrukturen mit denen man arbeiten kann:

# 1.) Tupel
x:tuple = (1,2,3)
y:tuple = (1,2,3)

print("Ist x gleich y? " + str(x == y))

try: 
    x[0] = 1
except:
    print("Achtung! Tuples sind unveränderlich!")

# 2.) Listen 
a = [1,2,3]
b = list({1,2,3})

print("Ist a gleich b ?" + str(a == b))