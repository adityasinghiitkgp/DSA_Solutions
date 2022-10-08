class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        dp = [10**9] * n
        dp[src] = 0

        for _ in range(min(n - 1, k + 1)):
            # min(n - 1, k + 1): at most how many hops
            temp = dp.copy()
            
            for f, t, p in flights:
                temp[t] = min(temp[t], dp[f] + p)
            dp = list(temp)

        return dp[dst] if dp[dst] != 10**9 else -1