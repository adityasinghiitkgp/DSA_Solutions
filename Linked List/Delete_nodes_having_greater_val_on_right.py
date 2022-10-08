def reverse(head):
    pre=None
    curr=head
    while curr:
        new=curr.next
        curr.next=pre
        pre=curr
        curr=new
    return pre
    
class Solution:
    def compute(self,head):
        temp=reverse(head)
        curr=temp
        while curr and curr.next:
            if curr.data>curr.next.data:
                curr.next=curr.next.next
            else:
                curr=curr.next
        head=reverse(temp)
        return head
        