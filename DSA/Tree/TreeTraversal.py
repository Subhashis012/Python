class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value


def preOrder(root):
    if root:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')

root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(8)

print("Preorder traversal:")
preOrder(root)  
print()
print("Inorder traversal:")
inOrder(root)   
print()
print("Postorder traversal:")
postOrder(root) 