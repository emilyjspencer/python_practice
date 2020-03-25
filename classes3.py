class Animal(object):

  is_mammal = True # variable available throughout class

  def __init__(self, name, colour):
   self.name = name
   self.colour = colour
  
  def description(self):
    print(self.name)
    print(self.colour)
    
whale = Animal("Harold", "grey")
whale.description()


class Animal(object):

  is_mammal = True # variable available throughout class
  is_healthy = True # variable available throughout class

  def __init__(self, name, colour):
    self.name = name
    self.colour = colour

  def description(self):
    print(self.name)
    print(self.colour)
    
cheetah = Animal('Nom', "orange and black")
dingo = Animal('I_stole_your_baby', "brown")
raccoon = Animal('Ringo', "medium grey")

print(cheetah.is_healthy)
print(dingo.is_healthy)
print(dingo.name)
print(raccoon.is_healthy)