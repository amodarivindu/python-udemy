#file = open("input/data.txt")

'''print(type(file))  # Output: <class '_io.TextIOWrapper'>

content = file.read(5)  # Read the file content
print(content)  # Output the content of the file

content = file.read()  # Read the file content
print(content)  # Output the content of the file'''

#############################################################

'''content = file.readline()  # Read the first line of the file
print(content)  # Output the first line of the file

while True:
    content = file.readline()  # Read the next line of the file
    if not content:  # If no more lines, break the loop
        break
    print(content)  # Output the next line of the file

for line in file:  # Iterate through each line in the file
    print(line)  # Output each line of the file'''

'''for i, line in enumerate(file):  # Iterate through each line with an index
    print(f"Line {i}:", line)  # Output each line with its index

file.close()  # Always close the file when done'''

######################################################################

'''file = open("input/data.txt", "w")  # Open the file safely using 'with' statement

for i in range(0, 10):
    file.write(f"Line {i}\n")  # Write lines to the file'''

################################################################

with open("input/data.txt", "r") as file_new:  # Open the file safely using 'with' statement
    contents = file_new.read()  # Write lines to the file
    print(contents)  # Output the content of the file