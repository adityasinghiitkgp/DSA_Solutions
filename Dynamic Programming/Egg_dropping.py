def solve(e,f,dp):
    if e==1 or f==0 or f==1:
        return f
        
    elif dp[e][f]!=-1:
        return dp[e][f]
        
    mn=10*99    
    for k in range(1,f):
        temp=1+max(solve(e,f-k,dp),solve(e-1,k-1,dp))
        if mn>temp:
            mn=temp
        dp[e][f]=mn
    
    return mn
    
class Solution:
    def eggDrop(self,n, k):
        dp=[[-1 for i in range(k+1)]for j in range(n+1)]
        e=n
        f=k
        return solve(e,f,dp)