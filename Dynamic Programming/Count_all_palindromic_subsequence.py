def countPs(self,string):
    n= len(string)
    dp=[[0 for i in range(n)] for i in range(n)]
    for i in range(n-1,-1,-1):
        dp[i][i]=1
        for j in range(i+1,n):
            
            if string[i]==string[j] :
                dp[i][j]= (dp[i][j-1] + dp[i+1][j]+1)%1000000007
            else:
                dp[i][j]=(dp[i][j-1]+dp[i+1][j]-dp[i+1][j-1])%1000000007
                
    return dp[0][n-1]
                    