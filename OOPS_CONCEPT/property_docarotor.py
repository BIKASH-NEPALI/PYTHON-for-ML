class student:
    def __init__(self, phy , chem, math):
        self.chem=chem
        self.phy=phy
        self.math=math
        #self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    #def clc_percent(self):
       # self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    @property  #make any function as an property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
            
std1=student(80,90,45)
print(std1.percentage)
std1.math=50
print(std1.percentage)
std1.phy=100
print(std1.percentage)
#std1.clc_percent()
#print(std1.percentage)