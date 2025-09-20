class Complex:
    def __init__(self,real, img):
        self.real=real
        self.img=img
        print(f"{self.real}+{self.img}i")
    def __sub__(self,obj):
        real=self.real-obj.real
        img=self.img-obj.img 
        return Complex(real,img)
    @property
    def showresult(self):
        if self.img>0:
            sign="+"
        else:
            sign="-"
        print(f"{self.real}{sign}{self.img}i")
Cmplx1=Complex(4,5)
Cmplx2=Complex(4,7)
Cmplx3=Cmplx1-Cmplx2
Cmplx3.showresult

        
        