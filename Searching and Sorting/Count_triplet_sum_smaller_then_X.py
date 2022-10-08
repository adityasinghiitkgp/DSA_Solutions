def countTriplets(self, arr, n, sumo):
    arr.sort()
    count=0
    for i in range(n):
        x=sumo-arr[i]
        j=i+1
        k=n-1
        while j<k:
            if arr[j]+arr[k]<x:
                count+=(k-j)
                j+=1
            else:
                k-=1
    return count