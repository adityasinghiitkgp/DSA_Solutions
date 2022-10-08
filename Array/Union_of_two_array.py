def doUnion(self,a,n,b,m):
    x=[]
    
    se=set()
    for i in a:
        if i not in se:
            x.append(i)
            se.add(i)
    for i in b:
        if i not in se:
            x.append(i)
            se.add(i)
    return len(x)