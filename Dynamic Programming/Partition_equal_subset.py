def equalPartition(self, N, arr):
    sumi=sum(arr)
    if sumi%2!=0:
        return False
    sumi=sumi//2
    dp=[[0 for i in range(sumi+1)]for j in range(len(arr)+1)]
    for i in range(len(arr)+1):
        for j in range(sumi+1):
            if i==0 and j==0:
                dp[i][j]=True
            elif i==0:
                dp[i][j]=False
            elif j==0:
                dp[i][j]=True
            elif arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    if dp[len(arr)][sumi]:
        return  True
    return False
