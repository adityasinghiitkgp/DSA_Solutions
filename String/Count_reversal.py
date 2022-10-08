def countRev (s):
    n=len(s)
    if n%2!=0:
        return -1
    openi=0
    close=0
    lis=[]
    for i in range(n):
        if s[i]=="{":
            lis.append("{")
            openi+=1
        elif s[i]=="}" and len(lis)!=0:
            lis.pop()
            openi-=1
        else:
            close+=1
            
    if openi%2!=0:
        openi=openi//2+1
    else:
        openi=openi//2
    if close%2!=0:
        close=close//2+1
    else:
        close=close//2
    
    return close+openi  