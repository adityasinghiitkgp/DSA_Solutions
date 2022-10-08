def valueEqualToIndex(self,arr, n):
    lis=[]
    for i in range(n):
        if arr[i]==i+1:
            lis.append(i+1)
    return lis