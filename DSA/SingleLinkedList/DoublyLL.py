class Node:
    def __init__(self,value=None):
        self.data = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        else:
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
            temp.prev = t1
    
    def insertAtBegin(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def insertAtMid(self, value, x):
        t = self.head
        while t.next != None:
            if t.data == x:
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def deleteNode(self, value):
        temp = Node(value)
        t = self.head
        if(self.head == None):
            return "List is empty"
        # Deletion from beginning
        if t.data == value:
            self.head = t.next
            self.head.prev = None
            return        
        while t.next != None:
            # Deletion in between 
            if t.data == value:
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next
        # Deletion at end
        if t.data == value:
            t.prev.next = None

    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data, end=" <--> ")
            t1 = t1.next
        print(t1.data)

obj = DoublyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBegin(5)
obj.insertAtMid(50,20)
obj.deleteNode(40)
obj.printLL()