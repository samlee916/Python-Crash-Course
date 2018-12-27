#An example of using a for loops

students = ["Alice", "Dan", "Suzie"]
for student in students:
    print(student)#prints out each student is the list

x = "Hello"
for char in x:#prints out every char in what is stored in x
    print(char)

y = list(range(1,11))
print(y)
for i in y:#prints out 1-10
    print(i)

for i in range(1,10):#range(min, max+1)
    print(i)#using the range function, prints out 1-9