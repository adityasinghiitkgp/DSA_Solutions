def nextPermutation(self, N, arr):
    just_big=-1
    index=-1
    swap=-1
    if N==0:
        return []

    for i in range(N-1,0,-1):
        if arr[i]>arr[i-1]:
            just_big=arr[i]
            index=i
            break
    if just_big==-1:
        arr.sort()
        return arr
        
    for i in range(index,N):
        if arr[i]>arr[index-1] and arr[i]<=just_big:
            just_big=arr[i]
            swap=i
    arr[index-1],arr[swap]=arr[swap],arr[index-1]
    
    i=index
    j=N-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    
    return arr