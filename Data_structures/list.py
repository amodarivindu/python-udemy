#list
x = [12, 34, 56, 78]
y = x[2]
print(y)  # 56

x[3] = 100
print(x)  # [12, 34, 56, 100]
print(x[1])

#we can add new element to list
x.append(200)
print(x)  # [12, 34, 56, 100, 200] added at the end

x.insert(2, 300)
print(x)  # [12, 34, 300, 56, 100, 200] added at index 2

x.remove(100)
print(x)  # [12, 34, 300, 56, 200] removed 100
x.pop(2)
print(x)  # [12, 34, 56, 200] removed 300 by index

#adding two lists
y = [12, 34, 56, 78]
z = x + y
print(z)  # [12, 34, 56, 200, 12, 34, 56, 78] concatenated


is_this_value_in_list = 34 in x
print(is_this_value_in_list)  # True
is_this_value_not_in_list = 100 in x
print(is_this_value_not_in_list)  # False    


