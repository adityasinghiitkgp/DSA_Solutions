class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[0]*len(s) for i in range(len(s))]
        
        t=""
        for i in range(0,len(s)):
            dp[i][i]=1
        t=s[0]
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j] and (j-i==1 or dp[i+1][j-1]==1):
                    dp[i][j]=1
                    if len(t)<len(s[i:j+1]):
                        t=s[i:j+1]
        return t
        
        
            