def kLargest(self,arr, n, k):
    ans=[]
    arr.sort()
    for i in range(n-1,n-k-1,-1):
        ans.append(arr[i])
        
    return ans
    