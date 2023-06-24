class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlylinked:
    def __init__(self):
        self.head=None
        self.lastnode=None
    def append(self,data):
        if self.lastnode is None:
            self.head=Node(data)
            self.lastnode=self.head
        else:
            self.lastnode.next=Node(data)
            self.lastnode=self.lastnode.next
    def display(self):
        curr=self.head
        while curr is not None:
            print(curr.data,end=" ")
            curr=curr.next
    def compare(self):
        pass

a=singlylinked()
n= int(input("Enter no of nodes you want to insert: "))
for i in range(n):
    data=int(input("Enter the node"+ str(i+1)+" "))
    a.append(data)
print("The list is: ",end=" ")
a.display()
b=singlylinked()
n= int(input("\nEnter no of nodes you want to insert: "))
for i in range(n):
    data=int(input("Enter the node"+ str(i+1)+" "))
    b.append(data)
print("The list is: ",end=" ")
b.display()
a.compare(b)



