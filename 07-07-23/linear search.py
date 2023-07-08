n=int(input())
l=[1,2,3,4,5]
c=False
for i in range(len(l)):
    if l[i]==n:
        print("element found at position",i)
        break
if c==False:1
    print("element not found")