def findIntersection(head1,head2):
    prev=None
    head3=linkedList()
    while head1 and head2:
        if head1.data==head2.data:
            temp=Node(head1.data)
            if head3.head is None:
                
                head3.head=temp
            else:
                prev.next=temp
            prev=temp
            head1=head1.next
            head2=head2.next
            
        elif head1.data>head2.data:
            head2=head2.next
        else:
            head1=head1.next
    return head3.head
                