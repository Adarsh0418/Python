from functools import reduce

li =[1,2,3,4,5,6]

def sum(a,b):
    return a+b

sum_res = reduce(sum,li)
print(sum_res)