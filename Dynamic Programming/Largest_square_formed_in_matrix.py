def maxSquare(self, n, m, mat):
    
    dp=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        if mat[i][m-1]==1:
            dp[i][m-1]=1
    
    for i in range(m):
        if mat[n-1][i]==1:
            dp[n-1][i]=1
        
    for i in range(n-2,-1,-1):
        for j in range(m-2,-1,-1):
            if mat[i][j]!=0:
                dp[i][j]=1+min(dp[i+1][j],dp[i+1][j+1],dp[i][j+1])
                
    mn=0        
    for i in range(n):
        if mn<max(dp[i]):
            mn=max(dp[i])
    return mn