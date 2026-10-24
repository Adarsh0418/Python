class GreatGrandParent:
    def cook(self):
        print('GreatGrandParent cooks ABC')
class GrandParent:
    def cook(self):
        print('GrandParent cooks Birayani')
class Parent(GrandParent):
    def cook(self):
        print('Parent cooks Pulao')
class Child(Parent):
    def cook(self):
        print('Child cooks maggie')
        super().cook()
        super(Parent, self).cook()

c = Child()
c.cook()