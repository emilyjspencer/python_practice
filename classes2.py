

class Actor(object):

    def __init__(self, name, age, nationality):
      self.name = name
      self.age = age
      self.nationality = nationality

dustin = Actor("Dustin", 82, "American")
jack = Actor("Jack", 82, "American")
clint = Actor("Clint", 89, "American")

print(dustin.name, dustin.age, dustin.nationality)
print(jack.name, jack.age, jack.nationality)
print(clint.name, clint.age, clint.nationality)