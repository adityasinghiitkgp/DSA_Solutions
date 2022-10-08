def maximumMeetings(self,n,start,end):
    lis=[]
    for i,j in zip(start,end):
        lis.append([i,j])
    
    lis=sorted(lis,key=lambda x:x[1])
    ans=[]
    for i in lis:
        if not ans or ans[-1][1]<i[0]:
            ans.append(i)
    return len(ans)