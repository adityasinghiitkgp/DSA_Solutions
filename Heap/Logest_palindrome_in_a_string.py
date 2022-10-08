def longestPalin(self, S):
    lenght=0
    i=0
    j=len(S)
    ans=[]
    while i<j:
        m=i
        while i+1<j and S[i]==S[i+1]:
            i+=1
        
        p=i
        while m-1>=0 and p+1<j and S[m-1]==S[p+1]:
            m-=1
            p+=1
        
        x=p-m+1
        if x>lenght:
            ans=S[m:p+1]
            lenght=x
        i+=1
    return ans