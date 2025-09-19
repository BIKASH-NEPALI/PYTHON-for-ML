class Car:
    color="black"
    @staticmethod
    def start():
        print("Car started")
        @staticmethod
        def stop():
            print("car stopped.")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
Car1=ToyotaCar("honda")
Car2=ToyotaCar("swift")
print(Car1.name)
print(Car1.start())
print(Car2.color)