stack=[]
def push():
    n=int(input("Enter an element"))
    stack.append(n)
def popelement():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed elemnt is ",e)
def display():
    if not stack:
        print("stack is empty")
    else:
        print("the elment in the satck are:",stack)
def peak():
    if not stack:
        print("stack is empty")
    else:
        print("the top element of stack",stack[-1])
def seak():
    n=int(input("enter elment to search"))
    c=0
    for i in range(len(stack)):
        if(n==stack[i]):
            c+=1
    if(c>=1):
        print(n,"element found at pos",i,)
    else:
        print("not found")
while(1):
    print("1.push  2.pop 3.display 4.peak 5.seak  6.exit")
    ch=int(input("Enter ur choice"))
    if(ch==1):
        push()
    if(ch==2):
        popelement()
    if(ch==3):
        display()
    if(ch==4):
        peak()
    if(ch==5):
        seak()
    if(ch==6):
        break
    else:
        print("enter only given choices")