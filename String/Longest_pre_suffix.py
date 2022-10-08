def lps(self, s):
    l=[0]*len(s)
    i=0
    n=len(s)
    j=1
    while j<n:
        if s[i]==s[j]:
            l[j]=i+1
            i+=1
            j+=1
        else:
            if i-1>=0:
                i=l[i-1]
            else:
                i=0
                j+=1
    return l[-1]