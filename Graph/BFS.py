def bfsOfGraph(self, V, adj):
    ans=[]
    lis=[]
    lis.append(0)
    visited=[False]*(V)
    while lis:
        x=lis.pop(0)
        
        ans.append(x)
        visited[x]=True
        for i in adj[x]:
            if not visited[i]:
                lis.append(i)
                visited[i]=True
    return ans
