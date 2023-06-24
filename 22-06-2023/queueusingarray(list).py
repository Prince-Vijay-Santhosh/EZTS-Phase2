queue=[]
def enqueue():
    n=int(input("Enter an element"))
    queue.append(n)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("removed elemnt is ",e)
def display():
    if not queue:
        print("queue is empty")
    else:
        print("the elment in the queue are:",queue)
def seak():
    n=int(input("enter elment to search"))
    c=0
    for i in range(len(queue)):
        if(n==queue[i]):
            c+=1
    if(c>=1):
        print(n,"element found at pos",i,)
    else:
        print("not found")
while(1):
    print("1.enqueue  2.dequeue 3.display  4.seak  5.exit")
    ch=int(input("Enter ur choice"))
    if(ch==1):
        enqueue()
    if(ch==2):
        dequeue()
    if(ch==3):
        display()
    if(ch==4):
        seak()
    if(ch==5):
        break
    else:
        print("enter only given choices")
