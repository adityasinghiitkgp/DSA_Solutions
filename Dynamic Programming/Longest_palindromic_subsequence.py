def longestPalinSubseq(self, S):
    rev=S
    rev=rev[-1::-1]
    dp=[[0 for i in range(len(S)+1)]for j in range(len(S)+1)]
    for i in range(1,len(S)+1):
        for j in range(1,len(S)+1):
            if S[i-1]==rev[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[len(S)][len(S)]