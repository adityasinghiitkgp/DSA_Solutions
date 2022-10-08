def maxSum(arr,n):
    rev=sorted(arr,reverse=True)
    arr.sort()
    i=0
    sumi=0
    
    while i<n:
        sumi+=abs(rev[i]-arr[i])
        i+=1
    return sumi