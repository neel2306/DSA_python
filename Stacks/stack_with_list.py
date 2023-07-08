#Creating a stack with list.

class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)
        return "Element has been added to the stack"
    
    def pop(self):
        if self.isEmpty():
            return "Stack does not exist"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack does not exist"
        else:
            return self.list[-1]

    def deleteStack(self):
        if self.isEmpty():
            return "Stack does not exist"
        else:
            if (input('Do you want to delete the stack?').upper()) == 'Y':
                self.list = None



customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(5)
print(customStack.peek())