li = list(eval(input('Enter comma separted elements:')))
print('Orginal List: ', li)

def even(ele):
    if ele % 2 == 0:
        return ele
    
even_li =list(filter(li))
print("Even List: ",even_li)