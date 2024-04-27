class Car:
    @staticmethod
    def start():
        print('car started..')
    @staticmethod
    def stop():
        print('car stopped..')


class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

class Fortune(ToyotaCar):
    def __int__(self,type):
        self.type = type        

car1 = ToyotaCar('toyota')
car2 = ToyotaCar('prious')

print(car1.name)