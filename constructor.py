'''
    Constructor
    จะถูกเรียกพร้อมกับการสร้าง Object
'''

class Def_constructor:
    def __init__(self):
        print("Default constructor")

class Employee:
    # Create default constructor
    def __init__(self, name):
        self.name = name
        print("Name:", name, "from default constructor")

obj1 = Def_constructor() # Default Constructor
obj2 = Employee('Yuna') # Name: Yuna from default constructor
obj3 = Employee() # TypeError: __init__() missing 1 required positional argument: 'name'
