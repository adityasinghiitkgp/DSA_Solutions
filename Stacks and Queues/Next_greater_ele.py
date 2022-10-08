def nextLargerElement(self,arr,n):
    lis=[]
    nxt=[-1]*n
    for i in range(n):
        if not lis:
            lis.append(i)
        else:
            while lis and arr[lis[-1]]<arr[i]:
                nxt[lis[-1]]=arr[i]
                lis.pop()
            lis.append(i)
    return nxt