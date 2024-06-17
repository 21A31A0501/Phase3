def BFS(start,graph):
    visited=[start]
    q=[start]
    while len(q)!=0:
        ele=q.pop(0)
        for i in graph[ele]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    return visited
graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","E"],
    "D":["B","E"],
    "E":["C","D"]
}
res=BFS("B",graph)
print(res)
