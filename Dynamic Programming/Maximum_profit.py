def maxProfit(self, K, N, A):
    dp=[[0 for i in range(N+1)] for j in range(K+1)]
    
    for i in range(1,K+1):
        profit_past_days=-10**99
        for j in range(1,N):
            profit_past_days=max(profit_past_days,dp[i-1][j-1]-A[j-1])
            dp[i][j]=max(dp[i][j-1],profit_past_days+A[j])
            
    return dp[K][N-1]