class Stack:

    def __init__(self):
        self.stack = []

    def empty(self):
        return not self.stack
    
    def top(self):
        if self.empty():
            return None
        return self.stack[-1]
    
    def pop(self):
        if self.empty():
            return None
        return self.stack.pop()

    def push(self,item):
        self.stack.append(item)
    
    def __repr__(self):
        return self.stack

stack = Stack()

print(stack.empty())
stack.push(10)
print(stack.empty())