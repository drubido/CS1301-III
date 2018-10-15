#Write a function called "last_n" that accepts two arguments:
#a string search_string and an integer n. The function should
#return the last n characters from search_string. If
#search_string is shorter than n characters, then it should
#return the entire value of search_string.


def last_n(search_string, n):
    if len(search_string) < n:
        return search_string
    else:
        
        return search_string[-n:]



#The code below will test your function. If your function
#works correctly, this should print 789, saur, and 1.
print(last_n("123456789", 3))
print(last_n("Bulbasaur", 4))
print(last_n("1", 5))
myString = "You-are-a-strange-loop"
print(myString[-15:-5])