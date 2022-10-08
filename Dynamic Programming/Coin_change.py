def count(self, S, m, n): 
    s=sorted(S)
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(m):
        for j in range(s[i],n+1):
            dp[j]+=dp[j-s[i]]
    return dp[-1]
            
