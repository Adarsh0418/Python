def add(a,b):
    print("Start")
    print(a/b)
    print("End")

try:
    add(10,2)
except:
    print("Exception Occurred and Handled...")
else:
    print("There is no Exception")
finally:
    print("End")
print('Other Tasks')