def removeDuplicates(self, head):
    s=set()
    current=head
    prev=None
    while current.next:
        s.add(current.data)
        if current.next.data in s:
            prev=current.next
            current.next=prev.next
        else:
            current=current.next
    return head