def minimumNumberOfSwaps(self,S):
    opening=[]
    for i in range(len(S)):
        if S[i]=="[":
            opening.append(i)
            
    ans=0
    openi=0
    pos=0
    S=list(S)
    
    for i in range(len(S)):
        if S[i]=="[":
            openi+=1
            pos+=1
        else:
            openi-=1
        
        if openi<0:
            ans+=(opening[pos]-i)
            S[i],S[opening[pos]]=S[opening[pos]],S[i]
            openi=1
            pos+=1
    return ans