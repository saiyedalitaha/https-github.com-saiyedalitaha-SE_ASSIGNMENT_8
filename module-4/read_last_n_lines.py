def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[-n:]:
            print(line, end='')


file_path = 'file_manage.txt'  
num_lines = 5              
read_last_n_lines(file_path, num_lines)
