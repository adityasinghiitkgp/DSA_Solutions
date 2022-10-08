

def solve(arr,i,j,dp):
    if i>=j:
        return 0
        
    elif dp[i][j]!=-1:
        return dp[i][j]
    mn=10**99  
    for k in range(i,j):
        temp=solve(arr,i,k,dp)+solve(arr,k+1,j,dp)+(arr[i-1]*arr[k]*arr[j])
        mn=min(temp,mn)
        dp[i][j]=mn
        
    return dp[i][j]
        

class Solution:
    def matrixMultiplication(self, N, arr):
        dp=[[-1 for i in range(N)]for j in range(N)]

        i=1
        j=len(arr)-1
        return solve(arr,i,j,dp)