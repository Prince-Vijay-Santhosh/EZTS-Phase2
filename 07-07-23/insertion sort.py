n=int(input("enter size of array"))
l=[]
for i in range(n):
    i=int(input())
    l.append(i)
print("array before sorting")
print(l)
for i in range(1,n):
    j=i
    while l[j-1]>l[j] and j>0:
        l[j-1],l[j]=l[j],l[j-1]
        j=j-1
print("array after sorting")
print(l)