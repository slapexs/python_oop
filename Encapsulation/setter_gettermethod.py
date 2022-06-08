'''
    Setter and Getter method
        - Setter -> กำหนดค่าให้ Object
        - Getter -> ดึงค่าจาก Object
'''

class Members:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    # Setter method
    def setName(self, newname):
        self.__name = newname
    
    def setAge(self, newAge):
        self.age = newAge


    # Getter method
    def showData(self):
        return [self.__name, self.age]

    def getName(self):
        return self.__name

    
obj = Members('Yuna', 20)
print(obj.showData()) # ['Yuna', 20]
obj.setName('Yeji')
print(obj.showData()) # ['Yeji', 20]
print(obj.getName()) # Yeji