from abc import ABC,AbstractMethod
class Manufacturer(ABC):
  @abstractmethod
  def manufacture():
      pass

class Car(Manufacturer):
  def __init__(self):
      print("car manufacurer")
  def manufacture(self,cars):
      print(f"manufactures {self.cars} in no time!!")

class Bike(Manufacturer):
  def __init__(self):
      print("Bike manufacturer")
  def manufacture(self,bikes):
      print(f"manufactures {self.bikes} very soon...yay!")
      
