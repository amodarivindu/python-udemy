a = [10, 23, 54, 45, 67]

b = list(a)  # Copying the list)

b.append(100)  # Adding an element to the copied list
print(a)
print(b)

###################################################################################

c = [12, 23, 45, 27, 89]

d = []

for i in c:
    d.append(i)  # Appending elements from c to b
print(d)  # b now contains elements from both a and c

###################################################################################

e = [i for i in c]  # List comprehension to copy elements from c
print(e)  # e contains elements from c using list comprehension

f = [i * 2 for i in c]  # List comprehension to double each element in c and we can ad conditios for new list
print(f)  # f contains elements from c, each multiplied by 2

###############################################################################
def is_odd(number):
    return "odd" if number % 2 != 0 else "even" # Function to check if a number is odd or even

x = [32, 22, 34, 45, 57, 61]  # Define your list

g = [is_odd(value) for i, value in enumerate(x) if i % 2 == 0]  # List comprehension with condition to filter even numbers 

print(g)  # Output: ['odd', 'odd', 'odd']  # g contains the results of is_odd for even indexed elements in x