class Stack:
    def __init__(self):
        self.s = []
    
    def length(self):
        return len(self.s)
    
    def push(self, value):
        self.s.append(value)   # O(1)

    def peek(self):
        if not self.s:
            raise Exception("Stack is empty")
        return self.s[-1]
    
    def pop(self):
        if not self.s:
            raise Exception("Stack is empty")
        return self.s.pop()    # O(1)

stk = Stack()
# stk.pop()
stk.push(10)
stk.push(20)
print(stk.peek())