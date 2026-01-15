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

def get_successor(root):
    root = root.right
    while root and root.left:   # root != None and root.left != None
        root = root.left
    return root

def delete(root, value):
    if(root == None):
        return root
    if(root.data > value):
        root.left = delete(root.left, value)
    elif(root.data < value):
        root.right = delete(root.right, value)
    else:
        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left
        else:
            successor = get_successor(root)
            root.data = successor.data
            root.right = delete(root.right, successor.data)
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