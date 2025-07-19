'''count = 0

while True:

    if count == 5:
        break
    print("count", count)  # 0 1 2 3 4
    count += 1
    '''

x = [10, 8, 5, 4, 2]

count = 0   

while count < len(x): #here we should give the logic to stop the loop
    '''print("index", count)  # 0 1 2 3 4

    i = x[count]
    print("value", i)  # 10 8 5 4 2'''

    i = x[count]
    if i == 5:
        count += 1
        continue
    print("value", i)  # 10 8 4 2

    count += 1

#using countinue in loop we can skip the value
#using break in loop we can stop the loop