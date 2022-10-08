def find3Numbers(self,A, n, X):
    A.sort()
    for i in range(n):
        sumi=X-A[i]
        j=i+1
        k=n-1
        
        while j<k:
            if sumi==A[j]+A[k]:
                return True
            elif sumi<A[j]+A[k]:
                k-=1
            else:
                j+=1
    return False