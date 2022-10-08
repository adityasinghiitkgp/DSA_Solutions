def maxProfit(self,n,price):
    arr=price
    dp=[0]*n
    maxi=arr[n-1]
    mini=arr[0]
    for i in range(n-2,-1,-1):
        if arr[i]>maxi:
            maxi=arr[i]
        dp[i]=max(dp[i+1],maxi-arr[i])
    for i in range(1,n):
        if arr[i]<mini:
            mini=arr[i]
        dp[i]=max(dp[i-1],dp[i]+(arr[i]-mini))
    return dp[n-1]
