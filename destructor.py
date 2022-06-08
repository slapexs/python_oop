'''
    Destructor
    จะถูกเรียกใช้งานหลังจากเรียกใช้ ​object
'''
from unicodedata import name


class DestructorClass:
    def showname(self, name):
        self.name = name
        print("Name:", name)
    def __del__(self): # optional
        print("This is destructor for restore memory")

obj1 = DestructorClass()
obj1.showname("Yuna")

# Output
# Name: Yuna
# This is destructor for restore memory