class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
def insert(root,key):
    if root is None:
        return node(key)
    else:
        if root.data==key:
            return root
        elif root.data<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def search(root,key):
    if root is None or root.data==key:
        return root
    if root.data <key:
        return search(root.right,key)
    return search(root.left,key)
def inorder(root):
      if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
r=node(100)
r=insert(r,70)
r=insert(r,50)
r=insert(r,60)
r=insert(r,9)
r=insert(r,-3)
inorder(r)
n=int(input("\nenter an elment to search:"))
n=search(r,n)
if n is not None:
    print("  found")
else:
    print(" not found")
