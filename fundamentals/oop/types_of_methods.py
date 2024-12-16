class Bird:
  wings = False

  def __init__(self, color, species):
    self.color = color
    self.species = species

  def chirp(self):
    print('tweet')

  def fly(self, feet):
    print(f'The bird flies {feet} feet high')

  @classmethod
  def lay_eggs(cls, number):
    print(f"It laid {number} eggs")
    cls.wings = True
    print(Bird.wings)

  @staticmethod
  def look():
    print('The bird look')

my_bird = Bird('Red', 'Eagle')
my_bird.chirp()
my_bird.fly(20)
print(my_bird.species)


Bird.lay_eggs(21)
Bird.look()
print(f'My bird is a {my_bird.species} and it is {my_bird.color}')