class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    
    def printData(self):
        print("Name:", self.__name, "Age:", self.age)