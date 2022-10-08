def findPosition(self, N):
    if N<=0:
        return -1
    x=int(math.log(N,2))
    if 2**x==N:
        return x+1
    else:
        return -1