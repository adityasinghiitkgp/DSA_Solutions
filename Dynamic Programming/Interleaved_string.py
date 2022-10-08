def lcs(n,m,l,s1,s2,C):

    dp=[[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 and j==0:
                dp[i][j]=1
                
            elif s1[j-1]==C[i+j-1] and s2[i-1]==C[i+j-1]:
                dp[i][j]=dp[i][j-1] or dp[i-1][j]
                
            elif s1[j-1]==C[i+j-1]:
                dp[i][j]=dp[i][j-1]
                
            elif s2[i-1]==C[i+j-1]:
                dp[i][j]=dp[i-1][j]
                
    return dp[m][n]
    
class Solution:
    
    def isInterleave(self,A, B, C):
        n=len(A)
        m=len(B)
        l=len(C)
        if (len(A)+len(B))!=len(C):
            return False
        return lcs(n,m,l,A,B,C)