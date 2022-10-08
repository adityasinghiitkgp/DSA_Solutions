def reverseList(self, head):
    prev=None
    current=head
    while current!=None:
        next_variable=current.next
        current.next=prev
        prev=current
        current=next_variable
        
    return prev