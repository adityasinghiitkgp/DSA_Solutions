def findTwoElement( self,arr, n):
    s=set()
    lis=[]
    for i in range(n):
        x=len(s)
        s.add(arr[i])
        y=len(s)
        if x==y:
            lis.append(arr[i])
            break
    
    total=(n*(n+1))/2
    curr=sum(arr)
    if curr>total:
        lis.append(int(lis[0]-(curr-total)))
    else:
        lis.append(int(lis[0]+(total-curr)))
    return lis