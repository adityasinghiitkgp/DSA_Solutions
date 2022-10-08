def maximizeTheCuts(self,n,x,y,z):
    arr=[]
    arr.append(x)
    arr.append(y)
    arr.append(z)
    
    lenght=n
    
    dp=[[-1 for i in range(lenght+1)]for j in range(len(arr)+1)]

    for i in range(len(arr)+1):
        for j in range(lenght+1):
            if i==0:
                dp[i][j]=-10**99
            elif j==0:
                dp[i][j]=0
                
            
            elif arr[i-1]<=j:
                
                
                dp[i][j]= max(1+dp[i][j-arr[i-1]] ,dp[i-1][j]) 
            else:
                dp[i][j]=dp[i-1][j]

    if dp[3][n]<0:
        return 0
    return dp[3][n]