from Employee import Employee

class Programmer:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    
    def printData(self):
        return ['Programmer file', self.__name, self.age]