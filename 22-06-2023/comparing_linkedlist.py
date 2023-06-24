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
class singlell2:
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
       
obj=singlell()
obj2=singlell1()
n=int(input("how many elements you would like to insert in 1"))
for i in range(n):
    data=int(input("Enter data"))
    obj.append(data)
print("the linked list:",end=" ")
obj.display()
n=int(input("how many elements you would like to insert in 1"))
for i in range(n):
    data=int(input("Enter data"))
    obj.append(data)
print("the linked list:",end=" ")
obj.display()
                                  
