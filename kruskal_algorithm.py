def kruskal(graph):
    edge_list=[]
    for source in graph:
        for edge in graph[source]:
            weight,dest=edge
            edge_list.append((weight,source,dest))
    edge_list.sort()
    parent={}
    for vertex in graph:
        parent[vertex]=vertex
    mst=[]
    def find_parent(vertex):
        if parent[vertex]!=vertex:
             parent[vertex]=find_parent(parent[vertex])
        return parent[vertex]
    #checking loop
    for edge in edge_list:
        weight,source,dest=edge
        if find_parent(source)!=find_parent(dest):
            mst.append(edge)
            parent[find_parent(source)]=find_parent(dest)
    return mst
                             #bfs we use queue
graph={'A':[(10,'F'),(28,'B')],
       'B':[(28,'A'),(16,'C'),(14,'G')],
       'C':[(14,'B'),(12,'D')],
       'D':[(18,'G'),(12,'C'),(22,'E')],
       'E':[(24,'G'),(22,'D'),(24,'F')],
       'F':[(10,'A'),(25,'E')],
        'G':[(18,'D'),(14,'B'),(25,'E')]}
mst=kruskal(graph)
print(mst,end="\n")