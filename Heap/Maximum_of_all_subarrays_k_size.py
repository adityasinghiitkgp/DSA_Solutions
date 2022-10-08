def max_of_subarrays(self,arr,n,k):
    maxi=[]
    for i in range(k):
        while maxi and arr[maxi[-1]]<arr[i]:
            maxi.pop()
        maxi.append(i)
    ans=[]
    
    for i in range(k,n):
        ans.append(arr[maxi[0]])
        while maxi and maxi[0]<=i-k:
            maxi.pop(0)
        while maxi and arr[maxi[-1]]<arr[i]:
            maxi.pop()
        maxi.append(i)
    ans.append(arr[maxi[0]])
    return ans
        