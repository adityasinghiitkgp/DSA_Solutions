def safe(graph,k,V,color,c,v):
    for i in range(V):
        if graph[v][i]==1 and color[i]==c:
            return False
    return True
def solve(graph,k,V,color,v):
    if v==V:
        return True
    for c in range(1,k+1):
        if safe(graph,k,V,color,c,v):
            color[v]=c
            if solve(graph,k,V,color,v+1):
                return True
        color[v]=0
    return False
def graphColoring(graph, k, V):
    color=[0]*V
    return solve(graph,k,V,color,0)