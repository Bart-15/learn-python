import datetime

class Car:
  def getCarAge(self):
    currentYear = datetime.date.today().year
    return currentYear - self.year


my_car = Car()
my_car.year = 2005
print(my_car.getCarAge())