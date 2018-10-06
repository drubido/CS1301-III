#Add an item to aList
def addItem(aList):
	aList.append("New Item!")
	print("aList:", aList)

myList = ["One", "Two", "Three"]
print("myList before addItem:", myList)
addItem(myList)
print("myList after addItem:", myList)

#Python passes primitive data types ByValue
#Python passes more advanced data types ByReference

