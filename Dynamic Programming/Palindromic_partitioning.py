
def palindrome(string):
    x=string[-1::-1]
    for i in range(len(x)):
        if x[i]!=string[i]:
            return False
    return True
    
def partition(string,i,j,dp):
    if i>=j:
        return 0
    elif palindrome(string[i:j+1]):
        return 0
        
    elif dp[i][j]!=-1:
        return dp[i][j]
        
    mn=10**9
    for k in range(i,j):
        if palindrome(string[i:k+1]):
            right=partition(string,k+1,j,dp)
        else:
            dp[i][k]=0
    
        temp=1+right
        mn=min(mn,temp)
        dp[i][j]=mn
        
    return dp[i][j]
        

class Solution:
    def palindromicPartition(self, string):
        dp=[[-1 for i in range(len(string))]for j in range(len(string))]
        i=0
        j=len(string)-1
        return partition(string,i,j,dp)