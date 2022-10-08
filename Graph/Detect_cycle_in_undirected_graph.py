
def solve(visited,adj,V,parent,src):
    visited[src]=True
    for i in adj[src]:
        if not visited[i]:
            if solve(visited,adj,V,src,i):
                return True
        else:
            if parent!=i:
                return True
    return False
class Solution:
    
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        visited=[False]*V
        for i in range(V):
            if not visited[i]:
                if solve(visited,adj,V,-1,i):
                    return True
        return False
