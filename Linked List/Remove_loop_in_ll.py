def removeLoop(self, head):
    curr=head
    s=set()
    s.add(head)
    while curr:
        if curr.next in s:
            curr.next=None
        s.add(curr.next)
        curr=curr.next