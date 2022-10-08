def maxSubstring(self, S):
    if S[0]=="1":
        curr=-1
        maxi=-1
    else:
        curr=+1
        maxi=+1
    
    for i in range(1,len(S)):
        if S[i]=="1":
            curr=max(-1,curr-1)
            maxi=max(curr,maxi)
        else:
            curr=max(1,curr+1)
            maxi=max(curr,maxi)
    return maxi