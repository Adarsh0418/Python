t1 = (10,20,20,True, 'Code')
print(t1, type(t1))

print(t1[0])
print(t1[3])

# t1[0] = 300 //not allowed

'''
1.tuples stores Homogeneous as well as Hetrogeneous Type of Data.
2.Tuple is an Ordered Collection of Data.
3.Tuple stores duplicate values.
'''

#unpacking the tuple:
t2 =(100,200,300,400)
e1, e2, e3, e4 = t2
print(f'e1: {e1}, e2: {e2}, e3: {e3}, e4: {e4}')

tup1 = (10,20)
tup2 = (30, 40)
newtup = tup1  + tup2
print(len(newtup))