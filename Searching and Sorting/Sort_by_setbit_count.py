from collections import defaultdict
def solve(i):
    count=0
    while i:
        i=(i &(i-1))
        count+=1
    return count
        
        
class Solution:
    def sortBySetBitCount(self, arr, n):
        d=defaultdict(list)
        for i in arr:
            count=solve(i)
            d[count].append(i)
            
        lis=[]
        d=sorted(d.items(),reverse=True)
        for i in d:
            
            lis.append(i[1])
        arr.clear()
        for i in lis:
            for j in i:
                arr.append(j)
        return arr
        