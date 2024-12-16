class Animal:
  def __init__(self, age, color):
    self.age = age
    self.color = color

  def born(self):
    print('This animal has been born')

class Bird(Animal):
  pass

my_bird = Bird(1, 'red')

my_bird.born()

print(my_bird.color)