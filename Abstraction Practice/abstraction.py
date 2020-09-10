from abc import ABC, abstractmethod

class Vehicle(ABC):
    def printNum(self,x):
        print("Passed Value: ", x)
    @abstractmethod
    def action(self):
        print("This is the Vehicle class")

            
class Car(Vehicle):
    def action(self):
        print("I can drive on the road")
    
class Boat(Vehicle):
    def action(self):
        print("I can travel on the water")
    
class Plane(Vehicle):
    def action(self):
        print("I can fly in the air")
    
    
C = Car()
C.printNum(100)
C.action()

B = Boat()
B.printNum(400)
B.action()

A = Plane()
A.printNum(120)
A.action()
