class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell:
    def __init__(self):
        self.head=None
    def insertatbegin(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def deleteatbegin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def deleteatend(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
        #while temp.next!=None :
            temp=temp.next
            prev=prev.next
        prev.next=None
    def deleteatpos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("->",end=" ")
                temp=temp.next
                
obj=singlell()
n=node(10)
obj.head=n
n1=node(20)
n.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
n5=node(60)
n4.next=n5
obj.display()
print("after inserting at beginning\n")
obj.insertatbegin(100)
obj.display()
print("\ndelete at begginning")
obj.deleteatbegin()
obj.display()
print("\ndelete at end")
obj.deleteatend()
obj.display()
print("\ndeletion at given position")
obj.deleteatpos(3)
obj.display()

