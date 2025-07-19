x = [24, 654, 23, 45, 67, 89, 12, 34, 56, 78] # list

'''total = sum(x)
print("Total is", total)  # 24 654 23 45 67 89 12 34 56 78
average = total / len(x)
print("Average is", average)  # 24 654 23 45 67 89 12 34 56 78'''

#get the sum of all values in the list
total = 0
for i in x:
    total += i
print("Total is", total)  # 24 654 23 45 67 89 12 34 56 78
print("avg is", total/len(x))

#get the max and min value in the list

max_value = x[0]
min_value = x[0]
for i in x:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i

print("max value is", max_value)  # 24 654 23 45 67 89 12 34 56 78
print("min value is", min_value)  # 24 654 23 45 67 89 12 34 56 78