'''Private Variables must be accessed inside the same class.'''
class Demo1:
    def __init__(self):
        self._name = 'Ak'
    def disp1(self):
        print(self._name)


d1 = Demo1()

'''
public : When we want to access variables anywhere in the code.
protected: When we want to access variables inside the same class and inside child class.
private: When we want to access variables inside the same class.

public: a = 10
protected: _a = 10
private: __a = 10
'''