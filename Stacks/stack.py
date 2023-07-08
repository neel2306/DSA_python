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

customStack = Stack()
print(customStack.isEmpty())
    