stack=[]
n=int(input("enter size of stack"))
def push(): 
    for i in range(n):
     l=int(input("Enter an element"))
     stack.append(l)
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
        n=int(input("1.even 2.odd"))
        a=[]
        b=[]
        if(n==1):
          for i in stack:
              if(i%2==0):
                  a.append(i)
          print(a)
        elif (n==2):
            for i in stack:
                if(i%2!=0):
                    b.append(i)
            print(b)
while(1):
    print("1.push  2.pop 3.display   4.exit")
    ch=int(input("Enter ur choice"))
    if(ch==1):
        push()
    if(ch==2):
        popelement()
    if(ch==3):
        display()
    if(ch==4):
        break
    else:
        print("enter only given choices")
