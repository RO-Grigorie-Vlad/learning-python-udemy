#work with files

#create file or write to file (overwrites)
myFile = open("section3/file.txt", "w")
    #'r' open for reading (default)
    #'w' open for writing, truncating the file first
    #'a' append to a file

myFile.write("Hello from python\nThis is the second line")

#write to file (does NOT overwrites)
myFile = open("section3/file.txt", "a")
myFile.write("\nThis line was added after")

#read the file

# myFile = open("D:\\Udemy\\Python\\section3\\file.txt", "r") #full path (windows)

myFile = open("section3/file.txt", "r")
fileContents = myFile.read()
print(fileContents)

#reset the cursor for a more than one reading
myFile.seek(0)
fileContents = myFile.read()
print(fileContents)

#reading line-by-line
myFile.seek(0)
line = myFile.readline()
count = 0
while line:
    print("Line{}: {}".format(count, line.strip()))
    line = myFile.readline()
    count +=1
#or:
myFile.seek(0)
a =  myFile.readlines()
print(len(a))
print(a)

#closing a file - first option
myFile.close()

#this way we don't have to remmeber to close the file :
with open('section3/file.txt') as my_file :
    contents = my_file.read()

# why use with keyword:

# the advantage of using a with statement is that it is guaranteed 
# to close the file no matter how the nested block exits. 
# If an exception occurs before the end of the block, 
# it will close the file before the exception is caught 
# by an outer exception handler. 
# If the nested block were to contain a return statement, 
# or a continue or break statement, the with statement would automatically 
# close the file in those cases, too.