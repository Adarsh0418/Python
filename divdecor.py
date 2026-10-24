def smatdiv(function):
    def inner(a, b):
        if b == 0:
            print('Not possible')
        else:
            return function(a,b)
    return inner


@smatdiv
def div(a, b):
    print(a/b)

div(10, 2)
div(20, 5)
div(10, 0)