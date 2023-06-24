class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
def inorder(root):
      if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
def preorder(root):
     if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
       if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
root=node(100)
root.left=node(400)
root.right=node(500)
root.left.left=node(700)
root.left.right=node(600)
root.left.right.left=node(900)
root.right.left=node(800)
root.right.right=node(200)
root.right.right.left=node(300)
print("inorder")
inorder(root)
print("\npreorder")
preorder(root)
print("\npostoreder")
postorder(root)