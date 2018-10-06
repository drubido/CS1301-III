def addOne(num):
	num = num + 1
	print(num)


# By VALUE
myNumber = 5

print(myNumber)
print(id(myNumber))

addOne(myNumber)

print(myNumber)


print("---------------------------")
#By REFERENCE
num1 = 1
num2 = 2
num3 = 3

numList = [num1, num2, num3]
print(id(numList[0]))
print(id(numList[1]))
print(id(numList[2]))

print("---------------------------")

for num in numList:
	addOne(num)
	print(id(num))

print(numList)
print(id(numList))

print("---------------------------")

addOne(numList[0])

print(numList)

print("---------------------------")
def addOneToAll (numList):
	for num in numList:
		num = num + 1
	print(numList)

print(numList)
print(id(numList))

addOneToAll(numList)







