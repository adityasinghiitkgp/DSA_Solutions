def AllPossibleStrings(self, s):
    n=len(s)
    res=[]
    for i in range(1,1<<n):
        a=""
        for j in range(0,n):
            if (i & 1<<j):
                a+=str(s[j])
        res.append(a)
    res.sort()
    return res
