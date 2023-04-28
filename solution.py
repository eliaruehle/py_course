from pprint import pprint
dict1 = dict()
set1 = set()
list1 = list()

dict1["SWT"] = "Aßmann"
dict1["Prog"] = "Fetzer"
dict1["Mathe"] = "Baumann"
dict1.update({"Ikt" : "Franz"})
dict1["hallo"] = "welt"
print(dict1["SWT"])

prof_list = ["Aßmann", "Goetz"]

dict1["SWT"] = prof_list

pprint(dict1)

print(dict1.items())
print("Keys: " + str(dict1.keys()))
print("Values: " + str(dict1.values()))

print("Keys: ", dict1.keys())
print(dict1.values(), dict1.keys())