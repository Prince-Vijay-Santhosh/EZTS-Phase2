class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
def inorder(root):
    current=root
    stack=[]
    done=0
    while(1):
        #reach the left most node
        if current is not None:
            stack.append(current)
            current=current.left
        elif (stack):
            current=stack.pop()
            print(current.data,end=" ")
            current=current.right
        else:
            break
    print()
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