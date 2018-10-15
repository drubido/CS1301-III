myString = "0123456789"

print (myString[0])
print (myString[-1])
print (myString[-2])
print (myString[-10])
print (myString[1:])
print (myString[:0])
print (myString[5:])
print (myString[0:3])
print (myString[0::3])
print (myString[0::])
print (myString[::9])
print (myString[5+1:])
print (myString[:2])


def scramble(aString):
	if len(aString) % 2 == 0:
		aString = aString[len(aString)/2:] + aString[:len(aString)/2]
	else:
		aString = aString[len(aString)//2:] + aString[:len(aString)//2]
	return aString

string1 = "abcd"
string2 = "abcde"
string3 = "railroad"
string4 = "fireworks"
print(string1 + " -> " + scramble(string1))
print(string2 + " -> " + scramble(string2))
print(string3 + " -> " + scramble(string3))
print(string4 + " -> " + scramble(string4))

