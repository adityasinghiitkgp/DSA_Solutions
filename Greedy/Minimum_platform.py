def minimumPlatform(self,n,arr,dep):
    arr.sort()
    dep.sort()
    count=0
    i=0
    j=0
    while i<len(arr) and j<len(dep):
        if dep[j]>=arr[i]:
            count+=1
            i+=1
        else:
            i+=1
            j+=1
    return count