## Generators.py# This module contains a generator function that yields odd numbers up to a specified limit.
def get_odd_numbers(upper_limit):
    odd = []
    for number in range(1, upper_limit, 2):  # Start from 1 and increment by 2 to get odd numbers
        if number % 2 == 1:
            odd.append(number)
    return odd  # Return the list of odd numbers
        

x = get_odd_numbers(10)  # Call the function with an upper limit of 100
print(x)  # Output the list of odd numbers
## If use above code it will a disadvantage of memory usage as it stores all odd numbers in a list.


# Instead, we can use a generator to yield odd numbers one by one.
def get_odd_numbers(upper_limit):
    for number in range(1, upper_limit, 2):  # Start from 1 and increment by 2 to get odd numbers
        if number % 2 == 1:
            yield number

print("starting generator")
y = get_odd_numbers(10)        
print("finishing generator")
# This will create a generator object that can be iterated over to get odd numbers
# Using a generator is more memory efficient as it yields one number at a time in stead of storing

for number in y:  # Call the generator function with an upper limit of 10
    print(number)  # Output each odd number yielded by the generator

print(y)  # Output the generator object
