def countBT (self, h):
    dp=[0]*(h+1)
    mod=(10**9)+7
    dp[0]=1
    dp[1]=1
    
    for i in range(2,h+1):
        dp[i]=(dp[i-1]*((2*dp[i-2])+dp[i-1]))%mod
        
    return dp[h]
