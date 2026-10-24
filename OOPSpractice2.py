class Employee:
    company_name = 'Code'

    def work(self):
        print(self.name,' is working')

    def play(self):
        print(self.name,' is playing')

c1 = Employee()
c1.name = 'AK'
c1.id = 101
c1.work()

c2 = Employee()
c2.name = 'Pk'
c2.id = 102
c2.work()
c2.play()