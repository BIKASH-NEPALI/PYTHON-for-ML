class Car: 
    def __init__(self):
        self.acc=False
        self.brake=False
        self.clutch=False
        
    def starts(self):
        self.clutch=True
        self.acc=True
        print("car started")
Car1=Car()
Car1.starts()