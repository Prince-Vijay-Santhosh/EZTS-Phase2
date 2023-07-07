class Node:
   def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=' ')
		inorder(root.right)
def insert(node, key):
    if node is None:
       return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
def minvalueNode(Node):
    curr=Node 
    while (curr.left is not None):
        curr = curr.left
    return curr

def deleteNode(root, key):
    if root is None:
        return root
    if root.key > key:
        root.left = deleteNode(root.left, key)
        return root
    elif root.key < key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root=None
            return temp
        elif root.right is None:
            temp = root.left
            root=None
            return temp
        temp=minvalueNode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Original BST: ", end='')
inorder(root)

print("\n\nDelete a Leaf Node: 20")
root = deleteNode(root, 20)
print("Modified BST tree after deleting Leaf Node:")
inorder(root)

print("\n\nDelete Node with single child: 70")
root = deleteNode(root, 70)
print("Modified BST tree after deleting single child Node:")
inorder(root)

print("\n\nDelete Node with both child: 50")
root = deleteNode(root, 50)
print("Modified BST tree after deleting both child Node:")
inorder(root)
