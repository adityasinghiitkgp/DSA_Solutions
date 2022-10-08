
def solve(arr,i,j,dp):
    if i>=j:
        return 0

    elif dp[i][j]!=-1:
        return dp[i][j]
 
    temp1= arr[i]+ min(solve(arr,i+1,j-1,dp),solve(arr,i+2,j,dp))
    temp2=arr[j]+ min(solve(arr,i+1,j-1,dp),solve(arr,i,j-2,dp))
    dp[i][j]=max(temp1,temp2)
   
    return dp[i][j]
        
        

class Solution:
    def optimalStrategyOfGame(self,arr, n):
        dp=[[-1 for i in range(n+1)]for j in range(n+1)]
        i=0
        j=n-1
        return solve(arr,i,j,dp)
