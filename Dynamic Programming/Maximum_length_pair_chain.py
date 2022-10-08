class Solution:
    def findLongestChain(self, pairs):
        if not pairs:
            return 0
        pairs.sort()
        dp=[1]*len(pairs)
        
        for i in range(1,len(pairs)):
            for j in range(0,i):
                if pairs[i][0]>pairs[j][1]:
                    dp[i]=dp[j]+1
        return dp[len(pairs)-1]