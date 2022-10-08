def disarrange(self, N):
    m=(10**9)+7
    dp=[0 for i in range(N+1)]
    dp[1]=0
    dp[2]=1
    
    for i in range(3,N+1):
        dp[i]=((i-1)*(dp[i-1]+dp[i-2]))%m
        
    return dp[N]