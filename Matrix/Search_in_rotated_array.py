def solve(l,r,key,A):
    while l<=r:
        mid=(l+r)//2
        if A[mid]==key:
            return mid
        elif A[mid]>key:
            r=mid-1
        else:
            l=mid+1
    return -1
            
        
class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                break
        x=A[0:i+1]
        y=A[i+1:]
        
        a=solve(0,len(x)-1,key,x)
        if a!=-1:
            return a
        b=solve(0,len(y)-1,key,y)
        if b!=-1:
            return len(x)+b
        return -1