def tour(self,lis, n):
    arr=[]
    for i in range(n):
        arr.append(lis[i][0]-lis[i][1])
    lis=[]
    sumi=0
    d=-1
    flag=True
    for i in range(len(arr)):
        sumi+=arr[i]
        if sumi<0:
            lis.append(sumi)
            sumi=0
            d=i
            flag=False
    if flag==True:
        return 0
    if d==-1:
        return -1
    if sumi+sum(lis)>=0:
        return d+1
    else:
        return -1
    