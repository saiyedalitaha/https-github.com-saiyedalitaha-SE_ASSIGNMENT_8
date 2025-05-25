# 1). What is File function in python? What is keywords to create and write file.

# The file function is python file object provides methods and attributes to access and manipulate files.
# Using file objects, we can read or write any files. Whenever we open a file to perform any operations on it, 
# Python returns a file object.

f = open('demofile3.txt','w')
f.write('Paragraphs are the building blocks of papers.!')
f.close()
