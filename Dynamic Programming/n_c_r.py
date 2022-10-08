def nCr(self, n, r):
    dp=[0]*(r+1)
    
    dp[0]=1
    for i in range(1,n+1):
        j=min(i,r)
        while j>0:
            dp[j]=(dp[j]+dp[j-1])%(1000000007)
            j-=1
    return dp[-1]