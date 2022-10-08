def solve(A,B,ans,lis,index):
    if B==0:
        ans.append(list(lis))
        return 
    for i in range(index,len(A)):
        if A[i]<=B:
            lis.append(A[i])
            solve(A,B-A[i],ans,lis,i)
            lis.pop()
    
class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,A, B):
        ans=[]
        lis=[]
        A=sorted(list(set(A)))
        solve(A,B,ans,lis,0)
        return ans
        