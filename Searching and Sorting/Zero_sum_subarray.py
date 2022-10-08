def findSubArrays(self,arr,n):
    d={}
    count=0
    sumi=0
    d[0]=1
    for i in range(n):
        sumi+=arr[i]

        if sumi not in d:
            d[sumi]=1
        else:
            count+=d[sumi]
            d[sumi]+=1

    return count