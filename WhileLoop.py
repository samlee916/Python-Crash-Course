#An example of using the while loop

i = 1
while i < 10:
    print(i)#will keep printing until it reaches 9
    i = i + 1#increments by 1 on each execution

j = 1
while j < 12:
    print(j)
    j = j + 1
else:
    print("Greater than 12.")

k = int(input("Enter k: "))
while k < 10:
   k = int(input("Enter k: "))#stops when the user input 10 or more

t = []
inp = input("Enter a value: ")
while inp != "stop":#keeps adding until you enter stop
    t.append(inp)
    inp = input("Enter a value: ")
    print(t)
