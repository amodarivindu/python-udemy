x = {"hello", "Hello", "hi", "hi", "1"}  #in the set we can not have duplicate values and only key vaues are included
print(x)  # {'hello', 'hi', 'Hello'}

y = {"1", "2"}

z = y.union(y)  # we can use union method to add two sets
print(z)  # {'hello', 'hi', 'Hello', '1', '2'}

t = x - y

print(t)  # {'hello', 'hi', 'Hello'}  # we can use - operator to remove the elements of y from x