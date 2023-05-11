my_list = [3,5,7.89,3.2,4]

s = 0
for x in my_list:
    s = s + x

m = s/ len(my_list)

print(m)
print(round(m,0))

if round(m,0)%2 == 0 :
    print("Der Mittelwert ist gerade")
else: 
    print("Der Mittelwert ist ungerade")

rm = round(m,0)%2 


number = 3.141

match int(number)%2:
    case 0:
        print("Die Zahl ist gerade")
    case _ : 
        print("Die Zahl ist ungerade")
