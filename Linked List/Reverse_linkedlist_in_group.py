def reverse(self,head, k):
    prev=None
    current=head
    count=0
    while current!=None and count<k:
        next_variable=current.next
        current.next=prev
        prev=current
        current=next_variable
        count+=1
        
    if current!=None:
        head.next=self.reverse(current,k)
    return prev
