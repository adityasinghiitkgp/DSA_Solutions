from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        lis=[]
        for k,v in count.items():
            heapq.heappush(lis,(-v,k))
        
        remaining_count=0
        remaining_string=""
        ans=""
        while lis:
            a,b=heapq.heappop(lis)
            
            ans+=b
            if remaining_count<0:
                heapq.heappush(lis,(remaining_count,remaining_string))
            
            a+=1
            remaining_count=a
            
            remaining_string=b
         
        if len(ans)!=len(s):
            return ""

        return ans

                               
                               