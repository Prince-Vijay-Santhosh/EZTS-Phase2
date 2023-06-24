from queue import LifoQueue
s=LifoQueue(maxsize=3)
print("the size of stack before push any element",s.qsize())#
s.put('a')
s.put('b')
s.put('c')
print("size of stack after push element into stack:   ",s.qsize())
print("returns true if stack is full else flase",s.full())
print("element popped" ,s.get())
print("element popped" ,s.get())
print("elment popped ",s.get())
print(s.empty())
print(type(s))