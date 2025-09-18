#methods that don't use self parameter.(works at class level)
class Student():
    @staticmethod
    def greet():
        print("hello welcome to the world!")
    def __init__(self,name):
        self.name=name
        print("your name is:",name)
S1=Student("Deepika")
S1.greet()