def setBits(self, N):
    count=0
    while N>0:
        N=(N&(N-1))
        count+=1
    return count