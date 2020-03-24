#=> Use of index() and insert() methods

pets = ["cat", "dog", "rabbit", "hamster", "gerbil", "budgie"]

rabbit_index = pets.index("rabbit")


print(pets.index("rabbit"))

pets.insert(6, "parrot")
print(pets)

#=> 2
#=> ['cat', 'dog', 'rabbit', 'hamster', 'gerbil', 'budgie', 'parrot']