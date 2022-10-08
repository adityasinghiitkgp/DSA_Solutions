def smallestSubWithSum(self, a, n, x):
    sumi=0
    ans=10**9
    j=0
    for i in range(n):
        sumi+=a[i]
        if sumi>x:
            while sumi>x:
                ans=min(ans,i-j+1)
                sumi-=a[j]
                j+=1
    
    return ans