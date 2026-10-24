d1 = {
    'name':'Ak',
    'age': 33,
    'phone':231222,
    'name':'Mk'
}
print(d1, type(d1))

print(d1['name'])
print(d1['age'])

for i in d1.keys():
    print(i, end = "-")

print()

for i in d1.values():
    print(i,end="-")

print()
for i in d1.items():
    print(i)