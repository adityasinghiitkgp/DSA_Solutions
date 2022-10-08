def minimumCost(self, cost, N, W):
    
    dp=[[-1 for i in range(W+1)] for j in range(N+1)]
    
    for i in range(N+1):
        for j in range(W+1):
            if i==0:
                dp[i][j]=10**99
            elif j==0:
                dp[i][j]=0
            elif i<=j and cost[i-1]!=-1:
                dp[i][j]=min(cost[i-1]+dp[i][j-i],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
                
    if dp[N][W]==10**99:
        return -1
        
    else:
        return dp[N][W]
