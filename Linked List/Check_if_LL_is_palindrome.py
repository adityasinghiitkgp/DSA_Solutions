

def reverse(head):
    prev=None
    curr=head
    while curr:
        new=curr.next
        curr.next=prev
        prev=curr
        curr=new
    return prev
    
def middle(head):
    slow=head
    fast=head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    return slow
    
class Solution:
    def isPalindrome(self, head):
        
        mid=middle(head)
        next_mid=mid.next
        mid.next=None
        
        rev_mid=reverse(next_mid)
        while rev_mid and head:
            if rev_mid.data!=head.data:
                return False
            rev_mid=rev_mid.next
            head=head.next
        return True