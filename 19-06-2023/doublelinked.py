class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None
class dll:
    def __init__(self):
        self.head=None

    def insertatbegin(self):
        n=Node(900)
        temp=self.head
        temp.pre=n
        n.next=temp
        self.head=n
    def insertatend(self):
        n=Node(1000)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.pre=temp
    def insertpos(self,pos):
        n=Node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.pre=temp
        n.next=temp.next
        temp.next.pre=n
        temp.next=n

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
                if(temp.next==None):
                    break
            print(temp.data)

l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.pre=n1
n1.next=n2
n3=Node(300)
n2.next=n3
n3.pre=n2
l.insertatbegin()
l.insertatend()
l.insertpos(2)
l.display()

l=list(range(1,6))
n=int(input("n value"))
a=[]
for i in range(-n,-1):
    a.append(l[-n])
print(a)




