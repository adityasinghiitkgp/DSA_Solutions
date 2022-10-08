def findSubString(self, st):
    
    n=len(st)
    ans=0
    lenght=n
    s=list(set(st))
    d=dict()
    count=0
    start=0
    for i in range(n):
    
        if st[i] not in d.keys():
            d[st[i]]=1
            count+=1
        else:
            d[st[i]]+=1
            
        if count==len(s):
            while d[st[start]]>1:
                d[st[start]]-=1
                start+=1
                
            ans=i-start+1
            if lenght>ans:
                lenght=ans
    return lenght