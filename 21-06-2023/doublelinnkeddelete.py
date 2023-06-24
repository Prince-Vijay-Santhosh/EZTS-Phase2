class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class singlell:
    def __init__(self):
        self.head=None
    def deletatbegin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def deletatbeginr(self):
        temp=self.head
        while temp.next:
                temp=temp.next
        t=temp.prev
        p=temp
        while t:
                t=t.prev
                p=p.prev
        p.prev=None
    def deleteatend(self):
        temp=self.head.next
        p=self.head
        while temp.next is not None:
            temp=temp.next
            p=p.next
        p.next=None
        temp.prev=None
    def deleteatpos(self,pos):
        temp=self.head.next
        p=self.head
        for i in range(1,pos-1):
            temp=temp.next
            p=p.next
        p.next=temp.next
        temp.next.prev=p
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("<->",end=" ")
                temp=temp.next
    def reverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp.next:
                   temp=temp.next
            while temp:
                print(temp.data,end=" ")
                if temp.prev!=None:
                    print("<->",end=" ")
                temp=temp.prev
                
obj=singlell()
n=node(10)
obj.head=n
n1=node(20)
n.next=n1
n1.prev=n
n2=node(30)
n1.next=n2
n2.prev=n1
n3=node(40)
n2.next=n3
n3.prev=n2
n4=node(50)
n3.next=n4
n4.prev=n3
n5=node(60)
n4.next=n5
n5.prev=n4
obj.display()
print("\n")
obj.reverse()
print("\ndelete at beginning")
obj.deletatbegin()
obj.display()
print("\n")
obj.deletatbeginr()
obj.reverse()
print("\n delete at end")
obj.deleteatend()
obj.display()
print("\n")
obj.reverse()
print("\ndelete at pos")
n=int(input("enter position to delete"))
obj.deleteatpos(n)
obj.display()
print("\n")
obj.reverse()


