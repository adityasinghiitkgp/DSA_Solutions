def longestSubsequence(self,a,n):
    lis=set(a)
    inc=sorted(list(lis))
    m=len(inc)
    dp=[[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if inc[i-1]==a[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]