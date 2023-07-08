n=int(input("enter size of array"))
l=[]
for i in range(n):
    i=int(input())
    l.append(i)
print("array before sorting")
print(l)
for i in range(n-1):
    swap=False
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            swap=True
            l[j],l[j+1]=l[j+1],l[j]
    if swap==False:
        break
print("array after sorting")
print(l)
            