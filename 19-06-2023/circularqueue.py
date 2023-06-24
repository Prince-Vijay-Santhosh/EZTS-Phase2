class Circularqueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,data):
        #CONDITION IF QUEUE IS FULL
        if((self.rear+1)%self.size==self.front):
            print("Queue is Full")
        # QUEUE IS EMPTY
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
            #ADD ELEMENT ALWAYS AT TAIL PLACE
        else:
            #NEXT POSITION AT REAR
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear] = data
    def dequeue(self):
        if(self.front==-1):
            print("Queue is empty")
            #CONDITION FOR EMPTY QUEUE
        elif (self.front==self.rear):
            temp=self.queue[self.front]
            self.front=self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        #CONDITION FOR EMPTY QUEUE
        if(self.front==-1):
            print("Queue is Empty")
        elif(self.rear>=self.front):
            print("Elements in the circular Queue",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        else:
            print("Elements in queue",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        if((self.rear+1)%self.size==self.front):
            print("Queue is full")
ob=Circularqueue(5)
ob.enqueue(14)
ob.enqueue(20)
ob.enqueue(10)
ob.enqueue(-6)
ob.display()
print("Delete value: ",ob.dequeue())
print("Delete value: ",ob.dequeue())
ob.display()





