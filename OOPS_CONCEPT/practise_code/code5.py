class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
    def __gt__(self,ord2):
        return self.price>ord2.price
order1=Order("chips",10)
order2=Order("Biscuit",30)
print(order1>order2)
