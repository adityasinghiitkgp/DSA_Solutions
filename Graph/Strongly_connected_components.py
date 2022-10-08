from collections import defaultdict

def topolo(V,adj,visited,src,topo):
    visited[src]=True
    for i in adj[src]:
        if not visited[i]:
            topolo(V,adj,visited,i,topo)
    topo.append(src)

def rev(V,adj,d):
    for i in range(len(adj)):
        for j in adj[i]:
            d[j].append(i)
            

def dfs(visited,d,x):
    visited[x]=True
    for i in d[x]:
        if not visited[i]:
            dfs(visited,d,i)
    
class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        topo=[]
        visited=[False]*V
        for i in range(V):
            if not visited[i]:
                topolo(V,adj,visited,i,topo)
        
        d=defaultdict(list)
        rev(V,adj,d)
        visited=[False]*V
        count=0
        while topo:
            x=topo.pop()
            if not visited[x]:
                dfs(visited,d,x)
                count+=1
        return count