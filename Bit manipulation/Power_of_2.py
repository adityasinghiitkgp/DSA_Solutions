def isPowerofTwo(self,n):
    if n==0:
        return False
    x=int(math.log(n,2))
    
    if 2**x==n:
        return True
    else:
        return False