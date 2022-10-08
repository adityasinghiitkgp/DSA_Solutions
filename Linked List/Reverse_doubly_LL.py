def reverseDLL(head):
    pre=None
    curr=head
    while curr:
        new=curr.next
        curr.next=pre
        curr.prev=new
        pre=curr
        curr=new
    return pre
