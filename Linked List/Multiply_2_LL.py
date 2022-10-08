def multiplyTwoList(head1, head2):
    s=""
    while head1:
        s+=str(head1.data)
        head1=head1.next
    p=""
    while head2:
        p+=str(head2.data)
        head2=head2.next
        
        
    return (int(s)*int(p))%(10**9+7)
    