def getNthFromLast(head,n):
    count=0
    curr=head
    while curr:
        curr=curr.next
        count+=1
    if head is None or head.next==None:
        return -1
    elif n>count:
        return -1
    x=count-n
    curr=head
    while x:
        curr=curr.next
        x-=1
        
    return curr.data