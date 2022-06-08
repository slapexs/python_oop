# Attribute
class Employee:
    # Create method
    def detail(self):
        # print("Method detail on class Employee")
        self.name = "Yuna"
        self.salary = 30000
        print("Name:", self.name)
        print("Salary:", self.salary)

# Create oject
obj1 = Employee()
# Call method
obj1.detail() # Name: Yuna , Salary: 30000


'''
    กำหนดค่าให้ Attribute
'''
class Employee1:
    def info(self, name, salary):
        self.name = name
        self.salary = salary
        print("Name:", self.name, " Salary:",self.salary)
        

obj2 = Employee1()
obj2.info('Yeji', 25000) # Name: Yeji  Salary: 25000
obj3 = Employee1()
obj3.info('Rose', 40000) # Name: Rose  Salary: 40000