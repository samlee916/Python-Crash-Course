#An example of writing a file and opening it in Python

file = open("testfile.txt", "w")#creates and overwrite teh file
file.write("Hello World!")
file = open("testfile.txt", "a")#adds the word to the file
file.write("\nHello World!!!")
file.close()
