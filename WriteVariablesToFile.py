#An example of writing variables to a file in Python

x = [3,4,5,6,7,7,8,8,9,10]

file = open("testfile.txt", "w")

for element in x:
    file.write(str(element) + "\n")#adding the  varaibles to the test file

file.close()