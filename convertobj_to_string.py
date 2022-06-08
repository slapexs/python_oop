'''
    Convert object ot string
'''

class Members:
    def __init__(self, name, age, salary):
        self.__name = name
        self.age = age
        self.salary = salary

    def printData(self):
        print("Name:", self.__name, "Age:", self.age, "Salary:", self.salary)

    def getIncome(self):
        return self.salary * 12

    def __str__(self):
        return ("Name={} Age={} Salary*12={}".format(self.__name, self.age, self.getIncome()))
    

class Employee(Members):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

dataUser = Employee("Yuna", 20, 12000)
print(dataUser.getIncome()) # 144000
print(type(dataUser.getIncome())) # int
print(dataUser.__str__()) # ('Name:', 'Yuna', 'Age:', 20, 'Salary*12:', 144000)
print(type(dataUser.__str__())) # tuple
        