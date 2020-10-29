## Author: Feras
## Description: A function that searches a list of words 
##  and uses a key char to find a word and returns a list.

def searchString(stringLst, keyword):
    foundKeyWord = []
    for i in stringLst:
        for j in i:
            if j == keyword:
                foundKeyWord.append(i)
    return foundKeyWord
print(searchString(["rose", "flower", "nice", "light", "beautiful"],"i"))