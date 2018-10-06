myList = ["One", "Two", "Three"]
#Print the spot inmemory to which
#myList is pointing
print(id(myList))
myList.append("Four")
#Print the spot inmemory to which
#myList is pointing
print(id(myList))
myList = ["Five", "Six", "Seven"]
#Print the spot inmemory to which
#myList is pointing
print(id(myList))