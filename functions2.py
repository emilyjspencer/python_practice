def distance_from_zero(number):
  if type(number) == int or type(number) == float:
   print(abs(number))
  else:
     print("Sunshine")

distance_from_zero(20)
distance_from_zero("happy")
distance_from_zero(4.5)

#=> 20
#=> Sunshine
#=> 4.5