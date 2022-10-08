
def solve(V,adj,visited,last_place,src,ans):
    visited[src]=True
    for i in adj[src]:
        if not visited[i]:
            last_place=solve(V,adj,visited,last_place,i,ans)
    ans[last_place]=src
    return last_place-1
    


class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        visited=[False]*V
        last_place=V-1
        ans=[0]*V
        for i in range(V):
            if not visited[i]:
                last_place=solve(V,adj,visited,last_place,i,ans)
        return ans