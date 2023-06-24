n=int(input("Enter size of array"))
l=[]
for i in range(n):
    i=int(input())
    l.append(i)
print(l)
while(1):
    print("enter ur choice")
    print("1 insert")
    print("2 delete")
    print("3.search")
    print("4.sort")
    print("5.exit")
    ch=int(input())
    if(ch==1):
        s=int(input("enter how many element to insert"))
        for i in range(s):
           a=int(input("Enter num"))
           l.append(a)
        print(l)
    elif(ch==2):
        s=int(input("enter how many element to delete"))
        for i in range(s):
            print("enter which pos element to delete")
            b=int(input())
            del(l[b])
        print(l)
    elif(ch==3):
        print("enter element to search")
        s=int(input())
        for i in range(len(l)):
            if(s==l[i]):
                print(l[i],"pos found at",i)
                break
            else:
                print("element not fount")
        print(l)
    elif(ch==4):
        print(sorted(l))
        print(l)
    if(ch==5):
        exit(0)
    else:
        print("invalid choice")