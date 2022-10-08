def solve(mid,n):
    f=5
    count=0
    while mid>=f:
        count+=mid//f
        f*=5
    if count>=n:
        return True
    return False
        
class Solution:
    def findNum(self, n : int):
        if n==1:
            return 5
        
        low=0
        high=n*5
        ans=0
        while low<=high:
            mid=(low+high)//2
            if solve(mid,n):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans