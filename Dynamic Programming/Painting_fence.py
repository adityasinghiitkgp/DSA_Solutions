

def solve(dp,n,k):
    md=1000000007
    diff=dp[1]
    for i in range(2,n+1):
        
        same=diff
      
        diff=dp[i-1]*(k-1)
        
        
        dp[i]=(same+diff)%md
    
    return dp[n]
        
class Solution:
    def countWays(self,n,k):
        dp=[0 for i in range(n+1)]
        dp[0]=0
        dp[1]=k
        
        return solve(dp,n,k)