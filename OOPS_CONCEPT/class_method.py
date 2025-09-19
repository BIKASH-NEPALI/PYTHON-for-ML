class Person:
    name="anonymous"
    #def change_name(self,name):
        #self.name=name
    @classmethod
    def change_name(cls,name):#class method 
        cls.name=name
P1=Person()
P1.change_name("Bikash")
print(P1.name)
print(Person.name)