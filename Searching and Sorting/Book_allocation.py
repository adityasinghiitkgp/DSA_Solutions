

def binary(arr,n,m,mid):
    current_sum=0
    student=1
    for i in range(n):
        if arr[i]>mid:
            return False
        if current_sum + arr[i]> mid:
            student+=1
            current_sum=arr[i]
            if student>m:
                return False
        else:
            current_sum+=arr[i]
    return True
    
class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,arr, n, m):
        if n<m:
            return -1
        sumi=0
        for i in range(n):
            sumi+=arr[i]
        start=0
        end=sumi
        result=10**9
        while start<=end:
            mid=(start+end)//2
            if binary(arr,n,m,mid):
                result=min(result,mid)
                end=mid-1
            else:
                start=mid+1
        return result