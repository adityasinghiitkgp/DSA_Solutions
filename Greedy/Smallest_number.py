def smallestNumber (self, S, D):

    S-=1
    ans=[0]*D
    if S>(9)*D:
        return -1
    
    if S==0 and D==1:
        return 0
    for i in range(D-1,0,-1):
        if S>9:
            ans[i]=9
            S-=9
            
        else:
            ans[i]=S
            S=0
    ans[0]=1+S  
    s=""
    for i in ans:
        s+=str(i)
    return s
