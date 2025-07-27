
name = "Amoda"
height = 176
message = "my height is cm " + str(height)
print(message) 
message = "Hello %s. My height is %d cm." % (name, height) # c-style string formatting
print(message)  # Output: Hello Amoda. My height is 176 cm.

message = "Hello {}. My height is {} cm.".format(name, height)  # str.format() method
print(message)  # Output: Hello Amoda. My height is 176 cm.
message = "Hello {1}. My height is {0} cm.".format(name, height)  # str.format() method
print(message)  # Output: Hello 176. My height is Amoda cm.

message = f"Hello {name}. My height is {height:05d} cm."  # f-string formatting (Python 3.6+)
print(message)  # Output: Hello Amoda. My height is 176 cm.

'''hello amoda
my name is pipuni
''' #comment multiple lines