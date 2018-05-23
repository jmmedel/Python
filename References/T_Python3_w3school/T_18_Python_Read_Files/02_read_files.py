

"""
Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many character you want to return:

Example
Return the 5 first characters of the file:"""

f = open("demofile.txt", "r")
print(f.read(5))


"""
Read Lines
You can return one line by using the readline() method:

Example
Read one line of the file:"""

f = open("demofile.txt", "r")
print(f.readline())

"""
By calling readline() two times, you can read the two first lines:

Example
Read two lines of the file:"""

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


"""
By looping through the lines of the file, you can read the whole file, line by line:

Example
Loop through the file line by line:"""

f = open("demofile.txt", "r")
for x in f:
  print(x)
  