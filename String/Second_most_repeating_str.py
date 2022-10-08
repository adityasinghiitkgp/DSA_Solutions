def secFrequent(self, arr, n):
    d=dict()
    max1=0
    max2=0
    for i in arr:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    maxi=-10**9
    for k,v in d.items():
        if v>maxi:
            maxi=v
            key=k
    
    del d[key]
    maxi=-10**9
    
    for k,v in d.items():
        if v>maxi:
            maxi=v
            key=k
    return key
    