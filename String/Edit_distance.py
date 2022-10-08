def editDistance(self, s, t):
    n=len(s)
    m=len(t)
    dp=[[0 for i in range(m+1)]for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if i==0 and j==0:
                dp[i][j]=0
            elif i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif s[i-1]!=t[j-1]:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
            else:
                dp[i][j]=dp[i-1][j-1]
    return dp[n][m]
