def smallestWindow(self, s, p):
    
    n=len(s)
    m=len(p)
    d={}
    count=0
    start=0
    ans=[0]*n

    new=s
    for i in range(n):
        if s[i] in d.keys():
            d[s[i]]+=1
        else:
            d[s[i]]=1
            if s[i] in p:
                count+=1
                
        if count==m:
            while d[s[start]]>1 or s[start] not in p:
                d[s[start]]-=1
                start+=1
                
                
            ans=s[start:i+1]
            if len(ans)<len(new):
                new=ans
                
                
    if count!=m:
        return -1
    else:
        return new
            