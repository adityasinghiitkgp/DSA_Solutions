def maxChainLen(Parr, n):
        lis=[]
        for i in Parr:
            lis.append([i.a,i.b])
        

        lis.sort()
       
        dp=[1]*n
        maxi=0
        for i in range(1, n):
            for j in range(0, i):
                if (lis[i][0] > lis[j][1] and
                      dp[i] < dp[j] + 1):
                    dp[i] = dp[j] + 1
 
                    
        for i in range(n):
            if dp[i]>maxi:
                maxi=dp[i]
        return maxi

        