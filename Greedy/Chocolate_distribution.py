def findMinDiff(self, A,N,M):
    if M>N:
        return -1
    A.sort()
    mini=10**99
    i=0
    while i<N-M+1:
        mini=min(mini,A[i+M-1]-A[i])
        i+=1
    return mini