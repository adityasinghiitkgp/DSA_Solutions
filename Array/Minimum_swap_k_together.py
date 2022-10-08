
def minSwap (arr, n, k) : 
    good=0
    for i in range(n):
        if arr[i]<=k:
            good+=1
    bad=0
    for i in range(good):
        if arr[i]>k:
            bad+=1
    
    ans=bad
    j=good
    for i in range(n):
        if j==n:
            break
        if arr[i]>k:
            bad-=1
        if arr[j]>k:
            bad+=1
        ans=min(ans,bad)
        j+=1
    return ans