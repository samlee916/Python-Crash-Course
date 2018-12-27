#A Python example of reading a file

files = open("testfile.txt", "r")
print(files.readlines())#reads the file and prints it out
files.close

#another way to open/read a file
with open("testfile.txt") as files:
    print(files.readlines())