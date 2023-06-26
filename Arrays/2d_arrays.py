import numpy as np

twoDArray = np.array([[1,2,3], [4,5,6], [7,8,9]])
#print(twoDarray)

#Insertion
new2DArray = np.insert(twoDArray, 0, [[10,11,12]], axis=1)
#print(new2DArray)

#Accessing in 2d arrays
def accessEle(array, rowIdx, colIdx):
    if rowIdx >= len(array) and colIdx >= len(array[0]):
        print('Error')
    else:
        print(array[rowIdx][colIdx])

#accessEle(new2DArray, 1, 2)

#Traversing a 2d Array
def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

#traverseArray(new2DArray)

#Linear Search
def linearSearch(array, element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == element:
                return 'found at index :' +str(i)+" "+str(j)
    return 'Element not found'
                
#print(linearSearch(new2DArray, 6))

#Deleting an element/column/row
newArray = np.delete(new2DArray, 0, axis=0)
#print(new2DArray)
#print(newArray)

