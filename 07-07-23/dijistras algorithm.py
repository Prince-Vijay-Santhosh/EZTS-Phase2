import heapq
def dijkstras(graph,source):
    distance={}
    for vertex in graph:
        distance[vertex]=999
    distance[source]=0
    
    heap=[]
    heapq.heappush(heap,(0,source))
    while len(heap)!=0:
        cur_wt,cur_ver=heapq.heappop(heap)
        if cur_wt > distance[cur_ver]:
            continue
        for edge in graph[cur_ver]:
            travel_wt , node =edge
            cost=cur_wt+travel_wt
            if cost < distance[node]:
                distance[node]=cost
                heapq.heappush(heap,(cost,node))
    print(distance)     



graph = {
    'a':[(2,'b'),(4,'d')],
    'b':[(7,'c'),(1,'d')],
    'c':[(1,'f')],
    'd':[(3,'e'),(5,'f')],
    'e':[(2,'c'),(5,'f')],
    'f':[],
    }
ans=dijkstras(graph,'a')
print(ans)