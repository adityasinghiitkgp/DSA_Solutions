def removeDuplicates(head):
    prev=None
    current=head
    while current!=None and current.next:
        if current.data==current.next.data:
            prev=current.next
            current.next=prev.next
        else:
            current=current.next
    return head