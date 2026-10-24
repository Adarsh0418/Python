def process(a,b):
    print(a/b)

try:
    process(10,ak)
except ZeroDivisionError:
    print('ZeroDivison Error occurred and Handled')
except NameError:
    print('Name Error ocurred and Handled')
except TypeError:
    print('Type Error ocurred and Handled')
except:
    print('Some Exception')
finally:
    print("End")