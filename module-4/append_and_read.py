
with open("example.txt", "a") as file:
    file.write("This is the new line added.\n")


with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

#Run this code  using the terminal:
#python append_and_read.py

