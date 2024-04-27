class Order:
    def __init__(self,item,price):
        self.items = item
        self.price = price

    def __gt__(self,ord2):
        return self.price > ord2.price


ord1 = Order("Book",100)
ord2 = Order("Pencil",10)

print(ord1 > ord2)