class Dog:
  def bark(self, num_of_times):
    print(self.name * num_of_times)

my_pup = Dog()
my_pup.name = 'Max'
my_pup.bark(30)