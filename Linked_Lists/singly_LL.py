
'''
Creating a single linked list.
'''
class Node:
    #Step2 : Creating a node
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        #Step1 ; Creating head and tail and intializing to null
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #Inserting in a linked list.
    def insertSLL(self, value, location):
        newNode = Node(value) #Making a new node
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: #Means we are inserting an element at the beginning of the LL
                newNode.next = self.head
                self.head = newNode
            elif location == -1: #Inserting an element at the end of the LL
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode 
            else:
                tempNode = self.head #Inserting in the middle
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
    
    #Traversing through a SLL
    def traverseList(self):
        if self.head is None:
            print('Single Linked List doesnt exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    #To search for an element.
    def searchList(self,element):
        if self.head is None:
            return 'Single Linked List does not exist'
        else:
            node = self.head
            while node is not None:
                if node.value == element:
                    return "Element exists: ", node.value
                node = node.next
            return 'Element does not exist'
        
    #Deleting a node
    def deleteNode(self, location):
        if self.head is None:
            print('Single LInked List does not exist')
        else:
            if location == 0: #Deleting first node in the SLL
                if self.head == self.tail: #If the SLL has only one node
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next #Changing head's reference to the next node.
            
            elif location == -1: #Deleting the last node
                if self.head == self.tail: #If the SLL has only one node
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else: #Deleting a node
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteList(self):
        if self.head is None:
            print('Single Linked List does not exist!')
        if (input('Do you really want to delete the list?').upper()) == "Y":
            self.head = None
            self.tail = None
            print('Deleted the list!')
'''
sLL = SingleLinkedList()
sLL.insertSLL(0,0)
sLL.insertSLL(1,-1)
sLL.insertSLL(2,-1)
sLL.insertSLL(3,-1)
sLL.insertSLL(4,-1)
sLL.insertSLL(5,-1)
sLL.insertSLL(7,-1)
sLL.traverseList()
sLL.deleteList()
sLL.traverseList()
'''
