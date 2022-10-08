def findMaxLen(ob, S):
    mx=0
    lis=[]
    lis.append(-1)
    for i in range(len(S)):
        if S[i]=="(":
            lis.append(i)
        else:
            if len(lis)!=0:
                lis.pop()
            
            if len(lis):
                mx=max(mx,i-lis[-1])
            else:
                lis.append(i)
    return mx