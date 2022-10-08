from collections import defaultdict
def solve(d,arr,v,src):
    v[src]=True
    arr[src]=True
    
    for i in d[src]:
        if not v[i]:
            if solve(d,arr,v,i):
                return True
        else:
            if arr[i]:
                return True
    arr[src]=False
    return False
class Solution:
    def isPossible(self,N,prerequisites):
        d=defaultdict(list)
        for i in range(len(prerequisites)):
            d[prerequisites[i][1]].append(prerequisites[i][0])
        
        arr=[False]*N
        v=[False]*N
        
        for i in range(N):
            if not v[i]:
                if solve(d,arr,v,i):
                    return False
        return True