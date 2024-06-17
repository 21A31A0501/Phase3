def DFS(start,graph,visited=None):     #-------stack
    if visited==None:
        visited=[]
    visited.append(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            DFS(neighbour,graph,visited)
    return visited
graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","E"],
    "D":["B","E"],
    "E":["C","D"]
}
res=DFS("A",graph)
print(res)