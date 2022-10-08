def rotate( arr, n):
    temp=arr[-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=temp
    return arr
    