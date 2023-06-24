from queue import Queue
s=Queue(maxsize=3)
print("the size of queue before enqueue any element",s.qsize())#
s.put('a')
s.put('b')
s.put('c')
print("size of queue after enqueuing element into queue:   ",s.qsize())
print("returns true if queue is full else flase     ",s.full())
print("element popped" ,s.get())
print("element popped" ,s.get())
print("elment popped ",s.get())
print(s.empty())
print(type(s))
