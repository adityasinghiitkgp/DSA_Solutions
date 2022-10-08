from collections import defaultdict
def dfs(i,d,visited,connections):
    visited[i]=True
    if i in d.keys():
        for j in d[i]:
            if visited[j]==False:
                dfs(j,d,visited,connections)

            
def solve(n,connections,m):
    d=defaultdict(list)
    for i in range(m):
        d[connections[i][0]].append(connections[i][1])
        d[connections[i][1]].append(connections[i][0])
    edges=m
    count=0
    visited=[False]*n
    for i in range(n):
        if visited[i]==False:
            dfs(i,d,visited,connections)
            count+=1
    
    extra=edges-((n-1)-(count-1))
    if extra>=count-1:
        return count-1
    return -1

class Solution:
    def makeConnected(self, n, connections):
        m=len(connections)
        return solve(n,connections,m)
        