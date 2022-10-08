def findPair(self, arr, L,N):
    arr.sort()
    i=0
    j=1
    A=arr
    while i<L and j<L:
        if A[j]-A[i]==N and i!=j:
            return True
        elif A[j]-A[i]>N:
            i+=1
        else:
            j+=1
    return False