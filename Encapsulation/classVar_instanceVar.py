'''
    Class variable and Instance variable
        - Class variable -> คือตัวแปรภายในคลาส ไม่จำเป็นต้องสร้าง object ก็เข้าถึงได้ (Level private เท่านั้น)
        - Instance variable -> คือตัวแปรที่อยู่ภายใน object เข้าถึงข้อมูลได้ต้องสร้าง object ก่อน
'''

class Members:
    def __init__(self, name, age):
        # Instance variable
        self.__name = name
        self._age = age

    def getData(self):
        return [self.__name, self._age]


obj = Members('Yuna', 20)
data = obj.getData()
print(data) # ['Yuna', 20]
print(obj._age) # 20

print("----------------")

class Employee:
    # class variable
    _minSalary = 12000
    _maxSalary = 30000

    def members(self, name, age):
        self.__name = name,
        self._age = age
print(Employee._minSalary) # 12000