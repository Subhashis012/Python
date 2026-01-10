class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, value):
        self.items.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            return self.items.pop(0)
        
    def display(self):
        return self.items
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.display())