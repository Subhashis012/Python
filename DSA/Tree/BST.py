class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):
    if root == None:
        return Node(value)
    if value == root.data:
        return root
    if root.data > value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root == None:
        return "Element not found"
    if value == root.data:
        return "Element found"
    if root.data > value:
        root.left = search(root.left, value)
    else:
        root.right = search(root.right, value)
    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

# root = Node(20)
# root.left = Node(15)
# root.right = Node(30)
# root.left.left = Node(12)
# root.left.right = Node(18)
# inOrder(root)

root = insert(None, 20)
insert(root, 15)
insert(root, 30)
insert(root, 12)
insert(root, 18)
inOrder(root)
print()
print(search(root, 18))