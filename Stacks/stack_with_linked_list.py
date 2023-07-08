
class Node:
    def __init__(self, value=None):
        self.value = value
        self .next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head #Changing the next reference of the node to point to the next node in the linked list
        self.LinkedList.head = node #Head pointing to the current node.
    
    def pop(self):
        if self.isEmpty():
            return "No element in stack"
        else:
            nodeValue = self.LinkedList.head.value #First node in the linked list
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
    
    def peek(self):
        if self.isEmpty():
            return "No element in stack"
        else:
            nodeValue = self.LinkedList.head.value #First node in the linked list
            return nodeValue
    
    def deleteStack(self):
        self.LinkedList.head = None


    
customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(5)
print(customStack)
print('*'*30)
customStack.pop()
print(customStack)
print('*'*30)
print(customStack.peek())
print('*'*30)
customStack.deleteStack()
print(customStack)
