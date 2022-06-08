'''
    การห่อหุ้ม (Encapsulation)
        - Access modifier = ระดับการเข้าถึง Class, Attribute, Method ประกอบด้วย 3 ระดับ
            Public
            Protected(_) = เข้าถึงได้เฉพาะ class ของตัวมันเองและ class ลูกที่จะสืบทอด
            Private(__) = จะมีแค่ class ตัวมันเองที่สามาถเข้าถึงได้
'''

class Employee:
    # Private method
    def __init__(self, name):
        # Public attribute
        self.name = name
        print("Name:", name)

    # Public method
    def showdata(self):
        print("Showdata name:", self.name)

obj1 = Employee('Yuna') # Name: Yuna
obj1.name = "Yeji"
obj1.showdata() # Showdata name: Yeji
print("--------------")

class Members:
    def __init__(self, name, age):
        self._name = name
        self.__age = age
        print("Name:", self._name, "Age:", self.__age)

    def showname(self):
        print("Self name:", self._name, "Age:", self.__age)

obj2 = Members('Rose', 22) # Name: Rose Age: 22
obj2.name = "Yuna"
print(obj2._name) # Rose
obj2._name = "Ryujin"
print(obj2._name) # Ryujin

obj2.showname() # Self name: Ryujin Age: 22
obj2.__age = 32 # Private แก้ไขข้อมูลไม่ได้
obj2._name = "Jenny"
obj2.showname() # Self name: Jenny Age: 22

