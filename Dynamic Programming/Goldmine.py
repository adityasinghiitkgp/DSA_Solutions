def maxGold(self, n, m, M):
    dp=[[0 for i in range(m)] for i in range(n)]
    
    for j in range(m-1,-1,-1):
        for i in range(n):
            
            if i==0 or j==m-1:
                left=0
            else:
                left=dp[i-1][j+1]
            
            if i==n-1 or j==m-1:
                right=0
            else:
                right=dp[i+1][j+1]
            
            if j==m-1:
                forword=0
            else:
                forword=dp[i][j+1]
                
            dp[i][j]=M[i][j]+max(forword,left,right)
    
    
    mn=dp[0][m-1]
    for i in range(n):
        if mn<dp[i][0]:
            mn=dp[i][0]
    return mn