def pageFaults(self, N, C, pages):
    d={}
    count=0
    lis=[]
    for i in pages:
        if i not in d and C:
            d[i]=1
            lis.append(i)
            count+=1
            C-=1
        elif i not in d:
            x=lis.pop(0)
            del d[x]
            d[i]=1
            lis.append(i)
            count+=1
        else:
            lis.remove(i)
            lis.append(i)
            
    return count