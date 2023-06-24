stack=[]
n=int(input("enter stack size"))
for i in range(n):
    n=int(input("Enter an element"))
    stack.append(n)  
for i in stack:
    if(i%2==0):
        print("even numbers",i,end=" ")