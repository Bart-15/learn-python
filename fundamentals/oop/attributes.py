class Bird:
  def __init__(self, color, species):
    self.color = color
    self.species = species


my_bird = Bird('Red', 'Eagle')

print(my_bird.species)

print(f'My bird is a {my_bird.species} and it is {my_bird.color}')