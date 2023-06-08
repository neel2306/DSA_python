from array import *

#Declaring an array
arr1 = array('i', [1,2,3,4,5])
arr2 = array('d',[1.2,4.5,6.7,8.2])

#print(arr1)

#Insertion in array.
arr1.insert(5,6)
#print(arr1)

#Trying to insert in the beginning of arr1
#arr1.insert(0,0)
#print(arr1)

#Traversing an array.
def traverseArray(array):
    for idx,item in enumerate(array):
        print(idx,item)
#traverseArray(arr1)

#Accessing array element.
def accessElemnt(array, index):
    if index > len(array):
        print("Error")
    else:
        print(array[index])
#accessElemnt(arr1, 3)

#Searching in array.
def searchArray(array, element):
    for i in array:
        if i == element:
            return array.index(element)
        return 'Element does not exist'
#print(searchArray(arr1, 4))

#Deleting an element in an array.
arr1.remove(5)
print(arr1)