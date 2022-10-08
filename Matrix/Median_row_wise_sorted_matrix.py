def median(self, matrix, r, c):
    n=r*c
    mid=n//2
    dp=[]
    for i in range(r):
        for j in range(c):
            dp.append(matrix[i][j])
    dp.sort()
    return dp[mid]