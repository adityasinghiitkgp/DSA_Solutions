def copyList(self, head):
    curr=head

    while curr!=None:
        newnode=Node(curr.data)
        newnode.next=curr.next
        curr.next=newnode
        curr=curr.next.next
    
    curr=head
    while curr!=None:
        if curr.arb:
            curr.next.arb=curr.arb.next
        curr=curr.next.next
        
    curr=head
    dupli=head.next
    while curr.next!=None:
        temp=curr.next
        curr.next=curr.next.next
        curr=temp
    return dupli
    