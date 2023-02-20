class Employee():
    def __init__(self):
        self.name = []
        self.payment = []
        self.database = {}
    

    def neat_name(self, last_name, first_name):
        combine = last_name + ' ' + first_name
        self.name.append(combine.title())


    def employee_payment(self, salary):
        self.payment.append(int(salary))


    def name_salary(self):
        self.database = dict(zip(self.name, self.payment))
        print(self.database)
        


    def give_raise(self, name, added = ''):
        if added:
            self.database[name] = self.database[name] + added
            print(name + ': ' + str(self.database[name]))
        else:
            self.database[name] = self.database[name] + 5000
            print(name + ': ' + str(self.database[name]))