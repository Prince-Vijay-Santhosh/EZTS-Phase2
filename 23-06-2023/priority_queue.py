s=[]
s.append((3,"harsha"))
s.append((1,"abhi"))
s.append((4,"varsha"))
s.append((2,"akash"))
print("Queue according to priority\n")
s.sort(reverse=True)
print(s)
print("\norignal queue")
while s:
    print(s.pop())