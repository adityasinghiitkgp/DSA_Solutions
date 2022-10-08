def commonElements (self,A, B, C, n1, n2, n3):
        
    i=0
    j=0
    k=0
    res=[]
    while i<n1 and j<n2 and k<n3:
        if A[i]==B[j] and A[i]==C[k]:
            res.append(A[i])
            i+=1
            j+=1
            k+=1
        elif A[i]>B[j]:
            j+=1
        elif A[i]>C[k]:
            k+=1
        else:
            i+=1
    res=set(res)
    res=list(sorted(res))
    return res    