def minValue(self, s, k):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
            
    lis=[]
    for v in d.values():
        lis.append(v)
        
    while k:
        x=lis.index(max(lis))
        lis[x]-=1
        k-=1
    sumi=0
    for i in lis:
        sumi+=i**2
    return sumi
