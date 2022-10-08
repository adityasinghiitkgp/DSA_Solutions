def kthSmallest(mat, n, k): 
    dp=[]
    for i in range(n):
        for j in range(n):
            dp.append(mat[i][j])
    dp.sort()
    return dp[k-1]