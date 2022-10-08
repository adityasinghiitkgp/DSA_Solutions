def solve(visited,V,adj,arr,src):
    visited[src]=True
    arr[src]=True
    for i in adj[src]:
        if not visited[i]:
            if solve(visited,V,adj,arr,i):
                return True
        else:
            if arr[i]==True:
                return True
    arr[src]=False
    return False

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited=[False]*(V)
        arr=[False]*V
        for i in range(V):
            if not visited[i]:
                if solve(visited,V,adj,arr,i):
                    return True
        return False