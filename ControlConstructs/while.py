#1-10
i = 1
while (i<11):
    print(i)
    i=i+1

#1-5
for i in range(1,6):
    if(i == 3):
        continue
    else:
        print(i)

#1-10
for i in range(1,11):
    if(i == 5):
        break
    else:
        print(i)

# 2*2 = 4
num = int(input('Enter your Number: '))
for i in range(1,11):
    print(i * num,end = " ")