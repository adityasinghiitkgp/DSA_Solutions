def isNegativeWeightCycle(self, n, edges):
    dist=[10*99]*n
    dist[0]=0
    for i in range(len(edges)):
        u=edges[i][0]
        v=edges[i][1]
        w=edges[i][2]
        if dist[v]>dist[u]+w:
            dist[v]=dist[u]+w
    for i in range(len(edges)):
        u=edges[i][0]
        v=edges[i][1]
        w=edges[i][2]
        if dist[v]>dist[u]+w:
            return 1
    return 0