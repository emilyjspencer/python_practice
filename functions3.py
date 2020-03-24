a = 5
b= 20

def add_function(x, y):
  return x + y

print(add_function(a, b))

#=> 25



a = "Howdy"

def string_function(s):
	return s + ' parnter'

print(string_function(a))

#=>  Howdy partner




def list_function(x):
    x[1] =  x[1] + 3
    return x

n = [3, 5, 7]
print(list_function(n))

#=> [3, 8, 7]




n = [3, 5, 7]

def print_list(x):
  for i in range(0, len(x)):
    print(x[i])
    
print_list(n)

#=>  3
#=>  5
#=>  7
