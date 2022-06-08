'''
    Polymorhism (การพ้องรูป)
        - Overloading method คือเมธอดชื่อเหมือนกันอยู่ในคลาสเดียวกันแตกต่างกันคือ parameter
        - Overiding method คือ เมธอดของคลาสลูก ที่ชื่อเหมือนเมธอคลาสแม่
'''
'''
    Overloading method
'''
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.salary = salary
        
    def showData(self):
        print("Name:", self.__name, "Salary:", self.salary)

class Accounting(Employee):
    __postionId = 100
    def __init__(self, name, salary, age):
        super().__init__(name, salary)
        self.age = age
    
    # Overiding method
    def showData(self):
        super().showData()
        print("Age:", self.age)

class Programmer(Employee):
    __postionId = 200
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary)
        self.__exp = experience
        self.__skill = skill

    # Overiding method
    def showData(self):
        super().showData()
        print("Skill:", self.__skill)
        print("Exp:", self.__exp)

    def __str__(self):
        return (super().__str__()+"Skill={} Exp={}".format(self.__skill, self.__exp))

class Sale(Employee):
    __postionId = 300
    def __init__(self, name, salary, area):
        super().__init__(name, salary)
        self.area = area

    # Overiding method
    def showData(self):
        super().showData()
        print("Area:", self.area)

obj_accouting = Accounting('Yuna', 12000, 22)
obj_programmer = Programmer('John', 20000, 2, 'WebDev')
obj_sale = Sale('Chai', 15000, 'Bangkok')

print("-----------------")

'''
    Overiding method
'''
print(obj_programmer.showData())
print(obj_accouting.showData())
print(obj_sale.showData())
print("--------------------")
print(obj_programmer.__str__())