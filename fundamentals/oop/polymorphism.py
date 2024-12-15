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

a_word = "polymorphism"
a_list = ["Classes", "OOP", "Polymorphism"]
a_tuple = (1, 2, 3, 80)

def get_length(list_data):
  total_length = len(list_data)

  return print(total_length)
    
iterate_list = [a_word, a_list, a_tuple]
    

for data in iterate_list:
  get_length(data)
    