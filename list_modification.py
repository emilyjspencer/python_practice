n = [6, 12, 18]

n[1] = n[1] * 5
print(n)
#=> [6, 60, 18]

# pop() removes the item at a specified index 
n = [7, 14, 21]
n.pop(1)
#=> 14
print(n)
# prints [7, 21]


#remove() removes the specified item 
n = [2, 3, 4, 5,6 ]
n.remove(3)
print(n)
#=> [2, 4, 5, 6]

#del() removes the item at a specified index. DOESN'T return anything 
n = [2, 3, 4, 5,6 ]
del(n[3])
# Doesn't return anything
print(n)
# [2, 3, 4, 6]