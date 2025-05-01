n = 3  # Number of lines to read

with open("file_manage.txt", "r") as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line, end="")

#Run this code  in the terminal:
#python read_first_n_lines.py
