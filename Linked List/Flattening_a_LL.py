    
def sorte(a,b):
    res=None
    if a==None:
        return b
    elif b==None:
        return a
    elif a.data>b.data:
        res=b
        res.bottom=sorte(a,b.bottom)
    else:
        res=a
        res.bottom=sorte(a.bottom,b)
    return res
    

def flatten(root):
    start=root
    if start is None:
        return
    
    res=sorte(start,flatten(start.next))
    
    return res