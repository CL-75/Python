from abc import ABC, abstractmethod

class Vehicle(ABC):
  def action(self):
    pass
    
 class Car(Vehicle):
   def action(self):
    print("I can drive on the road")
    
class Boat(Vehicle):
  def action(self):
    print("I can drive on the water")
    
class Plane(Vehicle):
  def action(self):
    print("I can fly in the air")
    
    
C = Car()
C.action()

B = Boat()
B.action()

A = Plane()
A.action()
