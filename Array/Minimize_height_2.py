def getMinDiff(self, arr, n, k):
    small=0
    big=0
    arr.sort()
    ans=arr[-1]-arr[0]
    for i in range(1,n):
        if arr[i]>=k:
            small=min(arr[0]+k,arr[i]-k)
            big=max(arr[-1]-k,arr[i-1]+k)
            ans=min(ans,big-small)
    return ans