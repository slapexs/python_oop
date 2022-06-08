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

    def __init__(self, name, age):
        self.__name = name
        self.age = age


class Accounting(Employee):
    def __init__(self):
        pass

class Programmer(Employee):
    def __init__(self):
        pass

class Sale(Employee):
    def __init__(self):
        pass

obj_accounting = Accounting()
obj_programmer = Programmer()
obj_sale = Sale()

print(obj_sale.maxsalary) # 30000
print(obj_programmer._Employee__minsalary) # 12000 _motherClass__classVar for private level