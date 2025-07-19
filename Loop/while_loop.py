'''x = [10, 8, 6, 4, 2]

max_val = x[0]
min_val = x[0]

for i in x:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i 

print("max value is", max_val)  # 10
print("min value is", min_val)  # 2
'''

count = 0
while count < 5:
    print("count", count)  # 0 1 2 3 4
    count += 1

#difference between for and while loop

    #for loop is used when we know the number of iterations and for loop get next value from the iterable
    #and it will stop when the iterable is finished

    #while loop is used when we dont know the number of iterations and while loop don't get next value from the iterable
    #and it will stop when the condition is false