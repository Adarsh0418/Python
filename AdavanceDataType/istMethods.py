li = [50]
# Adding Element into List(at the end of the list) using append():
li.append(100)
print(li)

#insert(index, element) inserts an element at specific index
li.insert(0,500)
print(li) 

#pop(): pop method without any argument removes and returns last element from the list.
ele = li.pop()
print(ele)
print(li)

#pop (index) : pop can remove specific index element from ist.
print(li.pop(0))
print(li)

#
li.append(700)
print(li)
#remove(element): removes element form list.
li.remove(700)
print(li)

#del keyword:
del li[1]
print("After del: ",li)