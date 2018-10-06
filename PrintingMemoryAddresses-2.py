myint1 = 5
#Printing the spot inmemory to which
#myInt1 is poiting
print(id(myint1))
myint1 = 6
#Printing the spot inmemory to which
#myInt1 is poiting
print(id(myint1))

myList = ["One", "Two", "Three"]
#Printing the spot inmemory to which
#myList is poiting
print(id(myList))
myList.append("Four")
#Printing the spot inmemory to which
#myList is poiting
print(id(myList))