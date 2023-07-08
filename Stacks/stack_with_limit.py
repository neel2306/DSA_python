 
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
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
        
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    def push(self, value):
        if self.isFull():
            return "Stack is full"
        else:
            self.list.append(value)
            return "Added element {} to the stack".format(value)
    
    def pop(self):
        if self.isEmpty():
            return 'Nothing to return'
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "No element in stack"
        else:
            return self.list[-1]
    
    def deleteStack(self):
        self.list = None
    

customStack = Stack(4)
print(customStack.isEmpty())
customStack.push(0)
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.isFull())
