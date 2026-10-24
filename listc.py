li = [10,20,30,40]
sq =[ ]
for i in li:
    sq.append(i ** 2)

print('Square list:',sq)

print([i ** 2 for i in li])


#add +5 to each element of li 
print([i + 5 for i in li])

# even elements  from li
li1 = [1,2,3,4,5]
print([i for i in li1 if i%2 == 0])