def LongestRepeatingSubsequence(self, A):
    n=len(A)
    dp=[[0 for i in range(n+1)]for j in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if A[i-1]==A[j-1] and i!=j:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[n][n]