# Lists are made of square braces, and they can contain many elements of different types in Python
# You can add, remove and update elements from a list  
l = ['Gabriel', 'Roberto', 'Carla', 2004]

# Tuples are very similar to lists, but here we use normal braces
# You can add and remove elements from a tuple, but never update them
t = ('Gabriel', 'Roberto', 'Carla', 2004)

# Sets are a bit different
# Sets won't accept duplicate elements
s = {'Gabriel', 'Roberto', 'Carla', 2004, 2004} # In this case 2004 won't appear twice
# Sets also don't keep an order of elements different than lists and tuples
print(s)

# ------------------------------------------------------------------------------------------

# In lists and tuples you can access individual elements by doing the following
print(l[0]) # Where the number means the index
print(t[2])

# You can also access from a reverse order
print(l[-1]) # Will give the last element of the list

# You can't access individual elements in sets
# print(s[2]) -> This won't work