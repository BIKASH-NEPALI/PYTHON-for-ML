class Student:
   university="Farwestern uninversity"#class attributes(same for all objects)
   
   #def __init__(self):
       #print("this is a deafult constructor ")
   def __init__(self,name, age, branch):# object attributes(differ for all objects)
       self.name=name
       self.age=age
       self.branch=branch
       print("constrctor is called")# invoke automatically
   def greet(self):
        print("hello mate, how area you?")
   def get_branch(self):
       print("your are from",self.branch,"branch")
       
       

#s3=Student()
s1=Student("prabin ",22,"computer")
s2=Student("ram dhami","21","computer")
s2.get_branch()
s2.greet()
print(s1.university)
print(s1.name,s1.branch)
print(s2.name,s2.age)
class Car:
    brand="mercedez"
    model="A23"
    color="BLUE "
c1=Car()
print(c1.color)
print(c1.brand)