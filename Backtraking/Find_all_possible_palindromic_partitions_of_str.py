def palin(s):
    rev=s[-1::-1]
    if s==rev:
        return True
    return False
def solve(S,ans,curr,n,index):
    if index>=n:
        ans.append(list(curr))
        return 
    for i in range(index,n):
        if palin(S[index:i+1]):
            curr.append(S[index:i+1])
            solve(S,ans,curr,n,i+1)
            curr.pop()
        
class Solution:
    def allPalindromicPerms(self, S):
        ans=[]
        curr=[]
        n=len(S)
        solve(S,ans,curr,n,0)
        return ans