
from collections import defaultdict
def solve(d,order,a,b):
    p=len(a)
    q=len(b)
    for i in range(min(p,q)):
        if a[i]!=b[i]:
            d[a[i]].append(b[i])
            order[ord(b[i])-ord("a")]+=1
            break
            
class Solution:
    def findOrder(self,dict, N, K):
        d=defaultdict(list)
        order=[0]*K
        for i in range(N-1):
            solve(d,order,dict[i],dict[i+1])
            
        lis=[]
        for i in range(K):
            if order[i]==0:
                lis.append(i)
            
        ans=[]
        
        while lis:
            x=lis.pop(0)
            word=chr(x+ord("a"))
            ans.append(word)
            
            for i in d[word]:
                z=ord(i)-ord("a")
                order[z]-=1
                if order[z]==0:
                    lis.append(z)
        
        return ans