def match(self,pat,string):
    n=len(string)
    m=len(pat)
    dp=[[False]*(m+1) for i in range(n+1)]
    
    dp[0][0]=True
    
    for i in range(1,m):
        if pat[i-1]=="*":
            dp[0][i]=dp[0][i-1]
            
    for i in range(1,n+1):
        for j in range(1,m+1):
            if pat[j-1]=="?" or pat[j-1]==string[i-1]:
                dp[i][j]=dp[i-1][j-1]
                
            elif pat[j-1]=="*":
                dp[i][j]=dp[i][j-1] or dp[i-1][j]
                
            else:
                dp[i][j]=False
    return dp[n][m]