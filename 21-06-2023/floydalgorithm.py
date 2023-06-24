#findinngloop in single linked list and removing it
class  node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,newdata):
        newnode=node(newdata)
        newnode.next=self.head
        self.head=newnode
    def detectandremoveloop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        slow=self.head
        fast=self.head
        while(slow and fast and fast.next):
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    print("meeting point",slow.data)
                    slow=self.head
                    while (slow.next!=fast.next):
                      slow=slow.next
                      fast=fast.next
                    print("start of loop",fast.next.data)
                    fast.next=None
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
obj=linkedlist()
obj.head=node(50)
obj.head.next=node(20)
obj.head.next.next=node(5)
obj.head.next.next.next=node(15)
obj.head.next.next.next.next=node(10)
extra=node(1)
obj.head.next.next.next.next.next=extra
extra.next=obj.head.next
obj.detectandremoveloop()
print("linked list after removing loop")
obj.display()