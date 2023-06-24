class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell:
    def __init__(self):
        self.head=None
        self.last=None
    def append(self,data):
        if self.last is None:
            self.head=node(data)
            self.last=self.head
        else:
            self.last.next=node(data)
            self.last=self.last.next
    def display(self):
        current=self.head
        while  current is not None:
            print(current.data,end=" ")
            current=current.next
       
obj=singlell()
n=int(input("how many elements you would like to insert"))
for i in range(n):
    data=int(input("Enter data"))
    obj.append(data)
print("the linked list:",end=" ")
obj.display()