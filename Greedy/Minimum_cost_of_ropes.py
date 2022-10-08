import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        heapq.heapify(arr)
        ans=0
        while len(arr)>1:

            x=heapq.heappop(arr)
            y=heapq.heappop(arr)
            ans+=(x+y)
            heapq.heappush(arr,x+y)
        return ans
            