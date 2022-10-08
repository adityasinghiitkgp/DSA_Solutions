def maxSumIS(self, Arr, n):
    dp=[0]*n
    dp[0]=Arr[0]
    for i in range(1,n):
        dp[i]=Arr[i]
        for j in range(i):
            if Arr[j]<Arr[i] and dp[i]<dp[j]+Arr[i]:
                dp[i]=dp[j]+Arr[i]

    
    return max(dp)