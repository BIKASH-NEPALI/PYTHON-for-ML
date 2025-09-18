# Create student class that takes name and marks of 3 subjects as arguments in constructor .
#Then create a method to print the average.
class Student:
    def __init__(self,name,marks):#marks is a list
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for value in self.marks:
            sum+=value
        print("HI",self.name," your average marks:",sum/3)
s1=Student("deepika",[34,56,98])
s1.get_avg()
    