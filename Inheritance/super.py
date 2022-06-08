'''
    Super - เรียกใช้งาน Constructor, Method, Attribute จากคลาสแม่

    super().__init__(name)
'''

'''
    การสืบทอดคุณสมบัติ
    class motherClass:
        pass

    class kidClass:
        pass

    kidObj = kidClass(motherClass)
'''

class Employee:
    __minsalary = 12000
    maxsalary = 30000

    def __init__(self, name, age, positionId):
        self.__name = name
        self.age = age
        self.__positionId = positionId

    def getData(self):
        return [self.__name, self.age, self.__positionId]
    
    def printName(self):
        print("Name:", self.__name)


class Accounting(Employee):
    __positionId = '001'
    def __init__(self, name, age):
        super().__init__(name, age, self.__positionId)

class Programmer(Employee):
    __positionId = '002'
    def __init__(self, name, age):
        super().__init__(name, age, self.__positionId)
        super().printName()

class Sale(Employee):
    __positionId = '003'
    def __init__(self, name, age):
        super().__init__(name, age, self.__positionId)

obj_accounting = Accounting('Yuna', 23)
obj_programmer = Programmer('Jane', 24) # Name: Jane -> becuz use super().printName() in class Programmer(Employee)
obj_sale = Sale("Chai", 33)
print(obj_accounting.getData()) # ['Yuna', 23, '001']
print(obj_sale.getData()) # ['Chai', 33, '003']

