class Car:
    def __init__(self, brand, age) :
        self.brand=brand
        self.age=age
    def identify(self): 
        print(' This car is a ' + self.brand + ' age ' + str(self.age))
    def modifyAge(self, newAge):
        self.age=newAge
        print('The new age of the car', self.brand,  'is', str(self.age))
        