#Add an exclamation to aString
def addExc(aString):
	aString = aString + "!"
	print("aString:", aString)

myString = "Hello, world"
print("myString before addExc:, ", myString)
addExc(myString)
print("myString after addExc:", myString)