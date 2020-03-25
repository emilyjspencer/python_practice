class ShoppingTrolley(object):
 
  
  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_trolley = {}
    
  def add_item(self, item, price):
    
    if not item in self.items_in_trolley: # if item isn't already in trolley
      self.items_in_trolley[item] = price # add item to trolling by adding key value to dictionary
      print(item + " added to trolley.")
    else:
      print(item + " is already in the trolley.")

  def remove_item(self, item):

    if item in self.items_in_trolley: # if item is already in trolley
      del self.items_in_trolley[item] # remove item from trolley using del
      print(item + " removed from trolley.")
    else:
      print(item + " is not in the trolley.")

trolley = ShoppingTrolley("emily")
trolley.add_item("oranges", 1)
trolley.add_item("apples", 1.5)
trolley.remove_item("apples")

#=> oranges added to trolley.
#=> apples added to trolley.
#=> apples removed from trolley.