def mergeKArrays(self, arr, K):
    lis=[]
    ans=[]
    m=len(arr[0])
    if m==0:
        return []
    for i in range(K):
        heapq.heappush(lis,(arr[i][0],i,0))
        
    while lis:
        top=heapq.heappop(lis)
        ans.append(top[0])

        if top[2]==m-1:
            continue
        list_num=top[1]
        ele_num=top[2]+1
        heapq.heappush(lis,(arr[list_num][ele_num],list_num,ele_num))
    return ans