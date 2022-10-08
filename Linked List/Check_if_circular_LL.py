def isCircular(head):
    temp=head
    current=head
    while current.next:
        if current.next==temp:
            return True
        current=current.next
    return False