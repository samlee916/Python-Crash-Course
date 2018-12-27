#An example about dictionary

words = {"A": "Apple", "B": "Bee"}
print(words["A"])#prints out Apple
print(words["B"])#prints out Bee
print(words.values())

words["C"] = "Can"#adding to the dictionary
words["D"] = "Dog"
print(words)

del words["A"]#deletes A
print(words)

months = {"January": 1, "February": 2}
print(months["February"])#prints out 2
