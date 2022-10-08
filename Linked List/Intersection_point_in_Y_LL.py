   
    
def length(head):
    count=0
    while head:
        count+=1
        head=head.next
    return count
    
def intersetPoint(head1,head2):
    p=length(head1)
    q=length(head2)
    
    if p==q:
        while head1!=None and head2!=None:
            if head1==head2:
                return head1.data
            else:
                head1=head1.next
                head2=head2.next
    i=0      
    while head1!=None and head2!=None and i<abs(p-q):
        if p>q:
            head1=head1.next
        else:
            head2=head2.next
        i+=1
    
    while head1!=None and head2!=None:
        if head1==head2:
            return head1.data
        else:
            head1=head1.next
            head2=head2.next
    
    return -1