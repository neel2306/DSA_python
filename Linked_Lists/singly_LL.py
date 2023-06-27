
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

#Linked list with 2 nodes.
sLL = SingleLinkedList()
node1 = Node(1)
node2 = Node(2)

sLL.head = node1
sLL.head.next = node2
sLL.tail = node2

