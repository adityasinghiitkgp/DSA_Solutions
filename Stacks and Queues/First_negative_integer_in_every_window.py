
def printFirstNegativeInteger( A, N, K):
    lis=[]
    d=[]
    
    for i in range(K):
        if A[i]<0:
            d.append(i)
            
    for i in range(K,N):
        if not d:
            lis.append(0)
        else:
            lis.append(A[d[0]])
            
        while d and d[0]<=(i-K):
            d.pop(0)
            
        if A[i]<0:
            d.append(i)
    if d:
        lis.append(A[d[0]])
    else:
        lis.append(0)
    return lis
        