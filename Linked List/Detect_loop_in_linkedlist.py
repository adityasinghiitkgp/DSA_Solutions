def detectLoop(self, head):
    d={}
    curr=head
    while curr:
        if curr not in d:
            d[curr]=1
        else:
            return True
        curr=curr.next
    return False