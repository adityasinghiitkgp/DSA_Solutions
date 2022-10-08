
def middle(head):
    slow=head
    fast=head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    return slow

class Solution:
    def splitList(self, head, head1, head2):
        
        curr=head
        while curr.next!=head:
            curr=curr.next
        curr.next=None
        
        mid=middle(head)
            
        head1=head
        head2=mid.next
        mid.next=head1
        
        curr=head2
        while curr.next:
            curr=curr.next
        curr.next=head2
        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2