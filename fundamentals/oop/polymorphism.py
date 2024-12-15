class Cow:

  def __init__(self, name):
    self.name = name

  def talk(self):
    print(self.name)


class Sheep:
  def __init__(self, name):
    self.name = name

    def talk(self):
      print(self.name + 'bleats')

cow1 = Cow('Bert')
sheep1 = Sheep('Jay')

def animal_talks(animal):
  animal.talk()

animal_talks(sheep1)