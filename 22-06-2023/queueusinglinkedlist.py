class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.head is None:
            self.head=node(data)
            self.last=self.head
        else:
          self.last.next=node(data)
          self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            print("stack is empty")
        else:
            popped=self.head.data
            self.head=self.head.next
            print("removed elemnt is",popped)
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
     
obj=queue()
while(1):
    ch=int(input("\nenter ur choice 1.enqueue 2.dequeue 3.display 4.exit\n"))
    if(ch==1):
        n=int(input("enter element"))
        obj.enqueue(n)
    elif(ch==2):
       obj.dequeue()
    elif(ch==3):
        obj.display()
    elif(ch==4):
        break
    else:
        print("enter given choices only")
        
