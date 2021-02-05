'''
The first function adds elements to the list that are not already present
in it and the second function does the same thing with the added functionality
of saving the rejected elements from the first list to a second list.
'''

myUniqueList = []
myLeftovers = []

def addToList(element):
    if element not in myUniqueList:
        myUniqueList.append(element)

def addToListWithRejected(element):
    if element not in myUniqueList:
        myUniqueList.append(element)
    else:
        myLeftovers.append(element)

addToList(1)
addToList(2)
addToList(1)
print(myUniqueList)
print(myLeftovers)

addToListWithRejected(3)
addToListWithRejected(2)
addToListWithRejected(1)
print(myUniqueList)
print(myLeftovers)
