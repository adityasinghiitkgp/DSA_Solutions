def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
    dp=[0]*N
    arr.sort()
    for i in range(1,N):
        
        dp[i]=dp[i-1]
        
        if arr[i]-arr[i-1]<K:
            if i>=2:
                dp[i]=max(dp[i],arr[i]+arr[i-1]+dp[i-2])
            else:
                dp[i]=max(dp[i],arr[i-1]+arr[i])
    return dp[N-1]