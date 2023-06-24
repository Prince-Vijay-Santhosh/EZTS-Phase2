class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class singlell:
    def __init__(self):
        self.head=None
    def insertatbegin(self,data):
        new=node(data)
        temp=self.head
        temp.prev=new
        new.next=temp
        self.head=new
    def insertatend(self,data):
        new=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.prev=temp
    def insertatpos(self,pos):
        n=node(400)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
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
obj.reverse()
print("\ninsert at beggining")
obj.insertatbegin(10)
obj.display()
print("\n")
obj.reverse()
print("\ninsert at end")
obj.insertatend(20)
obj.display()
print("\n")
obj.reverse()
print("\ninsert at pos")
obj.insertatpos(2)
obj.display()
print("\n")
obj.reverse()


