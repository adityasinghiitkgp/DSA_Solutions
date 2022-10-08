def isBipartite(self, V, adj):
    color=[-1]*V
    
    lis=[]
    for i in range(V):
        if color[i]==-1:
            lis.append(i)
            color[i]=1
            while lis:
                x=lis.pop()
        
                for i in adj[x]:
                    if i==x:
                        return False
                    if color[i]==-1:
                        color[i]=1-color[x]
                        lis.append(i)
                    if color[i]==color[x]:
                        return False
    return True