
def solve(m,n,ans,i,j,s):
    visited[i][j]=True
    x=[-1,1,0,0]
    y=[0,0,-1,1]
    if i==n-1 and j==n-1:
        ans.append(s)
        visited[i][j]=False
        return
        
    for k in range(4):
        newi=i+x[k]
        newj=j+y[k]
        if newi>=0 and newi<n and newj>=0 and newj<n and m[newi][newj]==1 and not visited[newi][newj]:
            if newi>i:
                solve(m,n,ans,newi,newj,s+"D")
            elif newi<i:
                solve(m,n,ans,newi,newj,s+"U")
            elif newj>j:
                solve(m,n,ans,newi,newj,s+"R")
            else:
                solve(m,n,ans,newi,newj,s+"L")
    visited[i][j]=False
 
            
class Solution:
    def findPath(self, m, n):
        ans=[]
        s=""
        global visited
        visited=[[False for i in range(n)]for j in range(n)]
        if m[0][0]==1:
           
            solve(m,n,ans,0,0,s)
        ans=sorted(ans)
        return ans
        