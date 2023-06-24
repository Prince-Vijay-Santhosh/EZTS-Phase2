class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=node(data)
        else:
            nb=node(data)
            nb.next=self.head
            self.head=nb
    def pop(self):
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
     def
     
obj=stack()
while(1):
    ch=int(input("\nenter ur choice 1.push 2.pop 3.display 4.exit\n"))
    if(ch==1):
        n=int(input("enter element"))
        obj.push(n)
    elif(ch==2):
       obj.pop()
    elif(ch==3):
        obj.display()
    elif(ch==4):
        break
    else:
        print("enter given choices only")
        