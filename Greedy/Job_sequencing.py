def JobScheduling(self,Jobs,n):
    arr=[0]*(n+1)
    lis=[]
    for i in Jobs:
        lis.append([i.deadline,i.profit])
    lis.sort(key=lambda s:s[1], reverse=True)
    
    for i in range(n):
        for j in range(min(n+1,lis[i][0]+1)-1,0,-1):
            if arr[j]==0:
                arr[j]=lis[i][1]
                break
    
    sumi=0
    count=0
    
    for i in range(len(arr)):
        if arr[i]!=0:
            count+=1
            sumi+=arr[i]
    return [count,sumi]