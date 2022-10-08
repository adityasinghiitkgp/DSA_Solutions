def solve(V,adj,visited,ans,src):
    visited[src]=True
    ans.append(src)
    for i in adj[src]:
        if not visited[i]:
            solve(V,adj,visited,ans,i)
        
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited=[False]*V
        ans=[]
        solve(V,adj,visited,ans,0)
        return ans