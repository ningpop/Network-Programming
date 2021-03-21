class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)
    
    def getAge(self):
        print(self.age)

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID
    
    def getID(self):
        print(self.employeeID)

employee = Employee('IoT', 65, 2018)
employee.getName()
employee.getAge()
employee.getID()