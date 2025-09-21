class employee:
    def __init__(self,role, dept,salary):
        self.dept=dept
        self.role=role
        self.salary=salary
    def showDetails(self):
        print(f"role:{self.role} and department is {self.dept}\n salary is{self.salary}")
e1=employee("accountant","Finance",40000)
e1.showDetails()
class Engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","computer science",67000)
eng1=Engineer("bikash","20")
eng1.showDetails()