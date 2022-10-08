def getCount(self, N):
    dp=[[0 for i in range(10)]for j in range(N+1)]
    num=[]
    num.append([0,8])
    num.append([1,2,4])
    num.append([2,1,3,5])
    num.append([3,2,6])
    num.append([4,1,7,5])
    num.append([5,2,4,6,8])
    num.append([6,3,5,9])
    num.append([7,4,8])
    num.append([8,7,5,9,0])
    num.append([9,8,6])
    for i in range(1,N+1):
        for j in range(10):
            if i==1:
                dp[i][j]=1
            
            else:
                for k in num[j]:
                    dp[i][j]+=dp[i-1][k]
                    
                    
    return sum(dp[N])