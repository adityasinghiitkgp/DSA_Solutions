
def getPairsCount(self,arr, n, k):
    count=0
    d={}
    for i in range(n):
        x=k-arr[i]
        if x in d:
            count+=d[x]
        if arr[i] not in d:
            d[arr[i]]=1
        else:
            d[arr[i]]+=1
    return count