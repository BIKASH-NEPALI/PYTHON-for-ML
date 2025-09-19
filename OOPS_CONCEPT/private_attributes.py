class Person:
    __name="anonymous" #private
    def __hello(self):
        print("hello person")
    def welcome(self):
        self.__hello(self)
p1=Person()
print(p1.welcome())
