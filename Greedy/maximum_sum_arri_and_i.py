def Maximize(self, a, n): 
    a=sorted(a)
    maxi=0
    for i in range(n):
        maxi+=(a[i]*i)
    return maxi%(10**9+7)