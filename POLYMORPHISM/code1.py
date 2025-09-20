class Complex:
    def __init__(self,real, img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(f"{self.real}i+{self.img}j")
    def add(self,obj):
        r=self.real+obj.real
        i=self.img+obj.img
        return Complex(r,i)
    def __sub__(self,obj): #operator ovelroading,dunder function 
        r=self.real-obj.real
        i=self.img-obj.img
        return Complex(r,i)
num1=Complex(3,4)

num2=Complex(2,1)
num3=num1.add(num2)
num3.showNumber()
num4=num2-num1
num4.showNumber()
