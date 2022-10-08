def maximizeSum(self, a, n, k):
    sumi=0
    a.sort()
    for i in range(n):
        if a[i]<0 and k:
            a[i]*=-1
            k-=1
    
    if k%2==0:
        return sum(a)
    else:
        sumi=sum(a)
        return sumi-(min(a)*2)
