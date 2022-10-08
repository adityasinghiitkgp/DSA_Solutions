def FirstNonRepeating(self, A):
    lis=[]
    res=""
    d={}
    for i in A:
        lis.append(i)
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        
        while lis:
            if d[lis[0]]>1:
                lis.pop(0)
            else:
                res+=lis[0]
                break
        if not lis:
            res+="#"
    return res