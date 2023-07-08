class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
def levelorder_traversal(root):
    queue=[root]
    while len(queue)!=0:
        ele=queue.pop(0)
        if len(queue)%2!=0:
            if ele.left!=None:
                queue.append(ele.left)
            if ele.right!=None:
                queue.append(ele.right)
            print(ele.data,end=" ")
        else:
            if ele.right!=None:
                queue.append(ele.right)
            if ele.left!=None:
                queue.append(ele.left)
            print(ele.data,end=" ")
        
root=node(100)
root.left=node(200)
root.right=node(300)
root.left.left=node(400)
root.left.right=node(500)
root.right.left=node(600)
root.right.right=node(700)

print("level----order----traversal:")
levelorder_traversal(root)