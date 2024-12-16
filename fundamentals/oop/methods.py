class Bird:
  def __init__(self, color, species):
    self.color = color
    self.species = species

  def chirp(self):
    print('tweet')

  def fly(self, feet):
    print(f'The bird flies {feet} feet high')

my_bird = Bird('Red', 'Eagle')
my_bird.chirp()
my_bird.fly(20)
print(my_bird.species)


print(f'My bird is a {my_bird.species} and it is {my_bird.color}')