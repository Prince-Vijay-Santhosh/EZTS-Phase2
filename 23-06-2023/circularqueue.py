class circularqueue():
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,data):
        #condition if queue is full
        if((self.rear+1)%self.size==self.front):
            print("queue is full")
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if(self.front==-1):
            print("queue is empty\n")
        elif(self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front +1)%self.size
            return temp
    def display(self):
        if(self.front==-1):
            print("queue is empty")
        elif(self.rear>=self.front):
            print("element in the circular queue are ",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end="  ")
            print()
        else:
            print("Element  in circular queue are ",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        if((self.rear +1)%self.size ==self.front):
            print("queue is full")
obj=circularqueue(5)
obj.enqueue(14)
obj.enqueue(22)
obj.enqueue(13)
obj.enqueue(-2)
obj.display()
print("delted values",obj.dequeue())
print("delted values",obj.dequeue())
obj.enqueue(9)
obj.enqueue(20)
obj.display()
obj.enqueue(100)
obj.display()

            
            