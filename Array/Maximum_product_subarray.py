def maxProduct(self,arr, n):
    small=arr[0]
    big=arr[0]
    ans=arr[0]
    for i in range(1,n):
        if arr[i]<0:
            big,small=small,big
        small=min(arr[i],small*arr[i])
        big=max(arr[i],big*arr[i])
        ans=max(ans,big)
    return ans