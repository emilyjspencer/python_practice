class Triangle(object):
  def __init__(self):
    self.sides = 3
 
  
shape = Triangle()
print(shape.sides)

#=>  3


class Person(object):
  def __init__(self, name):
    self.name = name

lily = Person("Lily")
print(lily.name)

#=>  Lily