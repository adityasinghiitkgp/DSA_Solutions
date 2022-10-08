def solve(n,dp):
    mod=(10**9)+7
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+(i-1)*dp[i-2])%mod

    return dp[n]
    
    
    
class Solution:
    def countFriendsPairings(self, n):
        dp=[0 for i in range(n+1)]
        
        dp[0]=0
        dp[1]=1
        if n>1:
            dp[2]=2
        return solve(n,dp)