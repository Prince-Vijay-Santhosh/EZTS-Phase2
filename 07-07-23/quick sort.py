n=int(input("enter size of array"))
l=[]
for i in range(n):
    i=int(input())
    l.append(i)
print("array before sorting")
print(l)
def quick_sort(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left_arr=[i for i in l if i<pivot]
    right_arr=[i for i in l if i>pivot]
    return quick_sort(left_arr)+[pivot]+quick_sort(right_arr)
ans=quick_sort(l)
print("array after sorting")
print(ans)
    
    

    