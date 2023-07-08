key=int(input())
l=[1,2,3,4,5]
l=sorted(l)
start=0
end=len(l)-1
c=False
while(start<=end):
    mid=(start+end)//2
    if l[mid]==key:
        print("element found at position",mid)
        c=True
        break
    elif key>l[mid]:
        start=mid+1
    elif key<l[mid]:
        end=mid-1
if c==False:
    print("element not found")
        
        
    
        
        