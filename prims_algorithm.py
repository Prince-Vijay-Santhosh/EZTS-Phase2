graph={'A':[(1,'B'),(3,'E')],'B':[(2,'E'),(1,'D'),(4,'C'),(1,'A')],'C':[(4,'B'),(1,'D')],'D':[(1,'B'),(1,'C'),(2,'E')],'E':[(2,'B'),(2,'D'),(3,'A')]}
#bfs we use queue
import heapq
def prims(graph,start):
    parent={}
    weights={}
    queue=[]
    visited=set()
    for vertex in graph:
        weights[vertex]=9999
    weights[start]=0
    heapq.heappush(queue,(0,start))
    while len(queue)!=0:
        cur_weight,cur_node=heapq.heappop(queue)
        if cur_node in visited:
            continue
        for weight,node in graph[cur_node]:
            if node not in visited and weight <weights[node]:
                weights[node]=weight
                parent[node]=cur_node
                heapq.heappush(queue,(weight,node))
            visited.add(cur_node)
    print(weights)
prims(graph,'A')