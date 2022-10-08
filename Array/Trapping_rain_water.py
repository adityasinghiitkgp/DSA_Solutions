def trappingWater(self, arr,n):
    l=0
    r=n-1
    left=arr[0]
    ans=0
    right=arr[r]
    while l<=r:
        if left<right:
            if arr[l]>left:
                left=arr[l]
            else:
                ans+=(left-arr[l])
            l+=1
        else:
            if arr[r]>right:
                right=arr[r]
            else:
                ans+=(right-arr[r])
            r-=1
    return ans