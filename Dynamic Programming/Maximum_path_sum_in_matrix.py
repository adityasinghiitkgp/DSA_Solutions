def maximumPath(self, N, Matrix):
    
    dp=[[0 for i in range(N)]for j in range(N)]
    for row in range(N-1,-1,-1):
        for col in range(N):
            
            if row==N-1:
                down=0
            else:
                down=dp[row+1][col]
                
            if row==N-1 or col==0:
                left=0
            else:
                left=dp[row+1][col-1]
            
            if row==N-1 or col==N-1:
                right=0
            else:
                right=dp[row+1][col+1]
                
            dp[row][col]=Matrix[row][col]+max(down,left,right)
    
    return max(dp[0])