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
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type
car1=Fortuner("electric_car")
car1.start()