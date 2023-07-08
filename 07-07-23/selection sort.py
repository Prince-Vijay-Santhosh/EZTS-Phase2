n=int(input("enter size of array"))
l=[]
for i in range(n):
    i=int(input())
    l.append(i)
print("array before sorting")
print(l)
for i in range(n):
    mini=i    #initial value
    for j in range(i+1,n):
        if l[mini]>l[j]:
            mini=j     #finding the min element index
    l[i],l[mini]=l[mini],l[i]
print("array after sorting")
print(l)
            
