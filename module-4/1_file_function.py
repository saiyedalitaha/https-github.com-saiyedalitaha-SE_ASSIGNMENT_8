#What is File function in python? What is keywords to create  and write file.

file = open("example.txt", "w")
file.write("Hello, this is a new file.")
file.close()


with open("example.txt", "w") as file:
    file.write("Hello, this is a new file.")