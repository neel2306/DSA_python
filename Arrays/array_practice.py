from array import *

#Create an array and traverse
arr1 = array('i', [1,2,3,4,5])

def traverseArray(array):
    for i in array:
        print(i)
#traverseArray(arr1)

#Access individual elements through indexes.
def accessEele(array, index):
    if index > len(array):
        print('Error')
    else:
        print(array[index])
#accessEele(arr1, 3)

#Append a value to array.
def appendValue(array, value):
    array.append(value)
    print(array)
#appendValue(arr1, 6)

#Insert a value.
def insertValue(array, index, value):
    array.insert(index, value)
    print(array)
#insertValue(arr1, 5, 6)

#Extend a python array
arr2 = array('i',[6,7,8,9])
def extendArray(array1,array2):
    array1.extend(array2)
    print(array1)
#extendArray(arr1, arr2)
