def longestSubsequence(self, N, A):
    dp=[0]*N
    res=0
    
    
    for i in range(0,N):
        dp[i]=1
        for j in range(0,i):

            if abs(A[j]-A[i])==1:
                dp[i]=max(dp[i],dp[j]+1)
        res=max(res,dp[i])
            
    return res