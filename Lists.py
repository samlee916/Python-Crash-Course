#An example of using lists and what you can do with it

shopping = ["Eggs", "Milk", "Coffee"]
print(shopping)
print(shopping[0])#prints out the first item
print(shopping[-1])#prints out the last item regardless of the length of the list
print(shopping[-2])#prints out the second to last item of the list

shopping[0] = "Bread"#replacing the first item in the list
print(shopping)

grocery = ["Eggs", "Milk", "Coffee"]
del grocery[0]#deletes first item
print(grocery)
grocery.append("Water")#adds water to the list
print(grocery)

grades = [1,2,3,1,2,3,7,8,9]
print(min(grades))#prints out the minimum number of that list
print(max(grades))#prints out the maximum number of that list
print(len(grades))#prints out the length of that list



