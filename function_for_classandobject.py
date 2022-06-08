'''
    isinstance and dir คือฟังก์ชันที่ทำงานกับ class, object
        - instance -> เช็คว่า Object นี้ถูกสร้างจาก class ที่เรานิยามหรือไม่
        - dir -> แสดง Attribute และ Method
        - __class__ -> แสดงชื่อ class ของ object
'''

class Employee:
    def showname(self):
        pass
    pass

class Numberone:
    pass

obj1 = Employee()
print(isinstance(obj1, Employee)) # True
print(isinstance(obj1, Numberone)) # False

# print(dir(obj1))
# Output
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    
print(dir(obj1.showname))
# Output
# ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
print(obj1.__class__) # <class '__main__.Employee'>