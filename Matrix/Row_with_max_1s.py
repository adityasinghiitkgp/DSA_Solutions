def rowWithMax1s(self,arr, n, m):
    maxi=0
    ans=-1
    for i in range(len(arr)):
        sumi=sum(arr[i])
        if sumi>maxi:
            maxi=sumi
            ans=i
    return ans