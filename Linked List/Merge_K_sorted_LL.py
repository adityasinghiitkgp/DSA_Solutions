def mergeKLists(self,arr,K):
    lis=[]
    for i in range(K):
        q=arr[i]
        while q:
            lis.append(q.data)
            q=q.next
    
    lis.sort()   
    head=Node(lis.pop(0))
    temp=head
    while lis:
        x=lis.pop(0)
        newNode=Node(x)
        temp.next=newNode
        temp=newNode
        
    return head
        