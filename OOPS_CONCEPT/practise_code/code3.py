#import math
class Circle:
    def __init__(self, radius):
        self.radius=radius
    def calcarea(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return (22/7)*self.radius
c1=Circle(21)
print(c1.calcarea())
print(c1.perimeter())