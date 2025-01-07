from abc import ABC,abstractmethod
class Manufacturer(ABC):
  @abstractmethod
  def manufacture(self):
      pass

class Car(Manufacturer):
  def __init__(self,*cars):
      self.cars=cars
      print("car manufacturer")
  def manufacture(self,*cars):
      print(f"manufactures {self.cars} in no time!!")

class Bike(Manufacturer):
  def __init__(self,*bikes):
      self.bikes=bikes
      print("Bike manufacturer")
  def manufacture(self):
      print(f"manufactures {self.bikes} very soon...yay!")

  def bike_price(self,*bikes):
      if self.bikes=="yamahaa":
          print(f"{self.bikes} costs around $80000")
      else:
          print("Try for new cars!!!")


def manufacture_unit(mtype):
    manufacturers={
        'car':Car,
        'bike':Bike

    }
    return manufacturers[mtype]()


